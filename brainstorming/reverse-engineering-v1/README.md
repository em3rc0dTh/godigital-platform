# GoDigital — Reverse Engineering v1

**Lifecycle position:** STEP 0 — Orphan Recovery / Software Archaeology  
**Date:** 2026-08-17  
**Status:** RECOVERY ACTIVE — OWNER REVIEW PENDING  
**Build:** FORBIDDEN IN THIS BASELINE

This folder is the entry point for the first formal reverse-engineering baseline of the GoDigital ecosystem.

The purpose of this version is not to redesign GoDigital. It is to recover what the code estate actually expresses, distinguish evidence from assumption, and produce a product/architecture hypothesis that the owner can review before any DESIGN, ARCH freeze, PLAN or BUILD work begins.

The governing rule is:

```text
MEMORY IS NOT EVIDENCE
README IS NOT AUTOMATICALLY TRUTH
MAIN IS NOT AUTOMATICALLY TRUTH
LATEST CODE IS NOT AUTOMATICALLY CANONICAL
DECLARED DEPENDENCY IS NOT AUTOMATICALLY IMPLEMENTED
IMPLEMENTED CODE IS NOT AUTOMATICALLY RUNNING
RUNNING CODE IS NOT AUTOMATICALLY BUSINESS-ADOPTED
```

The strongest recovered product hypothesis is:

> GoDigital is a multi-tenant Financial Operations Control Layer that transforms fragmented financial observations and operational evidence into trustworthy, contextualized and traceable financial truth, then combines that truth with explicit human authority to govern money-related business processes through auditable closure and external-system handoff.

This statement is **not yet owner-approved product truth**. It is the highest-confidence hypothesis recovered from six repositories.

## v1 document map

- `GD-RE-00-executive-master-v1.0.md` — executive purpose, ecosystem identity and owner-review gate.
- `../../arch/reverse-engineering-v1/GD-RE-01-foundational-systems-architecture-analysis-v1.0.md` — reconstructed ecosystem and repository roles.
- `../../plan/reverse-engineering-v1/GD-RE-02-orphan-recovery-process-v1.0.md` — recovery method, historical eras and evidence discipline.
- `../../test/reverse-engineering-v1/GD-RE-03-jett-audit-verdict-v1.0.md` — audit corrections and current recovery verdict.
- `../../plan/reverse-engineering-v1/GD-RE-04-next-gates-v1.0.md` — the gates required before DESIGN.
- `../../arch/reverse-engineering-v1/GD-RE-05-security-recovery-ledger-v1.0.md` — security/isolation findings discovered during archaeology.
- `../../mining-site/quarries/reverse-engineering-v1/GD-RE-Q01-source-corpus-ledger-v1.0.md` — durable repository/branch/SHA evidence ledger.

## Owner review boundary

The owner must explicitly decide whether the recovered goal, product identity and invariants describe the GoDigital that should continue forward.

Until that review happens:

```text
RECOVERY          ACTIVE
BRAINSTORMING     RECOVERED HYPOTHESIS ONLY
DESIGN            NOT STARTED
ARCH FREEZE        NOT STARTED
PLAN               RECOVERY PLAN ONLY
BUILD              NOT STARTED
RUNTIME TEST       NOT STARTED
```
