# GoDigital Ecosystem — Executive Master Document v1.0

**Document class:** Executive Recovery Baseline  
**Lifecycle:** STEP 0 — Software Archaeology / Reverse Engineering  
**Status:** PENDING OWNER REVIEW  
**Date:** 2026-08-17

## 1. Decision boundary

This document does not declare the final product definition of GoDigital. It records the strongest product and architectural thesis recoverable from the source estate.

```text
RECOVERED INTENT
      !=
OWNER-APPROVED PRODUCT PURPOSE
      !=
CANONICAL ARCHITECTURE
      !=
WORKING RUNTIME
      !=
PRODUCTION SYSTEM
      !=
BUSINESS-ADOPTED SYSTEM
```

The main goal below therefore has the status **HIGH-CONFIDENCE RECOVERED MAIN-GOAL HYPOTHESIS — PENDING OWNER CONFIRMATION**.

## 2. Recovered main goal

> **GoDigital exists to transform fragmented financial observations and operational evidence into trustworthy, contextualized and traceable financial truth, and then use that truth together with explicit human authority to control money-related business processes through auditable closure and external-system handoff.**

Compactly:

```text
OBSERVE REALITY
      ↓
PRESERVE EVIDENCE
      ↓
INTERPRET
      ↓
NORMALIZE
      ↓
RECONCILE
      ↓
ESTABLISH FINANCIAL TRUTH
      ↓
ADD BUSINESS CONTEXT
      ↓
APPLY HUMAN AUTHORITY
      ↓
CONTROL FINANCIAL PROCESS
      ↓
PROVE OUTCOME
      ↓
CLOSE / RECONCILE
      ↓
ERP / EXTERNAL HANDOFF
```

## 3. What GoDigital is

The strongest recovered product identity is:

> **GoDigital is a multi-tenant Financial Operations Control Layer.**

It sits between messy financial reality and formal business/financial systems.

It is not adequately described as only an ERP, accounting application, bank aggregator, dashboard, expense tracker, email parser, OCR tool, AI application or workflow engine. Those are capabilities or integrations inside the estate; none describes the whole.

GoDigital attempts to establish the relationship between:

```text
WHAT WAS OBSERVED
WHAT ECONOMIC EVENT PROBABLY OCCURRED
WHY THAT EVENT EXISTS
WHICH ORGANIZATIONAL CONTEXT IT BELONGS TO
WHO WAS ALLOWED TO AUTHORIZE IT
WHAT MONEY PROCESS FOLLOWED
WHAT EVIDENCE PROVES THE RESULT
```

## 4. Why GoDigital exists

Financial reality is fragmented. A bank notification can show movement without business intent. A purchase order can show intent without payment. An approval can show authority without execution. A receipt can show expenditure without authorization. A statement can be authoritative evidence while arriving later than email/web observations.

The system exists to connect these fragments without destroying their provenance.

The code estate repeatedly attacks this problem through multi-source acquisition, evidence preservation, normalization, cross-source matching, project/provider/account context, controlled payment/cash workflows, human decisions and ERP integration.

## 5. The two fundamental flows

### Evidence flow — what actually happened?

```text
Gmail / IMAP / Statement / Web / API
                ↓
          RAW OBSERVATION
                ↓
       Agent / parser / extractor
                ↓
      NORMALIZED OBSERVATION
                ↓
              RECO
                ↓
      CROSS-SOURCE MATCHING
                ↓
       Transaction_Raw
          + linkedSources[]
                ↓
     CANDIDATE FINANCIAL TRUTH
```

One of the strongest recovered principles is:

```text
SOURCE RECORD != ECONOMIC EVENT
```

Multiple observations may describe the same financial event. The RECO subsystem and `Transaction_Raw.linkedSources[]` preserve this distinction.

### Authority flow — what should have happened, and who was allowed to make it happen?

```text
TENANT / WORKSPACE
      ↓
MANAGED ENTITY
      ↓
BUSINESS UNIT
      ↓
PROJECT
      ↓
ENTITY / PROVIDER
      ↓
PURCHASE ORDER
      ↓
PAYMENT REQUEST or CASH REQUEST
      ↓
HUMAN DECISION
      ↓
APPROVAL
      ↓
AUTHORIZATION
      ↓
PAYMENT / EXPENDITURE
      ↓
EVIDENCE
      ↓
SETTLEMENT / RECONCILIATION
      ↓
CLOSURE
```

The architectural center of GoDigital is where evidence truth and authority truth meet.

## 6. Recovered ecosystem

