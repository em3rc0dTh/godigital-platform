# GoDigital Reverse Engineering v1 — Next Gates

**Status:** REQUIRED BEFORE DESIGN  
**Primary next artifact:** `GD-REC-06 — Canonical / Legacy / Experimental / Unknown Matrix v1.0`

## 1. Why a single canonical/legacy label is insufficient

The largest archaeology risk is finding the newest code and declaring it architecture.

Every subsystem/component should therefore be classified independently across these axes:

### Generation
```text
HISTORICAL / LATEST / UNKNOWN
```

### Provenance
```text
GODIGITAL / SCAFFOLD / MIGRATION / EXTERNAL
```

### Implementation
```text
DECLARED / IMPLEMENTED / VERIFIED
```

### Runtime
```text
PROVEN / UNPROVEN / BROKEN / UNKNOWN
```

### Canonicality
```text
CANONICAL / CANDIDATE / SUPERSEDED / EXPERIMENT / UNKNOWN
```

### Dependency status
```text
USED / REFERENCED / ORPHANED / UNKNOWN
```

### Evidence confidence
```text
HIGH / MEDIUM / LOW
```

## 2. GD-REC-06 questions

Repository by repository and subsystem by subsystem, answer:

```text
WHAT EXISTS?
WHICH GENERATION DOES IT BELONG TO?
WHERE DID IT COME FROM?
IS IT ACTUALLY IMPLEMENTED?
IS IT USED OR ONLY DECLARED?
WHAT DEPENDS ON IT?
WHAT REPLACED IT?
IS IT CANONICAL?
IS IT MIGRATION RESIDUE?
IS IT SCAFFOLD/DONOR MATERIAL?
IS IT AN EXPERIMENT?
IS IT DEAD/ORPHANED?
DO WE HAVE ENOUGH EVIDENCE TO KNOW?
```

## 3. Components that require early classification

### goDigital
- ShipFree scaffold identity/dependencies.
- Next.js local API routes.
- Drizzle/PostgreSQL domain models.
- Express/BFF proxy paths.
- Current workflow UI surfaces.

### GoDigitalBack
- Mongoose/Mongo domain ownership.
- tenancy and managed-entity database model.
- RECO.
- Gmail/IMAP synchronization.
- Odoo integration.
- Temporal integration.
- generic RBAC vs contextual workflow responsibility.

### imap
- current tenant-aware FastAPI path.
- legacy OCR/classifier artifacts.
- local/sample PDFs and generated residue.
- database selection/trust contract.

### agent
- Transformer extraction.
- Gemini extraction.
- n8n extraction.
- caller-visible provider selection.

### temporal
- GoDigital TypeScript workflow package.
- large infrastructure/vendor/server material in repository.
- payment/cash workflow contracts.
- naming mismatch with `temporal-suite` comments.

### godigital-platform
- historical container topology.
- copied frontend/backend/imap/agent generations.
- use as evidence only, unless later runtime evidence says otherwise.

## 4. Gate sequence before DESIGN

```text
GD-REC-06 COMPONENT CLASSIFICATION
      ↓
SERVICE CONTRACT MATRIX
      ↓
EXTERNAL DEPENDENCY / SYSTEM-OF-RECORD LEDGER
      ↓
SECURITY / SECRET / ISOLATION AUDIT
      ↓
TEST + CI INVENTORY
      ↓
DEPLOYMENT / RUNTIME TRUTH
      ↓
CROSS-REPOSITORY RELEASE MANIFEST
      ↓
OWNER REVIEW OF PRODUCT PURPOSE
      ↓
RECOVERY GATE DECISION
      ↓
DESIGN
```

The exact order may overlap for evidence collection, but DESIGN must not silently begin while these questions are unresolved.

## 5. Immediate mandatory findings already promoted

- Hard-coded MongoDB credential material in backend tenant DB configuration.
- Explicit backend TenantDetail ownership validation exists, but silent first-managed-entity fallback needs review.
- IMAP service tenant context is weaker than the backend trust boundary.
- Temporal is implemented but optional and runtime-unverified.
- Mongo/controller workflow state and Temporal durable state coexist.
- No authoritative release manifest binds the six repository versions together.

## 6. Recovery gate

STEP 0 can close only when the team can distinguish, with evidence:

```text
HISTORY
CURRENT IMPLEMENTATION
INTENDED CANONICAL MODEL
VERIFIED RUNTIME
SECURITY BOUNDARY
EXTERNAL OWNERSHIP
UNKNOWN / UNPROVEN AREAS
```

Closing STEP 0 does not require every bug to be fixed. It requires the truth about the estate to be known well enough that DESIGN is not built on accidental history.
