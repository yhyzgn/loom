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

## npx / bunx install

Install loom from this repository into the persistent hub directory `~/Projects/neo/pub/loom`:

```bash
npx --yes . install
bunx --package file:$PWD loom install
```

Install from a Git remote after pushing this repo:

```bash
npx --yes git+ssh://git@github.com/<owner>/loom.git install --repo git+ssh://git@github.com/<owner>/loom.git
bunx --package git+ssh://git@github.com/<owner>/loom.git loom install --repo git+ssh://git@github.com/<owner>/loom.git
```

The install command clones/copies loom to a persistent checkout, then runs `install-cli`, `install-hooks`, `install-shims`, `install-timer`, and `doctor`.