Six repositories form the current recovery corpus:

| Repository | Executive responsibility | Recovery interpretation |
|---|---|---|
| `em3rc0dTh/goDigital` | Human control plane / BFF | Latest product-facing generation mixed with scaffold/migration residue |
| `em3rc0dTh/GoDigitalBack` | Domain authority and integration hub | Current architectural center of gravity |
| `em3rc0dTh/imap` | Mailbox financial-evidence acquisition | Specialized acquisition adapter |
| `em3rc0dTh/agent` | Unstructured evidence interpretation | Specialized extraction/intelligence service |
| `em3rc0dTh/temporal` | Durable long-running workflow orchestration | Implemented, optional, runtime unverified |
| `em3rc0dTh/godigital-platform` | Historical integrated snapshot | Archaeological deployment/integration evidence |

The ecosystem is best characterized as a **central-domain platform with specialized satellite services**, not as either a textbook monolith or a mature independent microservice fleet.

## 7. Repository missions

### goDigital

Human-facing financial operations surface. It presents workspace/entity selection, projects, business units, accounts, entities/providers, purchase orders, payment/cash workflows, evidence and workflow views. It is where humans express authority-bearing decisions; the backend must remain the enforcement boundary.

### GoDigitalBack

The main domain/API/integration core. It owns the strongest recovered models for identity, tenancy, managed-entity databases, accounts, business context, procurement, payment/cash flows, transactions, reconciliation and integrations.

### imap

Acquires financial evidence from mailboxes. Its responsibility is capture and routing, not ownership of financial truth.

### agent

Turns messy HTML/text into structured financial variables. Multiple implementations exist behind one extraction API, including Transformer, Gemini and n8n paths. AI is therefore an interpretation mechanism, not financial authority.

### temporal

Adds durable waiting, signaling, timeouts and history to long-running human workflows. Payment Request has explicit approve/authorize/pay/reject signals. The backend integration is feature-flagged and deliberately non-fatal, so Temporal is not yet proven as sole state authority.

### godigital-platform

A late-2025 integrated time capsule containing frontend, backend, IMAP, Agent, MongoDB and Docker/Nginx topology. It proves an earlier integration shape but is not current source of truth.

## 8. Recovered domain spine

```text
Tenant
  ↓
TenantDetail / Managed Entity
  ├── Members
  ├── Accounts
  └── Business Units
          ↓
        Project
          ↓
     Entity / Provider
          ↓
     Purchase Order
          ↓
     Payment Request

Managed Entity
      ↓
  Cash Request
      ↓
Expense Evidence
      ↓
Settlement / Refund / Reimbursement

Financial Sources
      ↓
Transaction evidence
      ↓
RECO / reconciliation
```

## 9. Candidate invariants

These concepts appear stronger than any particular implementation and should not be removed without explicit architectural justification:

1. Evidence before interpretation.
2. Observation is not automatically a financial event.
3. Source provenance is preserved.
4. RECO separates observation sources from financial truth.
5. Financial events require organizational context.
6. Money-affecting processes require explicit authority.
7. Platform RBAC and contextual workflow responsibility are different concepts.
8. Payment and cash processes have explicit lifecycles.
9. Financial processes close using evidence, not only status flags.
10. Managed entities require intentional isolation boundaries.
11. AI interprets evidence; AI does not become financial authority.
12. ERP remains an integration boundary.
13. Long-lived human processes deserve durable history/orchestration.
14. Traceability must survive the full journey.

## 10. Main-goal achievement gates

GoDigital should not be declared successful merely because services start. It achieves the recovered main goal only if the complete business chain can be proven.

### Gate 1 — Capture reality
Can real evidence enter from actual external sources without manually rewriting the source facts?

### Gate 2 — Preserve evidence
Can the system answer where a fact came from, what the source contained and when it was observed?

### Gate 3 — Reconcile reality
Can multiple observations representing one event become one candidate financial truth while preserving provenance?

### Gate 4 — Add organizational context
Can a financial event be associated to the correct managed entity, account, business unit, project, provider and procurement context?

### Gate 5 — Apply human authority
Can the system prove who requested, approved, authorized, rejected, paid, reviewed or closed a money-related process?

### Gate 6 — Govern money processes
Can payment, cash/expense and related processes travel through explicit constrained lifecycles?

### Gate 7 — Prove the outcome
Does a terminal state such as `PAID` correspond to evidence that the action actually happened rather than only a status mutation?

### Gate 8 — Close the financial loop
Can advances/expenses resolve into exact settlement, reimbursement required, refund/return required or another financially explainable closure?

