from meridian.v1 import reference_pb2 as _reference_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncStatusEvent(_message.Message):
    __slots__ = ("source", "account_id", "last_synced_at_ns", "connection_healthy", "status_detail", "observed_at_ns")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_SYNCED_AT_NS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_HEALTHY_FIELD_NUMBER: _ClassVar[int]
    STATUS_DETAIL_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_NS_FIELD_NUMBER: _ClassVar[int]
    source: str
    account_id: str
    last_synced_at_ns: int
    connection_healthy: bool
    status_detail: str
    observed_at_ns: int
    def __init__(self, source: _Optional[str] = ..., account_id: _Optional[str] = ..., last_synced_at_ns: _Optional[int] = ..., connection_healthy: bool = ..., status_detail: _Optional[str] = ..., observed_at_ns: _Optional[int] = ...) -> None: ...

class RecordHoldingsStatementRequest(_message.Message):
    __slots__ = ("source", "external_statement_id", "as_of_date", "read_at_ns")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    AS_OF_DATE_FIELD_NUMBER: _ClassVar[int]
    READ_AT_NS_FIELD_NUMBER: _ClassVar[int]
    source: str
    external_statement_id: str
    as_of_date: str
    read_at_ns: int
    def __init__(self, source: _Optional[str] = ..., external_statement_id: _Optional[str] = ..., as_of_date: _Optional[str] = ..., read_at_ns: _Optional[int] = ...) -> None: ...

class RecordHoldingsStatementReply(_message.Message):
    __slots__ = ("statement_id", "already_recorded")
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ALREADY_RECORDED_FIELD_NUMBER: _ClassVar[int]
    statement_id: str
    already_recorded: bool
    def __init__(self, statement_id: _Optional[str] = ..., already_recorded: bool = ...) -> None: ...

class RecordHoldingRequest(_message.Message):
    __slots__ = ("statement_id", "account_id", "instrument_id", "unresolved_identifiers", "quantity_scaled_1e8", "market_value_scaled_1e8", "currency")
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    UNRESOLVED_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_SCALED_1E8_FIELD_NUMBER: _ClassVar[int]
    MARKET_VALUE_SCALED_1E8_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    statement_id: str
    account_id: str
    instrument_id: str
    unresolved_identifiers: _containers.RepeatedCompositeFieldContainer[_reference_pb2.Identifier]
    quantity_scaled_1e8: int
    market_value_scaled_1e8: int
    currency: str
    def __init__(self, statement_id: _Optional[str] = ..., account_id: _Optional[str] = ..., instrument_id: _Optional[str] = ..., unresolved_identifiers: _Optional[_Iterable[_Union[_reference_pb2.Identifier, _Mapping]]] = ..., quantity_scaled_1e8: _Optional[int] = ..., market_value_scaled_1e8: _Optional[int] = ..., currency: _Optional[str] = ...) -> None: ...

class RecordHoldingReply(_message.Message):
    __slots__ = ("holding_id", "resolved")
    HOLDING_ID_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_FIELD_NUMBER: _ClassVar[int]
    holding_id: str
    resolved: bool
    def __init__(self, holding_id: _Optional[str] = ..., resolved: bool = ...) -> None: ...

class StatementRecordedEvent(_message.Message):
    __slots__ = ("statement_id", "source", "as_of_date", "rows_received", "rows_resolved", "rows_unresolved", "recorded_at_ns")
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    AS_OF_DATE_FIELD_NUMBER: _ClassVar[int]
    ROWS_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    ROWS_RESOLVED_FIELD_NUMBER: _ClassVar[int]
    ROWS_UNRESOLVED_FIELD_NUMBER: _ClassVar[int]
    RECORDED_AT_NS_FIELD_NUMBER: _ClassVar[int]
    statement_id: str
    source: str
    as_of_date: str
    rows_received: int
    rows_resolved: int
    rows_unresolved: int
    recorded_at_ns: int
    def __init__(self, statement_id: _Optional[str] = ..., source: _Optional[str] = ..., as_of_date: _Optional[str] = ..., rows_received: _Optional[int] = ..., rows_resolved: _Optional[int] = ..., rows_unresolved: _Optional[int] = ..., recorded_at_ns: _Optional[int] = ...) -> None: ...

