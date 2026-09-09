from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InstrumentLifecycleState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INSTRUMENT_LIFECYCLE_STATE_UNSPECIFIED: _ClassVar[InstrumentLifecycleState]
    INSTRUMENT_LIFECYCLE_STATE_DEFINE: _ClassVar[InstrumentLifecycleState]
    INSTRUMENT_LIFECYCLE_STATE_ACTIVE: _ClassVar[InstrumentLifecycleState]
    INSTRUMENT_LIFECYCLE_STATE_DECOMMISSIONED: _ClassVar[InstrumentLifecycleState]

class MissReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MISS_REASON_UNSPECIFIED: _ClassVar[MissReason]
    MISS_REASON_NOT_FOUND: _ClassVar[MissReason]
    MISS_REASON_AMBIGUOUS: _ClassVar[MissReason]
INSTRUMENT_LIFECYCLE_STATE_UNSPECIFIED: InstrumentLifecycleState
INSTRUMENT_LIFECYCLE_STATE_DEFINE: InstrumentLifecycleState
INSTRUMENT_LIFECYCLE_STATE_ACTIVE: InstrumentLifecycleState
INSTRUMENT_LIFECYCLE_STATE_DECOMMISSIONED: InstrumentLifecycleState
MISS_REASON_UNSPECIFIED: MissReason
MISS_REASON_NOT_FOUND: MissReason
MISS_REASON_AMBIGUOUS: MissReason