### Gate 9 — Preserve traceability
Can an auditor reconstruct source → interpretation → reconciliation → context → request → authority → execution → evidence → closure?

### Gate 10 — External handoff
Can the resulting operational truth be transferred to Odoo/ERP or another system without losing GoDigital context?

### Gate 11 — Tenant safety
Can one managed entity ever read or mutate another managed entity's financial data through any supported path? Required answer: no.

### Gate 12 — Runtime coherence
Can one exact manifest of frontend/backend/imap/agent/temporal/integration SHAs be run and proven together?

## 11. Current executive assessment

```text
PRODUCT THESIS                 STRONG
EVIDENCE ACQUISITION           STRONG IMPLEMENTATION EVIDENCE
EVIDENCE PRESERVATION          STRONG
RECONCILIATION                 STRONG
BUSINESS CONTEXT MODEL         STRONG
HUMAN WORKFLOW MODEL           STRONG
PAYMENT/CASH MODEL             STRONG
TEMPORAL IMPLEMENTATION        IMPLEMENTED / OPTIONAL
ERP BOUNDARY                   IMPLEMENTED / UNVERIFIED
TENANT ISOLATION INTENT        STRONG
TENANT SECURITY PROOF          OPEN
RUNTIME INTEGRATION            OPEN
PRODUCTION OPERATION           UNKNOWN
BUSINESS ADOPTION              UNKNOWN
CANONICAL RELEASE              NOT DEFINED
MAIN GOAL ACHIEVEMENT          NOT YET PROVEN
```

## 12. Principal obstacles before success can be claimed

### Generational incoherence
Several implementation generations coexist: Next.js APIs and Express APIs; Drizzle/PostgreSQL models and Mongoose/Mongo models; controller/Mongo workflow state and Temporal workflow state.

### Scaffold/provenance contamination
The frontend retains ShipFree ancestry. Dependency presence must not be promoted into GoDigital architecture without evidence.

### Workflow authority duplication
Mongo/controller state and Temporal workflow state coexist intentionally but the authoritative future model is unresolved.

### Security debt
The recovery found unresolved tenant/service trust issues and hard-coded credential material. Security verification is a mandatory gate before architecture freeze.

### Release governance
No artifact currently defines which cross-repository collection of SHAs constitutes GoDigital version X.

## 13. Owner review contract

The owner should now explicitly decide:

- Is the recovered main goal correct, correct with changes, or wrong?
- Is **Financial Operations Control Layer** the right identity?
- Is `OBSERVATION != FINANCIAL EVENT` a permanent principle?
- Is RECO a core capability or an experiment?
- Is the operational scope of PO / Payment Request / Cash Request / Expenses / Reimbursement / Refund correct?
- Should Odoo/ERP remain an external boundary rather than become the center of GoDigital?
- Must money-related transitions preserve explicit human authority?
- Is multi-managed-entity operation fundamental?

## 14. Executive success definition

GoDigital should eventually be considered successful only when a real case can travel through:

```text
REAL FINANCIAL ACTIVITY
      ↓
REAL SOURCE OBSERVED
      ↓
RAW EVIDENCE PRESERVED
      ↓
INTERPRETED / NORMALIZED
      ↓
RECONCILED
      ↓
FINANCIAL EVENT ESTABLISHED
      ↓
CORRECT MANAGED ENTITY
      ↓
CORRECT BUSINESS CONTEXT
      ↓
AUTHORIZED HUMAN PROCESS
      ↓
CONTROLLED MONEY ACTION
      ↓
RESULTING EVIDENCE
      ↓
SETTLEMENT / RECONCILIATION
      ↓
AUDITABLE CLOSURE
      ↓
ERP / EXTERNAL HANDOFF
```

and the system can explain what happened, why, to which entity, for which purpose, who requested/approved/authorized it, whether money actually moved, what evidence proves it, whether multiple observations represent one event, whether it settled, and what was handed to the ERP.

## 15. Master verdict

The recovered estate does not look like a failed idea searching for a purpose. It looks like a coherent architectural thesis implemented across several generations without yet reaching canonical and operational maturity.

> **GoDigital connects financial evidence, operational context and human authority so organizations can transform fragmented financial reality into controlled, traceable and auditable financial operations.**

The code strongly demonstrates the intent. The architecture substantially supports it. What remains unproven is whether one canonical, secure and reproducible version of the ecosystem can complete the journey at runtime and in real business operation.

The next question is therefore not "what code exists?" but **"is this the GoDigital we intended to build?"**
