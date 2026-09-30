# meridian-schema

The contract an [Open Meridian](https://open-meridian.com) plugin links: the
sidecar's gRPC service, the typed operations a plugin's roles may take, and the
metadata every bus message carries, with the code generation that turns them
into Rust and Python types.

A plugin talks only to its sidecar, and the sidecar builds every message that
goes onto the bus. So what a plugin needs from Open Meridian is small, and this
is all of it. The domain messages the runtime exchanges past the sidecar --
statements, holdings, instruments -- and the bus's envelope itself live in
[meridian-core](https://github.com/open-meridian/meridian-core), under its
licence.

Every message here is justified by a row in the project's function matrix,
which is in turn justified by a workflow step; [CLAUDE.md](CLAUDE.md) holds the
rules for changing one.

## Layout

    proto/meridian/v1/         the sidecar's service, and every message's metadata
    proto/meridian/plugin/v1/  the typed operations (PluginOperations)
    codegen/                   the Rust generator
    gen/rust/                  generated crate, vendored
    gen/python/                generated package, vendored

## Generating

    make codegen

Runs in a pinned container. The only prerequisite is Docker: a host `protoc` at
a different version produces subtly different output, so the host is never asked
to have one.

Generated files are vendored and reviewed like any other code, and are never
edited by hand. `make check-codegen` regenerates into a scratch directory and
fails on any difference, so a hand-edit is reverted by the gate rather than
surviving as a local divergence.

## Verification

    make ci-local

| Gate | Enforces |
|---|---|
| `contract-diff` | a commit changing a `.proto` or a guardrail declares it in a trailer |
| `check-codegen` | `gen/` matches a fresh generation |
| `check-pb-compiles` | the generated Rust crate builds |
| `check-pb-imports` | the generated Python package imports and round-trips |
| `ci-mirror-check` | every CI job is reproducible by `ci-local` |

`make install-hooks` makes `git push` run it first.

## Releasing

Nothing is published: a consumer takes this repository at a commit.
meridian-core names one in its `Cargo.toml`, and meridian-python vendors
`gen/python` at the revision its Makefile's `SCHEMA_REV` names, so a change
here reaches a plugin when those move. Within a version, changes only add.

## Consuming

Rust, as a git dependency on this repository at a commit (crate `meridian-pb`,
in `gen/rust`):

```rust
use meridian_pb::v1::sidecar_service_client::SidecarServiceClient;
use meridian_pb::plugin::v1::plugin_operations_client::PluginOperationsClient;
```

Python, with `gen/python` on the path:

```python
from meridian.v1 import sidecar_pb2, sidecar_pb2_grpc
from meridian.plugin.v1 import operations_pb2, operations_pb2_grpc
```

A plugin written in Python does not need even this: it uses the
[Python SDK](https://github.com/open-meridian/meridian-python), which links it
for them, and `meridian plugin new` starts one from its reference plugin. The
operations are documented at
[open-meridian.dev](https://open-meridian.dev/api/typed-operations/).

## Licence

Apache-2.0, so that a plugin vendor links it and keeps their plugin. See
[LICENSE](LICENSE) and [NOTICE](NOTICE).
