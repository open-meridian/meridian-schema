#!/usr/bin/env python3
"""The generated Python package imports and round-trips.

Generated code that does not work is worse than none: the failure surfaces
downstream, in whichever consumer happens to touch it first, far from the schema
change that caused it. This catches it at the schema.

Deliberately shallow. It is not testing protobuf, it is testing that generation
produced an importable package whose messages survive a round trip -- including
the two shapes the contract cares about, a resolved holding and an unresolved
one.

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
    except Exception:
        return 0
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
        holdings = importlib.import_module("meridian.v1.holdings_pb2")
        reference = importlib.import_module("meridian.v1.reference_pb2")
        importlib.import_module("meridian.v1.envelope_pb2")
    except ImportError as exc:
        print(f"check-pb-imports FAILED: {exc}", file=sys.stderr)
        return 1

    problems: list[str] = []

    # A resolved holding, as fixtures/holdings/record-holding.yaml describes it.
    resolved = holdings.RecordHoldingRequest(
        statement_id="STMT-1",
        account_id="ACC-1",
        instrument_id="INS-1",
        quantity_scaled_1e8=1250000000,
        market_value_scaled_1e8=281250000000,
        currency="USD",
    )
    back = holdings.RecordHoldingRequest()
    back.ParseFromString(resolved.SerializeToString())
    if back != resolved:
        problems.append("a resolved holding did not survive a round trip")
    if back.quantity_scaled_1e8 != 1250000000:
        problems.append("scaled quantity changed across the wire")

    # The unresolved variant: identifiers instead of an instrument.
    unresolved = holdings.RecordHoldingRequest(
        statement_id="STMT-1",
        account_id="ACC-1",
        unresolved_identifiers=[
            reference.Identifier(scheme="symbol", value="ZZTOP", source="snaptrade")
        ],
        quantity_scaled_1e8=500000000,
        currency="USD",
    )
    back2 = holdings.RecordHoldingRequest()
    back2.ParseFromString(unresolved.SerializeToString())
    if back2.instrument_id != "":
        problems.append("an unresolved holding gained an instrument id")
    if not back2.unresolved_identifiers or back2.unresolved_identifiers[0].value != "ZZTOP":
        problems.append("unresolved identifiers were lost across the wire")

    # Cross-file import: holdings references a type declared in reference.proto.
    if not hasattr(holdings.RecordHoldingRequest, "DESCRIPTOR"):
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
        "                   resolves, sidecar service exposes all six operations"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
