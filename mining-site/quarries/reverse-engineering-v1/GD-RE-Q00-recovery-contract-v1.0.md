# GD-RE-Q00 — Recovery Contract v1.0

## Mission

Recover GoDigital as though the maintainers inherited an orphaned software estate with no trusted documentation and needed to determine what the system is, why it exists, how it evolved and which parts are trustworthy enough to form a future baseline.

## Non-negotiable rule

> For recovery purposes, know nothing about GoDigital until the repositories provide evidence.

```text
MEMORY IS NOT EVIDENCE.
OLD INTENTION IS NOT EVIDENCE.
README CLAIMS ARE NOT AUTOMATIC TRUTH.
MAIN IS NOT AUTOMATIC TRUTH.
LATEST IS NOT AUTOMATICALLY CANONICAL.
CODE + CONFIGURATION + SCHEMAS + BRANCHES + COMMITS + CONTRACTS ARE EVIDENCE.
```

## Questions for the estate as a whole and each repository

- What is it?
- Why does it exist?
- What is it for?
- What technologies/frameworks/services does it actually use?
- What are its data/domain models?
- How does it communicate with other components?
- What evidence proves the claim?
- What generation does the implementation belong to?
- Is it scaffold, migration residue, experimental or product-specific?
- Is it implemented, runtime-verified or merely declared?
- What remains unknown?

## Recovery behavior

Do not redesign during recovery. Do not clean code to make the story prettier. Do not delete contradictions. Do not infer production use from code presence. Preserve versioned findings and explicitly mark uncertainty.

## Expected outcome

A sufficiently reliable archaeological baseline from which the owner can decide:

```text
WHAT GODIGITAL WAS
WHAT GODIGITAL CURRENTLY CONTAINS
WHAT THE CODE APPEARS TO BE TRYING TO BECOME
WHAT IS CANONICAL / LEGACY / EXPERIMENTAL / UNKNOWN
WHAT SHOULD BE PRESERVED
WHAT SHOULD BE DESIGNED NEXT
```
