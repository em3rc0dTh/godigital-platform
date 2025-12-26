# !pip install -q transformers torch beautifulsoup4 pandas lxml

import re
import json
import pandas as pd
from bs4 import BeautifulSoup
from transformers import pipeline
from typing import Dict, Optional, List, Tuple, Any
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class UltraReceiptExtractor:
    """Extractor híbrido ultra-robusto para recibos HTML"""
    
    def __init__(self):
        print("🧠 Inicializando extractor híbrido avanzado...")
        self._init_ai_model()
        self.patterns = self._build_comprehensive_patterns()
        print("✅ Sistema completamente configurado")
    
    def _init_ai_model(self):
        """Inicializa el modelo de IA con manejo de errores"""
        try:
            self.qa_pipeline = pipeline(
                "question-answering",
                model="mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es",
                tokenizer="mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es"
            )
            self.ai_available = True
            print("✅ Modelo IA cargado correctamente")
        except Exception as e:
            print(f"⚠️ IA no disponible (modo solo regex): {str(e)[:60]}")
            self.ai_available = False
    
    def _build_comprehensive_patterns(self) -> Dict:
        """Construye patrones regex exhaustivos con transformadores y confianza"""
        return {
            'Monto': [
                # Ultra-específico: dentro del estilo morado de Yape
                (r'color:rgb\(96,3,145\)[^>]*?>([0-9,.]+)', 
                 lambda m: f"S/ {m.group(1).replace(',', '')}", 0.99),
                # Con S/ explícito y espacios
                (r'S/\s*([\d,]+\.?\d*)', 
                 lambda m: f"S/ {m.group(1).replace(',', '')}", 0.98),
                # En celda después de "Monto de yapeo"
                (r'(?:Monto\s+de\s+yapeo|Monto)[^<]*?<[^>]*?>([\d,.]+)', 
                 lambda m: f"S/ {m.group(1).replace(',', '')}", 0.96),
                # En tabla con etiqueta "Monto"
                (r'<td[^>]*>Monto[^<]*</td>\s*<td[^>]*>S/\s*([\d,.]+)', 
                 lambda m: f"S/ {m.group(1).replace(',', '')}", 0.95),
                # Decimal aislado (último recurso)
                (r'(?<![0-9])(\d{1,4}\.\d{2})(?![0-9])', 
                 lambda m: f"S/ {m.group(1)}", 0.75),
            ],
            
            'Fecha': [
                # Formato completo español con am/pm
                (r'(\d{1,2}\s+(?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\s+\d{4}\s*-\s*\d{1,2}:\d{2}\s*[ap]\.\s*m\.)', 
                 lambda m: m.group(1), 0.99),
                # Formato corto con barra
                (r'(\d{1,2}/\d{1,2}/\d{4}\s+\d{1,2}:\d{2}(?:\s*[ap]\.?\s*m\.?)?)', 
                 lambda m: m.group(1), 0.95),
                # ISO format
                (r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2})', 
                 lambda m: m.group(1), 0.90),
            ],
            
            'Operacion': [
                # Después de etiquetas específicas
                (r'(?:N°|Nº|n[uú]mero)\s*(?:de\s+)?operaci[oó]n[:\s]*(\d{6,8})', 
                 lambda m: m.group(1), 0.99),
                # En tabla estructurada
                (r'<td[^>]*>N°?\s*de\s*operaci[oó]n</td>\s*<td[^>]*>(\d{6,8})', 
                 lambda m: m.group(1), 0.98),
                # Número aislado de 7 dígitos (común en Yape)
                (r'(?<![0-9])(\d{7})(?![0-9])', 
                 lambda m: m.group(1), 0.85),
            ],
            
            'Origen': [
                # Saludo personalizado (máxima prioridad)
                (r'¡Hola,\s*([A-ZÑÁÉÍÓÚ][A-ZÑÁÉÍÓÚ\s.]+?)!', 
                 lambda m: self._clean_name(m.group(1)), 0.99),
                # En tabla como "Yapero"
                (r'(?:Yapero|yapeo)[^<]*?<[^>]*?>([A-ZÑÁÉÍÓÚ][A-ZÑÁÉÍÓÚ\s.]+?)(?:<|$)', 
                 lambda m: self._clean_name(m.group(1)), 0.98),
                # Como "remitente" u "origen"
                (r'(?:remitente|origen)[:\s]*([A-ZÑÁÉÍÓÚ][A-ZÑÁÉÍÓÚ\s.]+?)(?:\s*<|$)', 
                 lambda m: self._clean_name(m.group(1)), 0.92),
                # En tabla estructurada
                (r'<td[^>]*>Yapero</td>\s*<td[^>]*>([A-ZÑÁÉÍÓÚ][^<]+)', 
                 lambda m: self._clean_name(m.group(1)), 0.95),
            ],
            
            'Origen_Cuenta': [
                # Celular del yapero con contexto
                (r'(?:Tu\s+n[uú]mero\s+de\s+celular|celular)[^<]*?X+([\d]{3,4})', 
                 lambda m: f"XXXXXXXXX{m.group(1)}", 0.99),
                # Primera cuenta enmascarada en el documento
                (r'X{5,}([\d]{3,4})(?![X0-9])', 
                 lambda m: f"XXXXXXXXX{m.group(1)}", 0.88),
            ],
            
            'Destino': [
                # Patrón "Yapeaste X a NOMBRE"
                (r'Yapeaste[^<]*?a\s*<[^>]*?>\s*([A-ZÑÁÉÍÓÚ][A-ZÑÁÉÍÓÚ\s.]+?)(?:\s*<|$)', 
                 lambda m: self._clean_name(m.group(1)), 0.99),
                # Como "Nombre del Beneficiario"
                (r'(?:Nombre\s+del\s+)?[Bb]eneficiario[^<]*?<[^>]*?>([A-ZÑÁÉÍÓÚ][A-ZÑÁÉÍÓÚ\s.]+?)(?:<|$)', 
                 lambda m: self._clean_name(m.group(1)), 0.98),
                # En tabla estructurada
                (r'<td[^>]*>Nombre del Beneficiario</td>\s*<td[^>]*>([A-ZÑÁÉÍÓÚ][^<]+)', 
                 lambda m: self._clean_name(m.group(1)), 0.97),
                # Como "para" o "destino"
                (r'(?:para|destino|recibe)[:\s]*([A-ZÑÁÉÍÓÚ][A-ZÑÁÉÍÓÚ\s.]+?)(?:\s*<|$)', 
                 lambda m: self._clean_name(m.group(1)), 0.90),
            ],
            
            'Destino_Cuenta': [
                # Celular del beneficiario con contexto
                (r'(?:Celular\s+del\s+)?[Bb]eneficiario[^<]*?X+([\d]{3,4})', 
                 lambda m: f"XXXXXXXXX{m.group(1)}", 0.99),
                # Segunda cuenta enmascarada (después de encontrar origen)
                (r'X{5,}([\d]{3,4})(?![X0-9])', 
                 lambda m: f"XXXXXXXXX{m.group(1)}", 0.75),
            ],
        }
    
    def _clean_name(self, name: str) -> str:
        """Limpia y normaliza nombres propios"""
        name = re.sub(r'\s+', ' ', name).strip()
        name = re.sub(r'\s+[A-Z]\.$', '', name)  # Quitar iniciales finales
        name = name.replace(' .', '.').replace('..', '.')
        name = name.strip(' .,')
        return name
    
    def clean_html(self, html: str) -> Tuple[str, str]:
        """
        Limpia HTML y retorna tupla (texto_estructurado, html_limpio)
        Preserva estructura para patrones complejos
        """
        soup = BeautifulSoup(html, 'lxml')
        
        # Eliminar elementos no informativos
        for tag in soup(['script', 'style', 'meta', 'noscript', 'link', 'img']):
            tag.decompose()
        
        # Preservar HTML limpio para regex estructural
        html_clean = str(soup)
        
        # Extraer datos de tablas de forma estructurada
        table_data = []
        for table in soup.find_all('table'):
            for tr in table.find_all('tr'):
                cells = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
                if len(cells) >= 2:
                    table_data.append(f"{cells[0]}: {cells[1]}")
        
        # Convertir a texto plano
        text = soup.get_text(separator=' | ', strip=True)
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\|\s+\|', '|', text)
        
        # Priorizar datos tabulares al inicio
        if table_data:
            structured_text = '\n'.join(table_data) + '\n\n' + text
        else:
            structured_text = text
        
        return structured_text, html_clean
    
    def extract_with_patterns(self, html: str, text: str, field: str) -> Optional[Dict]:
        """
        Extrae usando patrones regex con validación exhaustiva
        Busca en HTML estructurado primero, luego en texto
        """
        if field not in self.patterns:
            return None
        
        best_match = None
        best_confidence = 0.0
        used_values = set()  # Para tracking de cuentas
        
        for pattern, transform, confidence in self.patterns[field]:
            # Búsqueda en HTML (más precisa)
            sources = [(html, 'html'), (text, 'text')]
            
            for source, source_type in sources:
                try:
                    matches = list(re.finditer(pattern, source, re.IGNORECASE | re.DOTALL))
                    
                    for match in matches:
                        value = transform(match)
                        
                        # Validación robusta
                        if not self._validate_value(field, value, used_values):
                            continue
                        
                        # Sistema de scoring mejorado
                        actual_confidence = confidence
                        if source_type == 'html':
                            actual_confidence += 0.01  # Bonus por HTML
                        
                        if actual_confidence > best_confidence:
                            best_match = value
                            best_confidence = actual_confidence
                            
                            # Tracking para cuentas (evitar duplicados)
                            if field in ['Origen_Cuenta', 'Destino_Cuenta']:
                                used_values.add(value)
                            
                            break  # Tomar primer match del patrón de mayor confianza
                    
                    if best_match:
                        break  # Ya encontramos un buen match
                        
                except Exception as e:
                    continue
            
            if best_match:
                break  # Ya tenemos el mejor resultado posible
        
        if best_match:
            return {
                'value': best_match,
                'confidence': round(best_confidence, 3),
                'method': 'regex'
            }
        return None
    
    def _validate_value(self, field: str, value: str, used_values: set = None) -> bool:
        """Validación exhaustiva por tipo de campo"""
        if not value or len(value.strip()) < 2:
            return False
        
        value = value.strip()
        
        if field == 'Monto':
            if not re.search(r'\d', value):
                return False
            if value.strip() in ['S/', 'S', '/', '0', '0.00']:
                return False
            # Validar que el monto tenga sentido
            amount = re.search(r'[\d.]+', value)
            if amount and float(amount.group()) > 100000:  # Monto irreal
                return False
        
        elif field in ['Origen', 'Destino']:
            # Lista negra de palabras
            blacklist = [
                'tu', 'seguridad', 'notificaremos', 'yapeo', 'app', 'presiona',
                'desde', 'interrogación', 'whatsapp', 'oficial', 'celular',
                'operación', 'beneficiario', 'numero', 'fecha', 'hora',
                'exitosamente', 'recuerda', 'compartir', 'clave'
            ]
            
            words = value.lower().split()
            if any(word in blacklist for word in words):
                return False
            
            # Debe empezar con mayúscula
            if not value[0].isupper():
                return False
            
            # Debe tener al menos una letra
            if not re.search(r'[A-Z]', value):
                return False
            
            # No debe ser muy largo (probable basura)
            if len(value) > 50:
                return False
        
        elif field in ['Origen_Cuenta', 'Destino_Cuenta']:
            # Formato exacto de cuenta enmascarada
            if not re.match(r'^X{5,}\d{3,4}$', value):
                return False
            
            # Evitar duplicados entre Origen y Destino
            if used_values and value in used_values:
                return False
        
        elif field == 'Operacion':
            # Solo números de 6-8 dígitos
            if not re.match(r'^\d{6,8}$', value):
                return False
        
        elif field == 'Fecha':
            # Debe tener números y elementos de fecha
            if not re.search(r'\d', value):
                return False
            # Validar formato mínimo
            if not (re.search(r'[\d/\-:]', value) or 
                   any(mes in value.lower() for mes in 
                       ['enero','febrero','marzo','abril','mayo','junio',
                        'julio','agosto','septiembre','octubre','noviembre','diciembre'])):
                return False
        
        return True
    
    def extract_with_ai(self, context: str, question: str, min_score: float = 0.02) -> Optional[Dict]:
        """Extracción con IA optimizada para contextos largos"""
        if not self.ai_available or len(context) < 50:
            return None
        
        try:
            # Optimizar contexto para IA
            if len(context) > 1500:
                lines = context.split('\n')
                relevant_parts = []
                
                # Tomar inicio (saludo, encabezado)
                relevant_parts.append('\n'.join(lines[:25]))
                
                # Buscar sección con datos clave
                for i, line in enumerate(lines):
                    if any(kw in line.lower() for kw in 
                          ['yapero', 'beneficiario', 'operación', 'monto', 'celular']):
                        relevant_parts.append('\n'.join(lines[max(0,i-5):min(len(lines),i+25)]))
                        break
                
                context = ' | '.join(relevant_parts)[:2000]
            
            result = self.qa_pipeline(question=question, context=context)
            
            if result['score'] >= min_score:
                value = result['answer'].strip(' .:,<>/\\')
                
                return {
                    'value': value,
                    'confidence': round(result['score'], 3),
                    'method': 'ai'
                }
                
        except Exception as e:
            pass
        
        return None
    
    def analyze(self, html: str) -> Dict:
        """Análisis completo híbrido con todas las capas de fallback"""
        # Limpieza y preparación
        text, html_clean = self.clean_html(html)
        
        if len(text) < 50:
            return {"error": "Contenido HTML insuficiente para análisis"}
        
        print(f"📄 Procesando {len(text)} caracteres de texto...")
        
        # Preguntas optimizadas para IA
        ai_questions = {
            'Monto': '¿Cuál es el monto exacto en soles? Solo el número.',
            'Fecha': '¿Cuándo ocurrió esta transacción? Fecha y hora completa.',
            'Operacion': '¿Cuál es el número de operación? Solo dígitos.',
            'Origen': '¿Cómo se llama quien envía el dinero?',
            'Origen_Cuenta': '¿Cuál es el celular de quien envía?',
            'Destino': '¿Quién recibe el dinero? Solo el nombre.',
            'Destino_Cuenta': '¿Cuál es el celular del beneficiario?',
        }
        
        results = {}
        used_accounts = set()
        
        # Extracción ordenada por prioridad
        for field in ['Monto', 'Fecha', 'Operacion', 'Origen', 'Origen_Cuenta',
                      'Destino', 'Destino_Cuenta']:
            
            result = None
            
            # NIVEL 1: Regex en HTML estructurado
            result = self.extract_with_patterns(html_clean, text, field)
            
            # NIVEL 2: IA como fallback
            if not result and field in ai_questions:
                result = self.extract_with_ai(text, ai_questions[field])
                
                # Validar output de IA
                if result:
                    if not self._validate_value(field, result['value'], used_accounts):
                        result = None
                    elif field in ['Origen_Cuenta', 'Destino_Cuenta']:
                        used_accounts.add(result['value'])
            
            # Guardar resultados
            if result:
                results[field] = result['value']
                results[f'{field}_confianza'] = result['confidence']
                results[f'{field}_metodo'] = result['method']
            else:
                results[field] = None
                results[f'{field}_confianza'] = 0.0
                results[f'{field}_metodo'] = 'none'
        
        # Campos derivados con alta confianza
        results['Moneda'] = 'PEN' if results.get('Monto') else None
        results['Moneda_confianza'] = 0.95 if results['Moneda'] else 0.0
        results['Moneda_metodo'] = 'inferencia'
        
        results['Servicio'] = 'Yapeo' if results.get('Monto') else None
        results['Servicio_confianza'] = 0.92 if results['Servicio'] else 0.0
        results['Servicio_metodo'] = 'inferencia'
        
        return results
    
    def analyze_batch(self, html_list: List[str]) -> pd.DataFrame:
        """Procesa múltiples HTMLs y retorna DataFrame unificado"""
        results = []
        total = len(html_list)
        
        for i, html in enumerate(html_list, 1):
            print(f"\n{'='*70}")
            print(f"📋 Documento {i}/{total}")
            result = self.analyze(html)
            result['doc_id'] = i
            results.append(result)
        
        return pd.DataFrame(results)
    
    def to_json(self, result: Dict, indent: int = 2, include_metadata: bool = False) -> str:
        """Convierte resultado a JSON"""
        if include_metadata:
            clean = result
        else:
            clean = {k: v for k, v in result.items()
                    if not k.endswith(('_confianza', '_metodo')) and k not in ['error', 'doc_id']}
        
        return json.dumps(clean, ensure_ascii=False, indent=indent)
    
    def to_dataframe(self, result: Dict, show_details: bool = False) -> pd.DataFrame:
        """Convierte a DataFrame visualizable"""
        df = pd.DataFrame([result])
        
        if not show_details:
            cols = [c for c in df.columns
                   if not c.endswith(('_confianza', '_metodo')) and c != 'doc_id']
            df = df[cols]
        
        return df.T.rename(columns={0: 'Valor'})

