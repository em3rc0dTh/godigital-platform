# GoDigital Ecosystem — Foundational Systems Architecture Analysis v1.0

**Class:** Recovered architecture analysis  
**Status:** APPROVED AS RECOVERY EVIDENCE — NOT CANONICAL ARCHITECTURE  
**Date:** 2026-08-17

## 0. Evidence boundary

This analysis reconstructs GoDigital from source code, configuration, schemas, branch history, service contracts and integration code rather than remembered product intent.

A repository README, package manifest, default branch or newest commit is evidence, but not automatic product truth.

The governing distinctions are:

```text
LATEST CODE != CANONICAL ARCHITECTURE
CANONICAL ARCHITECTURE != DEPLOYED VERSION
DEPLOYED VERSION != WORKING VERSION
WORKING VERSION != BUSINESS-ADOPTED VERSION
```

The latest coherent development generation presently recovered includes:

- `goDigital/feat/workflows` — branch head `eda1005a72ef6353549b89cee5ee24537ab9273f`.
- `GoDigitalBack/feat/workflow-engine` — branch head `6d7957e5e4bdd1730e63f325b263f6159df8cfa5`.
- `imap/feat/tenant` — branch head `853673f1d216b998ae579beb7b65a699b8e81c3a`.
- `agent/main` — branch head `fb66cb348421c5b3df87166dac0ad13e0e109160`.
- `temporal/main` — recovered repository containing GoDigital workflow packages; head at recovery time `81cd0dac9aeb6793cf4aca002c1ceb29f934c30b`.
- `godigital-platform/main` — historical integration snapshot; head before this documentation baseline `68358d4bca1fd1b80866cb03797fe45e4daeb05e`.

These are evidence anchors, not an assertion that they form one deployed release.

## 1. Ecosystem identity

Taken together, the repositories describe a **multi-tenant financial-operations control platform**.

The problem is not simply recording accounting entries. Financial truth originates in overlapping sources: Gmail, IMAP, web/bank observations, statements, purchase orders, payment requests, cash advances, receipts, invoices, approvals and ERP records.

GoDigital attempts to transform those fragments into controlled operational truth while retaining enough provenance to explain the result.

The architecture can be summarized as:

```text
FINANCIAL SOURCES
      ↓
CAPTURE
      ↓
RAW EVIDENCE
      ↓
EXTRACTION / NORMALIZATION
      ↓
RECO
      ↓
TRANSACTION TRUTH CANDIDATE
      ↓
BUSINESS CONTEXT
      ↓
HUMAN AUTHORITY
      ↓
PAYMENT / CASH WORKFLOWS
      ↓
EVIDENCE-BASED CLOSURE
      ↓
ERP / EXTERNAL SYSTEM
```

## 2. Evidence and authority are separate but convergent flows

### Evidence flow

`GoDigitalBack/src/services/reco.ts` accepts source classes including Statement, WEB, API, GMAIL and IMAP. It maps observations into a unified transaction model, searches for cross-source candidates and retains linked source data.

`GoDigitalBack/src/models/tenant/TransactionRaw.ts` supports multiple sources and `linkedSources[]`, preserving source identity, external identity, raw data and extraction time.

Architectural consequence:

```text
OBSERVATION != ECONOMIC EVENT
```

This is a core recovered invariant candidate.

### Authority flow

The domain model supplies context and permission to act: Tenant → TenantDetail/Managed Entity → Business Unit → Project → Entity/Provider → Purchase Order / Payment Request / Cash Request → human decision → execution → evidence → closure.

The frontend expresses user decisions. The backend must enforce identity, tenancy and domain transitions. Temporal can maintain durable history and waiting semantics for long-lived workflows.

The real center of GoDigital is the junction between evidence truth and authority truth.

## 3. Repository-by-repository architecture

### 3.1 `goDigital` — human control plane / BFF

The latest recovered frontend generation contains workspace selection, member management, business units, projects, entities/providers, accounts, transaction views, bank statements, purchase/payment/cash request experiences, expense evidence and workflow visualizations.

Why it exists: the domain core is not useful unless humans can assign context, review evidence, request money, approve/reject/authorize decisions and understand process state.

Important debt: the repository retains ShipFree scaffold ancestry, a broad dependency surface and overlapping local Next.js API/domain persistence from earlier generations. Package declaration is not equivalent to canonical architecture.

### 3.2 `GoDigitalBack` — domain authority and integration hub

The backend is the strongest architectural center of gravity. It contains identity/tenancy, members/roles/permissions, accounts, business units, projects, entities/providers, purchase orders, payment requests, cash requests, transaction evidence, reconciliation and external integrations.

Its tenancy implementation uses a system database plus dynamic per-`TenantDetail` Mongo connections. `src/middleware/tenantContext.ts` validates the authenticated tenant and verifies a requested TenantDetail belongs to that tenant before connecting.

The backend also owns the strongest recovered RECO implementation and integration paths toward Gmail, IMAP, Agent, Odoo and Temporal.

### 3.3 `imap` — mailbox acquisition adapter

The IMAP service is a specialized acquisition boundary. It connects to mailboxes, filters relevant financial communications, preserves/acquires content, sends unstructured evidence to the extraction service and routes structured observations downstream.

Why it exists: mailbox operations and email parsing have different operational/technology characteristics from the central TypeScript domain backend.

It should not own canonical financial truth. Its product role is to create evidence observations.

### 3.4 `agent` — extraction/intelligence adapter

`agent/main.py` exposes a FastAPI extraction service. The recovered API allows provider selection with Transformer as default and Gemini/n8n alternatives.

