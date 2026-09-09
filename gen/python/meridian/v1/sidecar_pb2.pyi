from meridian.v1 import envelope_pb2 as _envelope_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CallFailure(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CALL_FAILURE_UNSPECIFIED: _ClassVar[CallFailure]
    CALL_FAILURE_TIMEOUT: _ClassVar[CallFailure]
    CALL_FAILURE_REFUSED: _ClassVar[CallFailure]
    CALL_FAILURE_NO_HANDLER: _ClassVar[CallFailure]
    CALL_FAILURE_HANDLER_ERROR: _ClassVar[CallFailure]
CALL_FAILURE_UNSPECIFIED: CallFailure
CALL_FAILURE_TIMEOUT: CallFailure
CALL_FAILURE_REFUSED: CallFailure
CALL_FAILURE_NO_HANDLER: CallFailure
CALL_FAILURE_HANDLER_ERROR: CallFailure

class RegisterRequest(_message.Message):
    __slots__ = ("instance_id", "role", "tags", "schema_version")
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    role: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    schema_version: str
    def __init__(self, instance_id: _Optional[str] = ..., role: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., schema_version: _Optional[str] = ...) -> None: ...

class RegisterReply(_message.Message):
    __slots__ = ("admitted", "deployment_id", "refusal_reason", "publish_grants", "subscribe_grants")
    ADMITTED_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_REASON_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_GRANTS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_GRANTS_FIELD_NUMBER: _ClassVar[int]
    admitted: bool
    deployment_id: str
    refusal_reason: str
    publish_grants: _containers.RepeatedScalarFieldContainer[str]
    subscribe_grants: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, admitted: bool = ..., deployment_id: _Optional[str] = ..., refusal_reason: _Optional[str] = ..., publish_grants: _Optional[_Iterable[str]] = ..., subscribe_grants: _Optional[_Iterable[str]] = ...) -> None: ...

class PublishRequest(_message.Message):
    __slots__ = ("topic", "payload_type", "payload", "correlation_id", "causation_id")
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    CAUSATION_ID_FIELD_NUMBER: _ClassVar[int]
    topic: str
    payload_type: str
    payload: bytes
    correlation_id: str
    causation_id: str
    def __init__(self, topic: _Optional[str] = ..., payload_type: _Optional[str] = ..., payload: _Optional[bytes] = ..., correlation_id: _Optional[str] = ..., causation_id: _Optional[str] = ...) -> None: ...

class PublishReply(_message.Message):
    __slots__ = ("accepted", "message_id", "refusal_reason")
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_REASON_FIELD_NUMBER: _ClassVar[int]
    accepted: bool
    message_id: str
    refusal_reason: str
    def __init__(self, accepted: bool = ..., message_id: _Optional[str] = ..., refusal_reason: _Optional[str] = ...) -> None: ...

class SubscribeRequest(_message.Message):
    __slots__ = ("pattern",)
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    pattern: str
    def __init__(self, pattern: _Optional[str] = ...) -> None: ...

class Delivery(_message.Message):
    __slots__ = ("envelope",)
    ENVELOPE_FIELD_NUMBER: _ClassVar[int]
    envelope: _envelope_pb2.Envelope
    def __init__(self, envelope: _Optional[_Union[_envelope_pb2.Envelope, _Mapping]] = ...) -> None: ...

class CallRequest(_message.Message):
    __slots__ = ("topic", "payload_type", "payload", "correlation_id", "timeout_ms")
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    topic: str
    payload_type: str
    payload: bytes
    correlation_id: str
    timeout_ms: int
    def __init__(self, topic: _Optional[str] = ..., payload_type: _Optional[str] = ..., payload: _Optional[bytes] = ..., correlation_id: _Optional[str] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class CallReply(_message.Message):
    __slots__ = ("ok", "payload_type", "payload", "failure", "failure_detail")
    OK_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_DETAIL_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    payload_type: str
    payload: bytes
    failure: CallFailure
    failure_detail: str
    def __init__(self, ok: bool = ..., payload_type: _Optional[str] = ..., payload: _Optional[bytes] = ..., failure: _Optional[_Union[CallFailure, str]] = ..., failure_detail: _Optional[str] = ...) -> None: ...

class HeartbeatRequest(_message.Message):
    __slots__ = ("healthy", "detail")
    HEALTHY_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    healthy: bool
    detail: str
    def __init__(self, healthy: bool = ..., detail: _Optional[str] = ...) -> None: ...

class HeartbeatReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LeaveRequest(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class LeaveReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
