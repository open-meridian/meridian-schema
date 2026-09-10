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

## Review

Every pull request gets the same passes, in the same order, whether a person or
an agent wrote it. Uniformity is the point: a review that varies by author is a
review whose absence is invisible.

Mechanical checks do not belong in a review. Formatting, link targets, the
derivation chain, codegen staleness and the task ledger are enforced by
`make ci-local`. Attention spent on something a gate could catch is a missing
gate, and the fix is to write the gate.

Run the passes in order. Report at the first pass that finds an Important
finding; later passes still run, but the finding does not wait.

1. **Correctness.** Does it do what the spec says, and does it fail safely when
   it does not? State that survives a restart when it should not, or does not
   when it should. Error paths that swallow rather than surface. Concurrency
   assumptions that hold only under test timing. Arithmetic on money that is not
   exact decimal.
2. **Security.** Credentials in the diff, in a log line, in a fixture or in a
   compose file. Anything widening what an agent session may do without a human
   in the loop. New outbound network calls. Changes to `.claude/settings.json`,
   to hooks or to permissions are read line by line, every time.
3. **Contract compliance.** Does the change respect the derivation direction? A
   build-stage pull request touching a workflow, the matrix, the topic registry
   or a proto is a finding on its own, whether or not the change is a good one.
   The route is a contract-revision task, not an edit.
4. **Spec and plan alignment.** Does the diff match the plan it was approved
   against, and does that plan trace to a spec and an intent? A diff that
   quietly grew beyond its plan is a finding even when every added line is
   sound, because the scope was never reviewed.

**Important** findings are ship-blocking: data loss, a security exposure, a
wrong result, a broken contract, or scope that was never approved. State the
concrete failure, meaning the inputs, the state, and what goes wrong. A finding
without a failure scenario is a Nit wearing a costume.

**Nit** is everything else. Cap Nits at five and drop the weakest past that. A
review returning thirty Nits trains its reader to skim.

Excluded from review entirely: generated files, vendored dependencies, and
anything a CI gate already enforces.

People decide whether a finding merges or escalates, and whether the spec solves
the problem it claims to. Those stay with a named person.

> Canonical text: `meridian-design/REVIEW.md`. This copy exists because the
> reviewer runs in this repository and cannot read a private one. Drift between
> the two is a bug, not a variation.