class PositionUpdatedEvent(_message.Message):
    __slots__ = ("position", "statement_id", "previous_quantity_scaled_1e8")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_QUANTITY_SCALED_1E8_FIELD_NUMBER: _ClassVar[int]
    position: Position
    statement_id: str
    previous_quantity_scaled_1e8: int
    def __init__(self, position: _Optional[_Union[Position, _Mapping]] = ..., statement_id: _Optional[str] = ..., previous_quantity_scaled_1e8: _Optional[int] = ...) -> None: ...

class Position(_message.Message):
    __slots__ = ("account_id", "instrument_id", "quantity_scaled_1e8", "market_value_scaled_1e8", "currency", "last_statement_id", "as_of_date", "updated_at_ns")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_SCALED_1E8_FIELD_NUMBER: _ClassVar[int]
    MARKET_VALUE_SCALED_1E8_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    LAST_STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    AS_OF_DATE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_NS_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    instrument_id: str
    quantity_scaled_1e8: int
    market_value_scaled_1e8: int
    currency: str
    last_statement_id: str
    as_of_date: str
    updated_at_ns: int
    def __init__(self, account_id: _Optional[str] = ..., instrument_id: _Optional[str] = ..., quantity_scaled_1e8: _Optional[int] = ..., market_value_scaled_1e8: _Optional[int] = ..., currency: _Optional[str] = ..., last_statement_id: _Optional[str] = ..., as_of_date: _Optional[str] = ..., updated_at_ns: _Optional[int] = ...) -> None: ...

class ListPositionsRequest(_message.Message):
    __slots__ = ("account_id", "include_unresolved", "page_size", "cursor")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_UNRESOLVED_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    include_unresolved: bool
    page_size: int
    cursor: str
    def __init__(self, account_id: _Optional[str] = ..., include_unresolved: bool = ..., page_size: _Optional[int] = ..., cursor: _Optional[str] = ...) -> None: ...

class ListPositionsReply(_message.Message):
    __slots__ = ("positions", "unresolved", "next_cursor")
    POSITIONS_FIELD_NUMBER: _ClassVar[int]
    UNRESOLVED_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    positions: _containers.RepeatedCompositeFieldContainer[Position]
    unresolved: _containers.RepeatedCompositeFieldContainer[UnresolvedHolding]
    next_cursor: str
    def __init__(self, positions: _Optional[_Iterable[_Union[Position, _Mapping]]] = ..., unresolved: _Optional[_Iterable[_Union[UnresolvedHolding, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class UnresolvedHolding(_message.Message):
    __slots__ = ("holding_id", "account_id", "identifiers", "quantity_scaled_1e8", "market_value_scaled_1e8", "currency", "source", "as_of_date", "escalated")
    HOLDING_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_SCALED_1E8_FIELD_NUMBER: _ClassVar[int]
    MARKET_VALUE_SCALED_1E8_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    AS_OF_DATE_FIELD_NUMBER: _ClassVar[int]
    ESCALATED_FIELD_NUMBER: _ClassVar[int]
    holding_id: str
    account_id: str
    identifiers: _containers.RepeatedCompositeFieldContainer[_reference_pb2.Identifier]
    quantity_scaled_1e8: int
    market_value_scaled_1e8: int
    currency: str
    source: str
    as_of_date: str
    escalated: bool
    def __init__(self, holding_id: _Optional[str] = ..., account_id: _Optional[str] = ..., identifiers: _Optional[_Iterable[_Union[_reference_pb2.Identifier, _Mapping]]] = ..., quantity_scaled_1e8: _Optional[int] = ..., market_value_scaled_1e8: _Optional[int] = ..., currency: _Optional[str] = ..., source: _Optional[str] = ..., as_of_date: _Optional[str] = ..., escalated: bool = ...) -> None: ...
