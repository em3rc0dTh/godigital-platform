# GD-RE-Q01 — GoDigital Source Corpus Ledger v1.0

**Captured:** 2026-08-17  
**Purpose:** durable evidence anchors for Reverse Engineering v1.  
**Important:** a branch head is a recovery anchor, not proof of canonicality or deployment.

| Repository | Recovery branch/ref | Recovery SHA | Recovered role | Confidence |
|---|---|---|---|---|
| `em3rc0dTh/goDigital` | `feat/workflows` | `eda1005a72ef6353549b89cee5ee24537ab9273f` | latest recovered human control-plane/workflow generation | HIGH |
| `em3rc0dTh/GoDigitalBack` | `feat/workflow-engine` | `6d7957e5e4bdd1730e63f325b263f6159df8cfa5` | latest recovered central domain/workflow-integration generation | HIGH |
| `em3rc0dTh/imap` | `feat/tenant` | `853673f1d216b998ae579beb7b65a699b8e81c3a` | tenant-aware mailbox acquisition generation connected toward Agent/RECO | HIGH |
| `em3rc0dTh/agent` | `main` | `fb66cb348421c5b3df87166dac0ad13e0e109160` | extraction service with Transformer/Gemini/n8n implementations | HIGH |
| `em3rc0dTh/temporal` | `main` | `81cd0dac9aeb6793cf4aca002c1ceb29f934c30b` | recovered Temporal server/workflows repository containing GoDigital payment/cash workflows | HIGH for implementation; runtime unknown |
| `em3rc0dTh/godigital-platform` | `main` (pre-doc baseline) | `68358d4bca1fd1b80866cb03797fe45e4daeb05e` | historical integrated platform snapshot | HIGH |

## Architecture-bearing evidence examples

### GoDigitalBack — RECO

- `src/services/reco.ts`
  - accepts multiple observation source classes including Statement, WEB, API, GMAIL and IMAP;
  - maps source observations into a unified transaction model;
  - searches cross-source candidates;
  - preserves contributing source information.
- `src/models/tenant/TransactionRaw.ts`
  - supports multi-source evidence;
  - contains `linkedSources[]` with source/sourceId/externalId/rawData/extractedAt semantics.

Recovery implication: strong evidence for the invariant `OBSERVATION != ECONOMIC EVENT`.

### GoDigitalBack — tenancy

- `src/config/tenantDb.ts`
  - resolves dynamic managed-entity MongoDB connections from `TenantDetail`.
- `src/middleware/tenantContext.ts`
  - requires authenticated tenant context;
  - validates requested TenantDetail ownership;
  - currently permits fallback to the first managed entity when explicit selection is absent.

Recovery implication: database-per-managed-entity mechanism and isolation intent exist; secure isolation remains unverified.

### GoDigitalBack — Temporal bridge

- `src/services/temporal.ts`
  - feature flag `USE_TEMPORAL`;
  - configurable Temporal address with local default.
- payment request Temporal integration
  - starts workflow and sends approve/authorize/pay/reject signals;
  - is wrapped so orchestration failure does not break the normal endpoint.

Recovery implication: Temporal is implemented as optional durable orchestration/history companion, not yet proven sole domain authority.

### temporal — payment workflow

- `workflows/src/paymentRequest/workflow.ts`
  - approve/authorize/pay/reject signals;
  - queryable state;
  - multi-day approval/authorization/payment timeout semantics.
- `workflows/src/paymentRequest/activities.ts`
  - comments indicate Mongo/controller logic remains operational state owner in the recovered generation;
  - Temporal provides audit/durable workflow behavior.

Recovery implication: implementation alignment with backend is strong; runtime/prod remains unverified.

### agent

- `main.py`
  - FastAPI extraction API;
  - provider field with Transformer default and Gemini/n8n alternatives;
  - batch and health paths.

Recovery implication: multiple extractors behind a common service, but provider selection remains caller-visible.

### imap

- `app/api.py`
  - FastAPI/PyMongo/request-based acquisition/routing;
  - Agent extraction URL integration;
  - tenant database collection selection;
  - broad CORS configuration in recovered code.

Recovery implication: acquisition service is real; service-level trust boundary requires hardening/verification.

### godigital-platform

- root `docker-compose.yml`
- copied `goDigital/`, `GoDigitalBack/`, `agent/`, `imap/`

Recovery implication: historical evidence that these services were assembled together by late December 2025; not evidence that this repository represents the latest product generation.

## Evidence-confidence discipline

Use these independent fields in future ledgers:

```text
GENERATION: HISTORICAL / LATEST / UNKNOWN
PROVENANCE: GODIGITAL / SCAFFOLD / MIGRATION / EXTERNAL
IMPLEMENTATION: DECLARED / IMPLEMENTED / VERIFIED
RUNTIME: PROVEN / UNPROVEN / BROKEN / UNKNOWN
CANONICALITY: CANONICAL / CANDIDATE / SUPERSEDED / EXPERIMENT / UNKNOWN
DEPENDENCY STATUS: USED / REFERENCED / ORPHANED / UNKNOWN
EVIDENCE CONFIDENCE: HIGH / MEDIUM / LOW
```

This ledger must evolve by versioning, not by erasing earlier anchors.
