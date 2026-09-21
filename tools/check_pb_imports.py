#!/usr/bin/env python3
"""The generated Python package imports and round-trips.

Generated code that does not work is worse than none: the failure surfaces
downstream, in whichever consumer happens to touch it first, far from the schema
change that caused it. This catches it at the schema.

Deliberately shallow. It is not testing protobuf, it is testing that generation
produced an importable package whose messages survive a round trip -- the
message framing a plugin receives, and the registration and publish requests it
sends.

The domain messages are not here, and not because they were forgotten. They
moved to meridian-core on 2026-09-21: once no plugin can link a domain message,
they are the runtime's internal traffic past the sidecar, and core checks them.
This repository holds only what a plugin links.

Usage:  python3 tools/check_pb_imports.py [--gen gen/python]
Exit:   0 works, 1 does not, 2 the protobuf runtime is missing
"""

from __future__ import annotations

import argparse
import importlib
import pathlib
import sys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gen", default="gen/python")
    args = parser.parse_args()

    # Resolved rather than kept relative: the path is put on sys.path below,
    # and a relative entry there resolves against the working directory of
    # whoever invoked the script.
    gen = pathlib.Path(args.gen).resolve()
    if not gen.is_dir():
        print(f"check-pb-imports FAILED: no {args.gen}; run 'make codegen'", file=sys.stderr)
        return 1

    # Prepended, not appended: an installed package of the same name would
    # otherwise shadow the generated one and the check would pass against
    # code this repo did not produce.
    sys.path.insert(0, str(gen))

    try:
        import google.protobuf  # noqa: F401
    except ImportError:
        print(
            "check-pb-imports: the protobuf runtime is not installed.\n"
            "  python3 -m pip install protobuf",
            file=sys.stderr,
        )
        return 2

    try:
        envelope = importlib.import_module("meridian.v1.envelope_pb2")
        sidecar = importlib.import_module("meridian.v1.sidecar_pb2")
    except ImportError as exc:
        print(f"check-pb-imports FAILED: {exc}", file=sys.stderr)
        return 1

    problems: list[str] = []

    # The framing a plugin receives: metadata, a type name and opaque bytes.
    framed = envelope.Envelope(
        meta=envelope.MessageMeta(
            message_id="MSG-1",
            correlation_id="CORR-1",
            causation_id="MSG-0",
            publisher_instance_id="custody-1",
            topic="platform.street.command.record-holding",
            schema_version="v1",
            published_at_ns=1_757_376_000_000_000_000,
        ),
        payload_type="example.Payload",
        payload=b"\x00\x01opaque",
    )
    back = envelope.Envelope()
    back.ParseFromString(framed.SerializeToString())
    if back != framed:
        problems.append("an envelope did not survive a round trip")
    if back.payload != b"\x00\x01opaque":
        problems.append("payload bytes changed across the wire")

    # What a plugin sends first: the contract version it was built against.
    registered = sidecar.RegisterRequest(schema_version="v1")
    again = sidecar.RegisterRequest()
    again.ParseFromString(registered.SerializeToString())
    if again.schema_version != "v1":
        problems.append("a registration lost its contract version across the wire")

    # Cross-file import: sidecar.proto uses a type declared in envelope.proto.
    if not hasattr(sidecar.Delivery, "DESCRIPTOR"):
        problems.append("generated messages carry no descriptor")

    # The sidecar service. Generating only its messages would leave every
    # consumer hand-rolling the transport the contract already specifies, so the
    # stubs existing is the thing worth checking.
    try:
        grpc_mod = importlib.import_module("meridian.v1.sidecar_pb2_grpc")
    except ImportError as exc:
        print(f"check-pb-imports FAILED: sidecar service stubs missing: {exc}", file=sys.stderr)
        return 1

    for side in ("SidecarServiceStub", "SidecarServiceServicer"):
        if not hasattr(grpc_mod, side):
            problems.append(f"generated gRPC module has no {side}")

    # Every operation W4 declares must be callable. A method quietly missing
    # here is a workflow step with no way to perform it.
    #
    # Presence, never absence. The surface grows as workflows demand it, per
    # decisions/007, so an operation added here breaks nothing and one added to
    # the proto without this list noticing is caught by check-derivation, which
    # asks what workflow step it came from.
    expected = {"Register", "Publish", "Subscribe", "Call", "Heartbeat", "Leave"}
    servicer = getattr(grpc_mod, "SidecarServiceServicer", None)
    if servicer is not None:
        missing = sorted(m for m in expected if not hasattr(servicer, m))
        if missing:
            problems.append(f"sidecar service is missing operations: {', '.join(missing)}")

    for problem in problems:
        print(f"check-pb-imports FAILED: {problem}", file=sys.stderr)
    if problems:
        return 1

    print(
        "check-pb-imports OK: package imports, messages round-trip, cross-file import\n"
        "                   resolves, sidecar service exposes every operation W4 declares"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
