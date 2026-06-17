# loom

`loom` syncs global agent/harness configuration across machines through a Git-backed hub.

## Install

From a persistent checkout, run:

```bash
loom install
```

`loom install` performs the local machine setup:

1. installs the `loom` CLI into the user executable path, default `~/.local/bin/loom`
2. installs harness hooks
3. installs command shims
4. installs the periodic timer
5. runs `loom doctor`

## Common commands

```bash
loom doctor
loom sync
loom install
loom install-cli
loom install-hooks
loom install-shims
loom install-timer
loom timer-status
```

## Persistent hub

The sync hub should live in a persistent Git checkout, for example:

```text
~/Projects/neo/pub/loom
```

Configure a private Git remote for cross-machine pull/push sync.
