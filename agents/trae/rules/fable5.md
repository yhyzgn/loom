<!-- FABLE5:TRAE:START -->
# Default Fable5 persona adapter

Load and apply `/home/neo/.agent-personas/claude-fable5/core.md` as a default response style/safety layer.

Do not copy the original Claude prompt literally. Preserve this host agent's identity, tools, policies, and local project instructions. Read `/home/neo/.agent-personas/claude-fable5/references/CLAUDE-FABLE-5.original.md` only when the user explicitly asks for source-level comparison, audit, quotation, or migration details.
<!-- FABLE5:TRAE:END -->

<!-- GLOBAL-MEMORY:SPRING-BOOT-4-MIGRATION:START -->
## Spring Boot 4.x migration / upgrade

When the user mentions Spring Boot version migration, Spring Boot upgrade, or upgrading to Spring Boot 4.x, automatically consult and follow the official Spring Boot 4.0 Migration Guide:
https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide

Additional local preference for Jackson configuration during Spring Boot 4.x migrations:
- Prefer using/providing the `JsonMapper` bean first.
- Only add compatibility for an `ObjectMapper` bean when it is actually necessary for existing integrations or third-party code.
<!-- GLOBAL-MEMORY:SPRING-BOOT-4-MIGRATION:END -->
