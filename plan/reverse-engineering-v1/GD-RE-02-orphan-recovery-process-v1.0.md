# GoDigital — STEP 0 · Orphan Recovery / Software Archaeology v1.0

**Purpose:** recover GoDigital from code without assuming remembered intent.  
**Status:** ACTIVE; NOT CLOSED.  
**Source repositories modified during recovery:** none.

## 1. Recovery contract

For recovery purposes, assume nothing about what GoDigital was intended to be.

```text
Memory is not evidence.
Old intention is not evidence.
README claims are not evidence by themselves.
main is not automatically truth.
Code + configuration + schemas + branches + commits + service contracts are evidence.
```

The recovery process admits each relevant repository into a corpus, examines branch topology and commit history, identifies architecture-bearing implementations, reconstructs system generations, traces cross-service contracts and records uncertainty explicitly.

## 2. Why branch archaeology was mandatory

The default branches do not contain the entire latest GoDigital story.

The latest coherent frontend/backend generation recovered is approximately:

```text
goDigital/feat/workflows              2026-03-24
GoDigitalBack/feat/workflow-engine    2026-03-24
imap/feat/tenant                      2026-02-24
agent/main                            2026-02-24
temporal/main                         2026-03-23
```

The critical rule is:

```text
LATEST RECOVERED DEVELOPMENT GENERATION
             !=
CANONICAL / DEPLOYED / WORKING / ADOPTED GENERATION
```

## 3. Archaeological layers

### Era 1 — November 2025: financial evidence extraction

The early IMAP/OCR work shows the first clear problem: turn messy financial evidence into structured observations/transactions.

### Era 2 — December 2025: backend migration + integrated snapshot

Frontend history contains explicit migration toward an Express backend. The `godigital-platform` repository then freezes a multi-service topology with Next.js, Express, MongoDB, IMAP and Agent.

### Era 3 — January to early March 2026: financial operations control domain

The backend expands into tenants, managed entities, accounts, business units, projects, providers/entities, purchase orders, payment requests, Gmail/IMAP acquisition, statements, extraction, RECO, Odoo and reconciliation.

### Era 4 — March 2026: workflow/orchestration generation

The frontend/backend add richer cash/expense/member/workspace/workflow experiences. Temporal integration appears and a standalone `temporal` repository is recovered.

## 4. First major product conclusion

The estate no longer looks like only an email parser or bank dashboard.

The recovered behavioral spine is:

```text
SOURCE REALITY
      ↓
CAPTURE
      ↓
RAW EVIDENCE
      ↓
NORMALIZATION / EXTRACTION
      ↓
RECONCILIATION
      ↓
FINANCIAL TRUTH
      ↓
OPERATIONAL CONTEXT
      ↓
HUMAN AUTHORITY
      ↓
MONEY MOVEMENT
      ↓
TRACEABILITY / SETTLEMENT
      ↓
ERP / EXTERNAL HANDOFF
```

This remains a **high-confidence recovery hypothesis**, not a product definition until owner review.

## 5. RECO as first-class recovered subsystem

RECO should not be treated as just another service method.

The strongest conceptual model is:

```text
GMAIL observation ───────┐
IMAP observation ────────┤
Statement observation ───┤
WEB observation ─────────┤
API observation ─────────┘
                         ↓
                       RECO
                         ↓
                Transaction_Raw
                         ↓
                  linkedSources[]
```

The system attempts to preserve the difference between source evidence and economic reality.

## 6. Cross-service integration vocabulary

A recovery claim must distinguish:

- `DECLARED` — dependency/configuration exists.
- `IMPLEMENTED` — a code path exists.
- `STATICALLY COMPATIBLE` — contracts/calls align in code.
- `RUNTIME VERIFIED` — actually executed successfully under controlled test.
- `PRODUCTION VERIFIED` — evidence from production operation.

Example: IMAP → Agent → RECO is strongly supported as a static/code-path chain. It is not yet a runtime-proven production chain.

The same discipline applies to Odoo, Gmail, Temporal and AI providers.

## 7. Durable provenance rule

Every serious recovery claim should eventually record:

```text
STATUS
SOURCE TYPE
REPOSITORY
BRANCH
COMMIT SHA
PATH
BLOB SHA (when captured)
OBSERVATION
INTERPRETATION
CONFIDENCE
CONTRADICTIONS
SUPERSEDES / SUPERSEDED BY
```

Do not persist temporary assistant/tool citation IDs as repository provenance.

## 8. Current corpus

The first recovery started with five repositories. A sixth relevant repository, `em3rc0dTh/temporal`, was later discovered and admitted into the corpus because its GoDigital workflow contracts align with backend integration code.

The corpus is now:

```text
em3rc0dTh/goDigital
em3rc0dTh/GoDigitalBack
em3rc0dTh/godigital-platform
em3rc0dTh/imap
em3rc0dTh/agent
em3rc0dTh/temporal
```

## 9. Recovery status

```text
SOURCE CORPUS IDENTIFIED              ✅ SIX REPOSITORIES
REPOSITORY / BRANCH ARCHAEOLOGY      ✅ STRONG
EVOLUTION ERAS                       ✅ STRONG
HISTORICAL PLATFORM TOPOLOGY         ✅ STRONG
LATEST DEVELOPMENT GENERATION        ✅ STRONG
CANONICAL GENERATION                 ◉ UNKNOWN
DOMAIN SPINE                         ✅ STRONG
TENANCY INTENT                       ✅ STRONG
RECO                                 ✅ STRONG
IMAP → AGENT → RECO STATIC CHAIN     ✅ STRONG
PAYMENT DOMAIN                       ✅ STRONG
CASH REQUEST DOMAIN                  ✅ STRONG
TEMPORAL IMPLEMENTATION              ✅ FOUND / IMPLEMENTED
TEMPORAL RUNTIME                     ⛔ UNVERIFIED
FULL FILE CLASSIFICATION             ◉ OPEN
CANONICAL / LEGACY MATRIX            ⛔ NEXT
SCAFFOLD / MIGRATION CLASSIFICATION  ⛔ NEXT
SERVICE CONTRACT MATRIX              ⛔ NEXT
SECURITY / SECRET AUDIT              ◉ STARTED, NOT CLOSED
TENANT ISOLATION VERIFICATION        ⛔
TEST / CI INVENTORY                  ⛔
DEPLOYMENT TRUTH                     ⛔
RUNTIME REPRODUCIBILITY              ⛔
DATA MODEL CANONICALIZATION          ⛔
OWNER PRODUCT-PURPOSE REVIEW         ⛔

DESIGN                               ⛔
ARCH FREEZE                          ⛔
BUILD                                ⛔ DO NOT TOUCH
```

## 10. Why recovery must close before design

Recovery answers:

```text
WHAT WAS THERE?
WHAT EXISTS?
WHAT CHANGED?
WHAT CAN WE PROVE?
WHAT DO WE NOT KNOW?
```

Design answers a different question:

```text
WHAT SHOULD GODIGITAL BECOME?
```

Those questions must not be collapsed. Otherwise historical residue, latest code and intentional future architecture become indistinguishable.

## 11. Correct next movement

The next core classification artifact is the canonical/legacy/experimental/unknown matrix, expanded across independent axes. That contract is defined in `GD-RE-04-next-gates-v1.0.md`.