class Identifier(_message.Message):
    __slots__ = ("scheme", "value", "source")
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    scheme: str
    value: str
    source: str
    def __init__(self, scheme: _Optional[str] = ..., value: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...

class InstrumentRecord(_message.Message):
    __slots__ = ("instrument_id", "identifiers", "asset_class", "currency", "exchange_mic", "description", "lifecycle_state", "version", "valid_from_ns", "record_time_ns")
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    ASSET_CLASS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_MIC_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_STATE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VALID_FROM_NS_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_NS_FIELD_NUMBER: _ClassVar[int]
    instrument_id: str
    identifiers: _containers.RepeatedCompositeFieldContainer[Identifier]
    asset_class: str
    currency: str
    exchange_mic: str
    description: str
    lifecycle_state: InstrumentLifecycleState
    version: int
    valid_from_ns: int
    record_time_ns: int
    def __init__(self, instrument_id: _Optional[str] = ..., identifiers: _Optional[_Iterable[_Union[Identifier, _Mapping]]] = ..., asset_class: _Optional[str] = ..., currency: _Optional[str] = ..., exchange_mic: _Optional[str] = ..., description: _Optional[str] = ..., lifecycle_state: _Optional[_Union[InstrumentLifecycleState, str]] = ..., version: _Optional[int] = ..., valid_from_ns: _Optional[int] = ..., record_time_ns: _Optional[int] = ...) -> None: ...

class DefineInstrumentRequest(_message.Message):
    __slots__ = ("identifiers", "asset_class", "currency", "exchange_mic", "description", "valid_from_ns")
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    ASSET_CLASS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_MIC_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VALID_FROM_NS_FIELD_NUMBER: _ClassVar[int]
    identifiers: _containers.RepeatedCompositeFieldContainer[Identifier]
    asset_class: str
    currency: str
    exchange_mic: str
    description: str
    valid_from_ns: int
    def __init__(self, identifiers: _Optional[_Iterable[_Union[Identifier, _Mapping]]] = ..., asset_class: _Optional[str] = ..., currency: _Optional[str] = ..., exchange_mic: _Optional[str] = ..., description: _Optional[str] = ..., valid_from_ns: _Optional[int] = ...) -> None: ...

class AmendInstrumentRequest(_message.Message):
    __slots__ = ("instrument_id", "identifiers", "asset_class", "currency", "exchange_mic", "description", "valid_from_ns")
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    ASSET_CLASS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_MIC_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VALID_FROM_NS_FIELD_NUMBER: _ClassVar[int]
    instrument_id: str
    identifiers: _containers.RepeatedCompositeFieldContainer[Identifier]
    asset_class: str
    currency: str
    exchange_mic: str
    description: str
    valid_from_ns: int
    def __init__(self, instrument_id: _Optional[str] = ..., identifiers: _Optional[_Iterable[_Union[Identifier, _Mapping]]] = ..., asset_class: _Optional[str] = ..., currency: _Optional[str] = ..., exchange_mic: _Optional[str] = ..., description: _Optional[str] = ..., valid_from_ns: _Optional[int] = ...) -> None: ...

class DecommissionInstrumentRequest(_message.Message):
    __slots__ = ("instrument_id",)
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    instrument_id: str
    def __init__(self, instrument_id: _Optional[str] = ...) -> None: ...

class ReactivateInstrumentRequest(_message.Message):
    __slots__ = ("instrument_id",)
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    instrument_id: str
    def __init__(self, instrument_id: _Optional[str] = ...) -> None: ...

class ListInstrumentsRequest(_message.Message):
    __slots__ = ("lifecycle_state", "asset_class", "page_size", "cursor")
    LIFECYCLE_STATE_FIELD_NUMBER: _ClassVar[int]
    ASSET_CLASS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    lifecycle_state: InstrumentLifecycleState
    asset_class: str
    page_size: int
    cursor: str
    def __init__(self, lifecycle_state: _Optional[_Union[InstrumentLifecycleState, str]] = ..., asset_class: _Optional[str] = ..., page_size: _Optional[int] = ..., cursor: _Optional[str] = ...) -> None: ...

class ListInstrumentsReply(_message.Message):
    __slots__ = ("instruments", "next_cursor")
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[InstrumentRecord]
    next_cursor: str
    def __init__(self, instruments: _Optional[_Iterable[_Union[InstrumentRecord, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class ResolveIdentifierRequest(_message.Message):
    __slots__ = ("identifiers", "as_of_ns", "exchange_mic", "currency")
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    AS_OF_NS_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_MIC_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    identifiers: _containers.RepeatedCompositeFieldContainer[Identifier]
    as_of_ns: int
    exchange_mic: str
    currency: str
    def __init__(self, identifiers: _Optional[_Iterable[_Union[Identifier, _Mapping]]] = ..., as_of_ns: _Optional[int] = ..., exchange_mic: _Optional[str] = ..., currency: _Optional[str] = ...) -> None: ...

class ResolveIdentifierReply(_message.Message):
    __slots__ = ("found", "instrument_id", "miss_reason")
    FOUND_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    MISS_REASON_FIELD_NUMBER: _ClassVar[int]
    found: bool
    instrument_id: str
    miss_reason: MissReason
    def __init__(self, found: bool = ..., instrument_id: _Optional[str] = ..., miss_reason: _Optional[_Union[MissReason, str]] = ...) -> None: ...

class ResolveInstrumentRequest(_message.Message):
    __slots__ = ("instrument_id", "as_of_ns")
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    AS_OF_NS_FIELD_NUMBER: _ClassVar[int]
    instrument_id: str
    as_of_ns: int
    def __init__(self, instrument_id: _Optional[str] = ..., as_of_ns: _Optional[int] = ...) -> None: ...

class ResolveInstrumentReply(_message.Message):
    __slots__ = ("found", "instrument")
    FOUND_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    found: bool
    instrument: InstrumentRecord
    def __init__(self, found: bool = ..., instrument: _Optional[_Union[InstrumentRecord, _Mapping]] = ...) -> None: ...

class MissingInstrumentDetectedEvent(_message.Message):
    __slots__ = ("source", "asset_class", "identifiers", "as_of_ns", "publisher_instance_id", "reason", "observed_at_ns")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    ASSET_CLASS_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    AS_OF_NS_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_NS_FIELD_NUMBER: _ClassVar[int]
    source: str
    asset_class: str
    identifiers: _containers.RepeatedCompositeFieldContainer[Identifier]
    as_of_ns: int
    publisher_instance_id: str
    reason: MissReason
    observed_at_ns: int
    def __init__(self, source: _Optional[str] = ..., asset_class: _Optional[str] = ..., identifiers: _Optional[_Iterable[_Union[Identifier, _Mapping]]] = ..., as_of_ns: _Optional[int] = ..., publisher_instance_id: _Optional[str] = ..., reason: _Optional[_Union[MissReason, str]] = ..., observed_at_ns: _Optional[int] = ...) -> None: ...

class PullInstrumentReply(_message.Message):
    __slots__ = ("found", "instrument")
    FOUND_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    found: bool
    instrument: InstrumentRecord
    def __init__(self, found: bool = ..., instrument: _Optional[_Union[InstrumentRecord, _Mapping]] = ...) -> None: ...

class PullIdentifierReply(_message.Message):
    __slots__ = ("found", "instrument", "miss_reason")
    FOUND_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    MISS_REASON_FIELD_NUMBER: _ClassVar[int]
    found: bool
    instrument: InstrumentRecord
    miss_reason: MissReason
    def __init__(self, found: bool = ..., instrument: _Optional[_Union[InstrumentRecord, _Mapping]] = ..., miss_reason: _Optional[_Union[MissReason, str]] = ...) -> None: ...

class EscalateInstrumentRequest(_message.Message):
    __slots__ = ("source", "asset_class", "identifiers", "as_of_ns", "requesting_deployment_id")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    ASSET_CLASS_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    AS_OF_NS_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    source: str
    asset_class: str
    identifiers: _containers.RepeatedCompositeFieldContainer[Identifier]
    as_of_ns: int
    requesting_deployment_id: str
    def __init__(self, source: _Optional[str] = ..., asset_class: _Optional[str] = ..., identifiers: _Optional[_Iterable[_Union[Identifier, _Mapping]]] = ..., as_of_ns: _Optional[int] = ..., requesting_deployment_id: _Optional[str] = ...) -> None: ...

class EscalateInstrumentReply(_message.Message):
    __slots__ = ("instrument", "minted")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    MINTED_FIELD_NUMBER: _ClassVar[int]
    instrument: InstrumentRecord
    minted: bool
    def __init__(self, instrument: _Optional[_Union[InstrumentRecord, _Mapping]] = ..., minted: bool = ...) -> None: ...

class InstrumentAppliedEvent(_message.Message):
    __slots__ = ("instrument", "applied", "applied_at_ns")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    APPLIED_AT_NS_FIELD_NUMBER: _ClassVar[int]
    instrument: InstrumentRecord
    applied: bool
    applied_at_ns: int
    def __init__(self, instrument: _Optional[_Union[InstrumentRecord, _Mapping]] = ..., applied: bool = ..., applied_at_ns: _Optional[int] = ...) -> None: ...
