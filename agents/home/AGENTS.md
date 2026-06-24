<claude-mem-context>
# Memory Context

# [neo] recent context, 2026-06-24 11:42am GMT+8

Legend: 🎯session 🔴bugfix 🟣feature 🔄refactor ✅change 🔵discovery ⚖️decision 🚨security_alert 🔐security_note
Format: ID TIME TYPE TITLE
Fetch details: get_observations([IDs]) | Search: mem-search skill

Stats: 3 obs (658t read) | 58,005t work | 99% savings

### Apr 20, 2026
S4 Greeting exchange - user said hello in Chinese (Apr 20, 4:50 PM)
69 4:53p 🔵 Claude Code agent system inventory and configuration
71 4:55p 🔵 Investigated alirezarezvani/claude-skills marketplace
72 4:58p ⚖️ 用户选择保持现状不继续

Access 58k tokens of past work via get_observations([IDs]) or mem-search skill.
</claude-mem-context>

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

<!-- GLOBAL-MEMORY:LOOM-AUTOSYNC:START -->
## Loom auto-sync requirement

When changing global agent memory, cross-agent instruction files, or loom-managed agent configuration on this machine, automatically run `loom sync` before reporting completion, then verify that local HEAD matches `origin/main`. Do not wait for the user to remind you unless the sync is blocked by credentials, network failure, or a conflicting remote state.
<!-- GLOBAL-MEMORY:LOOM-AUTOSYNC:END -->
