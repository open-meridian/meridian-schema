# meridian-schema

Protobuf wire definitions and the code generation that turns them into Rust and
Python types.

## The rule that governs this repo

**A message here exists because a matrix row cites it, and that row exists
because a workflow step justifies it.** Nothing is added to serve an
implementation's convenience.

`make check-derivation` fails the build on any message no matrix row cites. It
is strict, always, and is never run in report-only mode. A gate that reports
without failing teaches its readers to ignore it.

**Never write a comment saying a message mirrors an implementation type.** If a
message needs that comment to be understood, it was derived backwards: the
implementation came first and the schema was fitted to it. The derivation gate
greps for the pattern and fails.

## Placement

Wire definitions only. No service implementations, no helpers, no test
harnesses. Generated output is vendored into a dedicated crate or module so it
compiles once and caches rather than relinking into every consumer.

## Changing a message

A schema change is a coordinated event, not a local one. A new message means a
new tag here, then a pinned update in every consumer, landed as one arc. Do not
land a schema change and leave consumers to discover it.

Within a major version, changes are additive. Field numbers are never reused;
retire them with `reserved`.

## Verification

    make ci-local