# ============================================================================
# API SIMPLIFICADA
# ============================================================================

def extraer(html: str, formato: str = 'tabla', detalles: bool = False) -> Any:
    """
    API simplificada para extracción de datos
    
    Args:
        html: Contenido HTML del recibo
        formato: 'tabla', 'json', 'dict'
        detalles: Incluir confianza y método
    
    Returns:
        Datos en el formato especificado
    """
    extractor = UltraReceiptExtractor()
    resultado = extractor.analyze(html)
    
    if formato == 'json':
        return extractor.to_json(resultado, include_metadata=detalles)
    elif formato == 'dict':
        if detalles:
            return resultado
        return {k: v for k, v in resultado.items()
                if not k.endswith(('_confianza', '_metodo'))}
    else:  # tabla
        return extractor.to_dataframe(resultado, show_details=detalles)

def extraer_batch(html_list: List[str]) -> pd.DataFrame:
    """Procesa múltiples HTMLs"""
    extractor = UltraReceiptExtractor()
    return extractor.analyze_batch(html_list)


MESES = {
    "enero": 1,
    "febrero": 2,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "setiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12
}

def adapt_to_transaction_schema(result: Dict) -> Dict:

    def parse_amount(val):
        if not val:
            return None
        num = re.search(r"[\d.]+", val)
        return float(num.group()) if num else None

    def parse_date(val):
        if not val:
            return None

        val = val.lower().strip()

        # 20 septiembre 2023 - 04:19 p. m.
        # 21 de diciembre de 2025 - 08:08 PM
        match = re.search(
            r"(\d{1,2})\s+de\s+([a-záéíóú]+)\s+de\s+(\d{4})\s*-\s*(\d{1,2}):(\d{2})\s*(am|pm)",
            val,
            re.IGNORECASE
        )

        if not match:
            return None

        day, month_name, year, hour, minute, meridian = match.groups()
        month = MESES.get(month_name)

        if not month:
            return None

        hour = int(hour)
        minute = int(minute)

        if "p" in meridian.lower() and hour < 12 or "pm" in meridian.lower() and hour < 12:
            hour += 12
        if "a" in meridian.lower() and hour == 12 or "am" in meridian.lower() and hour == 12:
            hour = 0

        dt = datetime(
            int(year),
            month,
            int(day),
            hour,
            minute
        )

        return dt.isoformat()   # 👈 listo para Mongo

    return {
        "transactionVariables": {
            "originAccount": result.get("Origen_Cuenta"),
            "destinationAccount": result.get("Destino_Cuenta"),
            "amount": parse_amount(result.get("Monto")),
            "currency": "PEN" if result.get("Monto") else None,
            "operationDate": parse_date(result.get("Fecha")),
            "operationNumber": result.get("Operacion")
        },
        "transactionType": "YAPEO" if result.get("Monto") else None,
        "confidence": {
            "amount": result.get("Monto_confianza", 0),
            "operationDate": result.get("Fecha_confianza", 0),
            "operationNumber": result.get("Operacion_confianza", 0)
        }
    }

    