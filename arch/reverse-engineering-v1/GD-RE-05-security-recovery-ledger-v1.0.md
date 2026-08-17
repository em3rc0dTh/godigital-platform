# GoDigital — Security & Isolation Recovery Ledger v1.0

**Class:** Recovery finding ledger  
**Status:** OPEN — SECURITY NOT VERIFIED  
**Rule:** A finding here is evidence of code condition or architectural risk; it is not automatically proof of runtime exploitability.

## SEC-REC-001 — Hard-coded MongoDB credential material

**Repository:** `em3rc0dTh/GoDigitalBack`  
**Recovered generation:** `feat/workflow-engine`  
**Path:** `src/config/tenantDb.ts`  
**Observation:** the dynamic tenant DB connection code contains hard-coded MongoDB administrative Docker credential material in the source-level connection URI.  
**Interpretation:** high-severity credential/configuration debt. It must not survive an architecture/security freeze.  
**Runtime status:** unknown.  
**Required action before freeze:** move all credentials into appropriately scoped secret/configuration management; rotate any credential that may have been used outside an isolated local environment; verify access scope.

## SEC-REC-002 — TenantDetail fallback selection

**Repository:** `em3rc0dTh/GoDigitalBack`  
**Path:** `src/middleware/tenantContext.ts`  
**Observation:** middleware validates JWT tenant identity and verifies a requested TenantDetail belongs to the authenticated tenant. If no explicit tenant-detail header is supplied, it can fall back to the first item in `tenant.dbList`.  
**Positive evidence:** ownership validation exists and the requested managed entity is not blindly trusted.  
**Risk:** silent first-entity fallback may be unsuitable for money-affecting actions where entity selection must be explicit and auditable.  
**Required action:** classify which routes may use fallback safely; require explicit managed-entity context for financial mutations; test cross-entity denial.

## SEC-REC-003 — Auxiliary IMAP tenant trust boundary is weaker

**Repository:** `em3rc0dTh/imap`  
**Recovered generation:** `feat/tenant`  
**Path:** `app/api.py`  
**Observation:** the service can select tenant collections from supplied database context and exposes broad CORS configuration. The recovered service boundary does not show the same JWT + TenantDetail ownership verification found in the main backend.  
**Interpretation:** service-to-service tenant context is a material trust-boundary gap.  
**Required action:** establish one canonical authenticated service contract for managed-entity context; never trust arbitrary database-name/user headers as sufficient authority.

## SEC-REC-004 — Database-per-managed-entity is an isolation mechanism, not proof

**Repository:** `em3rc0dTh/GoDigitalBack`  
**Paths:** `src/config/tenantDb.ts`, `src/middleware/tenantContext.ts`  
**Observation:** a system database stores global tenancy metadata and `TenantDetail` determines dynamic connections to entity-specific Mongo databases.  
**Interpretation:** strong isolation intent and a concrete isolation mechanism exist.  
**Do not claim yet:** "secure tenant isolation is proven."  
**Required verification:** authentication, authorization, route-by-route tenant context, service-to-service calls, background jobs, IMAP acquisition, RECO, Odoo and Temporal paths must all be tested for cross-entity leakage or mutation.

## SEC-REC-005 — Release identity/security reproducibility gap

**Observation:** no exact release manifest binds the frontend, backend, IMAP, Agent, Temporal and deployment/integration SHAs into one version.  
**Security consequence:** vulnerability analysis and incident reproducibility are weakened when the exact executing code set cannot be named.  
**Required action:** introduce a version/release manifest before production claims.

## Security gate status

```text
TENANT ISOLATION INTENT              STRONG
BACKEND OWNERSHIP VALIDATION         IMPLEMENTED
SERVICE TRUST CONSISTENCY            OPEN
SECRET MANAGEMENT                    FAIL / OPEN
CROSS-TENANT NEGATIVE TESTS          NOT PERFORMED
RUNTIME SECURITY VERIFICATION        NOT PERFORMED
PRODUCTION SECURITY CLAIM            NOT ALLOWED
```

No DESIGN/ARCH freeze should treat the current isolation model as verified until these items are resolved or consciously accepted with evidence.