This should be described as **multiple extraction implementations behind one HTTP service contract**, not as perfectly provider-transparent behavior because provider choice is still caller-visible.

Its architectural role is interpretation of unstructured evidence, not authorization and not canonical transaction truth.

### 3.5 `temporal` — durable workflow orchestration

The recovered `temporal` repository contains TypeScript workflows for `paymentRequest`, `cashRequest` and related workflow infrastructure.

The Payment Request workflow exposes explicit signals such as approve, authorize, pay and reject, plus queryable state and multi-day timeout windows.

`GoDigitalBack/src/services/temporal.ts` activates integration through `USE_TEMPORAL=true`. Payment workflow integration code is wrapped so a Temporal failure does not break the normal business endpoint.

Activities currently document an important division: Mongo/controller logic remains responsible for operational state while Temporal records durable process history/signals. This is migration-friendly but creates future authority duplication if left unresolved.

An unresolved naming inconsistency remains: backend comments refer to a `temporal-suite` contract while the recovered repository is named `temporal`.

### 3.6 `godigital-platform` — historical integrated snapshot

This repository froze an older multi-service topology around late December 2025:

```text
Nginx
  ├── goDigital / Next.js
  └── GoDigitalBack / Express
          ↓
        MongoDB

Frontend / integration paths
  ├── IMAP
  └── Agent
```

Its value is archaeological. It proves that independent components were once assembled into one deployable topology. Later backend/frontend development continued elsewhere, so it must not be treated as present-day source of truth.

## 4. Historical evolution

### Era 1 — November 2025: IMAP/OCR extraction prototype

The earliest recovered problem is turning messy financial evidence into structured transactions.

### Era 2 — December 2025: Express migration and integrated platform

Frontend history shows migration branches from Next.js-owned backend logic toward Express. `godigital-platform` later captures an integrated snapshot of frontend/backend/IMAP/Agent/Mongo.

### Era 3 — January to early March 2026: financial operations platform

The backend expands into tenants, managed entities, accounts, projects, providers, purchase orders, payment requests, Gmail/IMAP acquisition, statements, AI extraction, RECO, Odoo and reconciliation.

### Era 4 — March 2026: workflow/orchestration generation

Frontend/backend branches introduce richer cash/expense workflows, member/workspace features and Temporal integration. The standalone `temporal` repository appears at the same moment.

This is the latest coherent recovered development generation, not yet a canonical release.

## 5. Architectural classification

GoDigital is not best described as a single monolith and should not be called a textbook microservice system.

The most accurate recovered description is:

> **A service-oriented, polyglot financial platform centered on a modular domain backend, with specialized acquisition/intelligence satellites, a frontend BFF/control plane, database-per-managed-entity tenancy, and optional durable workflow orchestration.**

`GoDigitalBack` behaves like a modular monolith at the domain level; IMAP, extraction and durable workflow execution are separated where distinct technical/runtime characteristics justify it.

## 6. Is it event-driven?

Only partially.

There are asynchronous/event mechanisms: Gmail watch/PubSub concepts, scheduled synchronization, Temporal signals/workers and timeouts. But much integration is synchronous HTTP, Mongo reads/writes or scheduled polling.

The accurate description is **request-driven and synchronization-driven at the integration core, with event/durable-workflow mechanisms where useful**.

## 7. Coherent technical decisions

Several choices reinforce the recovered thesis:

- Python for mailbox/data extraction/ML work.
- TypeScript for frontend, backend and workflow contracts.
- MongoDB for tenant-local domain data plus heterogeneous evidence.
- Temporal for long-running human processes.
- React Flow/workflow UI where process topology matters.
- Odoo kept behind an integration boundary.
- RECO acting as an anti-corruption/reconciliation boundary between observation sources and internal truth.

The code estate is not merely a collection of fashionable technologies; there is a consistent problem underneath it.

## 8. Architectural debt and unresolved ownership

### Persistence ownership
The frontend retains Drizzle/PostgreSQL-era domain models while the backend owns newer Mongoose/Mongo forms of overlapping concepts.

### API ownership
Next.js local domain APIs coexist with newer calls/proxies into Express.

### Workflow authority
Mongo/controller state and Temporal state coexist. The intended future authority model is not frozen.

### Repository provenance
ShipFree frontend ancestry and infrastructure/vendor material complicate identification of true GoDigital product DNA.

### Authorization semantics
Generic platform roles (`superadmin`, `admin`, `standard`) do not fully model contextual financial responsibilities such as project owner, reviewer or treasurer. These concepts must not be conflated.

### Internal trust
The main backend validates tenant ownership more strongly than some auxiliary services. Service-to-service tenant context is not yet consistently enforced.

### Release governance
No exact cross-repository SHA manifest currently constitutes an authoritative GoDigital release.

## 9. Architecture conclusion

GoDigital does not need to be reinvented before its recovered identity is reviewed. It needs to be **canonicalized**.

The leading invariants worth preserving are:

```text
Managed-entity isolation
Evidence before interpretation
Observation != financial event
Source provenance is never discarded
RECO as reconciliation boundary
Project/provider/account context around money
Human authority before controlled money movement
Explicit payment/cash lifecycles
Evidence-based closure
ERP as integration boundary
Durable orchestration for genuinely long-lived processes
```

Technologies can change. These recovered principles should require explicit design justification before removal.

**Recovered one-sentence identity:**

> GoDigital is a multi-tenant financial-operations control layer designed to observe fragmented financial reality, preserve its evidence, reconcile it into trustworthy transaction truth, connect that truth to organizational context and human authority, and carry controlled money processes through auditable closure and external-system handoff.
