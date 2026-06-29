<!-- FABLE5:QWEN:START -->
# Default Fable5 persona adapter

Load and apply `/home/neo/.agent-personas/claude-fable5/core.md` as a default response style/safety layer.

Do not copy the original Claude prompt literally. Preserve this host agent's identity, tools, policies, and local project instructions. Read `/home/neo/.agent-personas/claude-fable5/references/CLAUDE-FABLE-5.original.md` only when the user explicitly asks for source-level comparison, audit, quotation, or migration details.
<!-- FABLE5:QWEN:END -->

<!-- GLOBAL-MEMORY:SPRING-BOOT-4-MIGRATION:START -->
## Spring Boot 4.x migration / upgrade

When the user mentions Spring Boot version migration, Spring Boot upgrade, or upgrading to Spring Boot 4.x, automatically consult and follow the official Spring Boot 4.0 Migration Guide:
https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide

Additional local preference for Jackson configuration during Spring Boot 4.x migrations:
- Prefer using/providing the `JsonMapper` bean first.
- Only add compatibility for an `ObjectMapper` bean when it is actually necessary for existing integrations or third-party code.
<!-- GLOBAL-MEMORY:SPRING-BOOT-4-MIGRATION:END -->

<!-- GLOBAL-MEMORY:DATABASE-SQL-REDLINES:START -->
## Database / SQL red lines

Across all projects, database and SQL work must avoid non-standard, hard-to-maintain database features. These are red-line constraints unless the user explicitly overrides them for a specific existing legacy system:
- Do not create or rely on database views.
- Do not create or rely on database functions.
- Do not create or rely on stored procedures.
- Do not create or rely on SEQ/sequence objects.
- Prefer ordinary tables, indexes, constraints, migrations, and application/ORM-layer business logic that are easy to review and maintain.
<!-- GLOBAL-MEMORY:DATABASE-SQL-REDLINES:END -->

<!-- GLOBAL-MEMORY:JAVA-SPRING-ORM-SQL-REDLINES:START -->
## Java Spring Boot MyBatis / JPA SQL red lines

For Java Spring Boot projects using MyBatis, MyBatis-Plus, JPA, Hibernate, or similar ORM/data-mapper stacks, do not write or embed native/raw SQL directly in application code for business functionality. This is a red-line constraint.

Required approach:
- Implement business data access through ORM/data-mapper methods, repositories, query builders/wrappers, entity mappings, criteria/specification APIs, or framework-supported derived/query methods.
- Keep SQL out of Java strings/annotations/XML snippets for business logic unless the user explicitly authorizes an exception for a specific legacy compatibility case.
- If raw SQL already exists, prefer migrating it toward ORM-level APIs during related maintenance.
<!-- GLOBAL-MEMORY:JAVA-SPRING-ORM-SQL-REDLINES:END -->

<!-- GLOBAL-MEMORY:MODULE-ENTRY-FILE-CONVENTION:START -->
## Module entry / core file convention

For any codebase, files that act as module cores or public entry points (for example `mod.rs`, `lib.rs`, `registry.rs`, `dispatcher.rs`, route aggregators, SDK facades, and similar orchestration surfaces) must remain thin and library-like: define public contracts, wire submodules, expose APIs, and coordinate high-level flow only. Do not let these files accumulate all registration, routing, parsing, persistence, validation, or protocol-binding logic. Split implementation by nature, module, and feature responsibility into focused child modules before the entry file becomes a dumping ground. Prefer meaningful responsibility boundaries over mechanical line-count appeasement; source-size checks are only a backstop, not the architecture standard.
<!-- GLOBAL-MEMORY:MODULE-ENTRY-FILE-CONVENTION:END -->

<!-- GLOBAL-MEMORY:NO-WARNING-SUPPRESSION:START -->
## No warning-suppression bypasses

Across all projects, do not use or keep suppression attributes or lint-level downgrades to hide compiler, clippy, linter, typechecker, test, docs, or CI failures. This includes `#[allow(...)]`, `#![allow(...)]`, `#[expect(...)]`, broad allow lists, and equivalent tool-specific bypasses. Fix the root cause instead. Existing suppressions are technical debt that must be removed by fixing root causes; do not copy, expand, or leave them in touched code. If generated/third-party code appears to require an exception, record the blocker for explicit human review rather than adding the bypass silently.
<!-- GLOBAL-MEMORY:NO-WARNING-SUPPRESSION:END -->

<!-- GLOBAL-MEMORY:LOOM-AUTOSYNC:START -->
## Loom auto-sync requirement

When changing global agent memory, cross-agent instruction files, or loom-managed agent configuration on this machine, automatically run `loom sync` before reporting completion, then verify that local HEAD matches `origin/main`. Do not wait for the user to remind you unless the sync is blocked by credentials, network failure, or a conflicting remote state.
<!-- GLOBAL-MEMORY:LOOM-AUTOSYNC:END -->
