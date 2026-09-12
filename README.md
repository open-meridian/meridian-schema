# meridian-schema

Protobuf wire definitions for Meridian, and the code generation that turns them
into Rust and Python types.

Every message here is justified by a row in the function matrix, which is in
turn justified by a workflow step. See [CLAUDE.md](CLAUDE.md).

## Layout

    proto/meridian/v1/     the definitions
    codegen/               the Rust generator
    gen/rust/              generated crate, vendored
    gen/python/            generated package, vendored

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
| `check-codegen` | `gen/` matches a fresh generation |
| `check-pb-compiles` | the generated Rust crate builds |
| `check-pb-imports` | the generated Python package imports and round-trips |
| `ci-mirror-check` | every CI job is reproducible by `ci-local` |

## Consuming

Rust, as a path dependency on `gen/rust` (crate `meridian-pb`):

```rust
use meridian_pb::v1::RecordHoldingRequest;
```

Python, with `gen/python` on the path:

```python
from meridian.v1 import holdings_pb2
```

## Licence

Apache-2.0. Implement it, generate from it, ship what you build, keep what you
change.

Permissive on purpose, and the reasoning is worth a sentence because the runtime
next door is not. A wire contract exists to be implemented by other people, and
both generated packages are derived from these files, so a copyleft licence here
would reach every plugin that imports the generated types. A specification that
makes implementers nervous gets reimplemented badly, which is the outcome a
contract is written to prevent. Apache rather than MIT for the patent grant,
which is the clause that matters when somebody implements a protocol
commercially.

`meridian-core`, the deployment runtime, is AGPL. That is where the network
clause earns its place.

