# RTK - Rust Token Killer

**Usage**: Token-optimized CLI proxy (60-90% savings on dev operations)

## Meta Commands (always use rtk directly)

```bash
rtk gain              # Show token savings analytics
rtk gain --history    # Show command usage history with savings
rtk discover          # Analyze Claude Code history for missed opportunities
rtk proxy <cmd>       # Execute raw command without filtering (for debugging)
```

## Installation Verification

```bash
rtk --version         # Should show: rtk X.Y.Z
rtk gain              # Should work (not "command not found")
which rtk             # Verify correct binary
```

⚠️ **Name collision**: If `rtk gain` fails, you may have reachingforthejack/rtk (Rust Type Kit) installed instead.

## Hook-Based Usage

All other commands are automatically rewritten by the Claude Code hook.
Example: `git status` → `rtk git status` (transparent, 0 tokens overhead)

Refer to CLAUDE.md for full command reference.

<!-- GLOBAL-MEMORY:SPRING-BOOT-4-MIGRATION:START -->
## Spring Boot 4.x migration / upgrade

When the user mentions Spring Boot version migration, Spring Boot upgrade, or upgrading to Spring Boot 4.x, automatically consult and follow the official Spring Boot 4.0 Migration Guide:
https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide

Additional local preference for Jackson configuration during Spring Boot 4.x migrations:
- Prefer using/providing the `JsonMapper` bean first.
- Only add compatibility for an `ObjectMapper` bean when it is actually necessary for existing integrations or third-party code.
<!-- GLOBAL-MEMORY:SPRING-BOOT-4-MIGRATION:END -->
