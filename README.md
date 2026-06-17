# loom

`loom` syncs global agent/harness configuration across machines through a Git-backed hub.

## Local use

```bash
loom doctor
loom sync
loom install-cli
loom install-hooks
loom install-shims
loom install-timer
```

## npx / bunx use

From this repository:

```bash
npx --yes . doctor
bunx --package file:$PWD loom doctor
```

From a Git remote after publishing/pushing this repo:

```bash
npx --yes git+ssh://git@github.com/<owner>/loom.git doctor
bunx --package git+ssh://git@github.com/<owner>/loom.git loom doctor
```

For durable cross-machine sync, install/clone the hub into a persistent directory, then run:

```bash
loom install-cli
loom install-hooks
loom install-shims
loom install-timer
```

`npx`/`bunx` one-shot temp execution is useful for bootstrap and diagnostics; the sync hub itself should live in a persistent Git checkout such as `~/Projects/neo/pub/loom`.
