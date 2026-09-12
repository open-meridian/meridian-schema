from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROLE_UNSPECIFIED: _ClassVar[Role]
    ROLE_OWNER: _ClassVar[Role]
    ROLE_ADMIN: _ClassVar[Role]
    ROLE_MEMBER: _ClassVar[Role]

class StaffCapability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STAFF_CAPABILITY_UNSPECIFIED: _ClassVar[StaffCapability]
    STAFF_CAPABILITY_ADMINISTER_SECURITY_MASTER: _ClassVar[StaffCapability]
    STAFF_CAPABILITY_RESTORE_ORGANISATION_OWNER: _ClassVar[StaffCapability]
    STAFF_CAPABILITY_ADMINISTER_STAFF: _ClassVar[StaffCapability]

class InvitationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVITATION_STATE_UNSPECIFIED: _ClassVar[InvitationState]
    INVITATION_STATE_PENDING: _ClassVar[InvitationState]
    INVITATION_STATE_ACCEPTED: _ClassVar[InvitationState]
    INVITATION_STATE_REVOKED: _ClassVar[InvitationState]
    INVITATION_STATE_EXPIRED: _ClassVar[InvitationState]

class InvitationDelivery(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVITATION_DELIVERY_UNSPECIFIED: _ClassVar[InvitationDelivery]
    INVITATION_DELIVERY_SENT: _ClassVar[InvitationDelivery]
    INVITATION_DELIVERY_PENDING: _ClassVar[InvitationDelivery]
    INVITATION_DELIVERY_FAILED: _ClassVar[InvitationDelivery]
ROLE_UNSPECIFIED: Role
ROLE_OWNER: Role
ROLE_ADMIN: Role
ROLE_MEMBER: Role
STAFF_CAPABILITY_UNSPECIFIED: StaffCapability
STAFF_CAPABILITY_ADMINISTER_SECURITY_MASTER: StaffCapability
STAFF_CAPABILITY_RESTORE_ORGANISATION_OWNER: StaffCapability
STAFF_CAPABILITY_ADMINISTER_STAFF: StaffCapability
INVITATION_STATE_UNSPECIFIED: InvitationState
INVITATION_STATE_PENDING: InvitationState
INVITATION_STATE_ACCEPTED: InvitationState
INVITATION_STATE_REVOKED: InvitationState
INVITATION_STATE_EXPIRED: InvitationState
INVITATION_DELIVERY_UNSPECIFIED: InvitationDelivery
INVITATION_DELIVERY_SENT: InvitationDelivery
INVITATION_DELIVERY_PENDING: InvitationDelivery
INVITATION_DELIVERY_FAILED: InvitationDelivery

class CreateOrganisationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class OrganisationRecord(_message.Message):
    __slots__ = ("organisation_id", "name", "created_at_ns")
    ORGANISATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_NS_FIELD_NUMBER: _ClassVar[int]
    organisation_id: str
    name: str
    created_at_ns: int
    def __init__(self, organisation_id: _Optional[str] = ..., name: _Optional[str] = ..., created_at_ns: _Optional[int] = ...) -> None: ...

class AddMemberRequest(_message.Message):
    __slots__ = ("organisation_id", "person_id", "role")
    ORGANISATION_ID_FIELD_NUMBER: _ClassVar[int]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    organisation_id: str
    person_id: str
    role: Role
    def __init__(self, organisation_id: _Optional[str] = ..., person_id: _Optional[str] = ..., role: _Optional[_Union[Role, str]] = ...) -> None: ...

class MembershipRecord(_message.Message):
    __slots__ = ("membership_id", "organisation_id", "person_id", "role", "created_at_ns", "granted_by_person_id")
    MEMBERSHIP_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANISATION_ID_FIELD_NUMBER: _ClassVar[int]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_NS_FIELD_NUMBER: _ClassVar[int]
    GRANTED_BY_PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    membership_id: str
    organisation_id: str
    person_id: str
    role: Role
    created_at_ns: int
    granted_by_person_id: str
    def __init__(self, membership_id: _Optional[str] = ..., organisation_id: _Optional[str] = ..., person_id: _Optional[str] = ..., role: _Optional[_Union[Role, str]] = ..., created_at_ns: _Optional[int] = ..., granted_by_person_id: _Optional[str] = ...) -> None: ...

class RemoveMemberRequest(_message.Message):
    __slots__ = ("organisation_id", "person_id")
    ORGANISATION_ID_FIELD_NUMBER: _ClassVar[int]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    organisation_id: str
    person_id: str
    def __init__(self, organisation_id: _Optional[str] = ..., person_id: _Optional[str] = ...) -> None: ...

class RemoveMemberReply(_message.Message):
    __slots__ = ("removed",)
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    removed: bool
    def __init__(self, removed: bool = ...) -> None: ...

class InviteMemberRequest(_message.Message):
    __slots__ = ("organisation_id", "email", "role")
    ORGANISATION_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    organisation_id: str
    email: str
    role: Role
    def __init__(self, organisation_id: _Optional[str] = ..., email: _Optional[str] = ..., role: _Optional[_Union[Role, str]] = ...) -> None: ...

class InvitationRecord(_message.Message):
    __slots__ = ("invitation_id", "organisation_id", "email", "role", "state", "delivery", "delivery_detail", "created_at_ns", "expires_at_ns", "invited_by_person_id")
    INVITATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANISATION_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_DETAIL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_NS_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_NS_FIELD_NUMBER: _ClassVar[int]
    INVITED_BY_PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    invitation_id: str
    organisation_id: str
    email: str
    role: Role
    state: InvitationState
    delivery: InvitationDelivery
    delivery_detail: str
    created_at_ns: int
    expires_at_ns: int
    invited_by_person_id: str
    def __init__(self, invitation_id: _Optional[str] = ..., organisation_id: _Optional[str] = ..., email: _Optional[str] = ..., role: _Optional[_Union[Role, str]] = ..., state: _Optional[_Union[InvitationState, str]] = ..., delivery: _Optional[_Union[InvitationDelivery, str]] = ..., delivery_detail: _Optional[str] = ..., created_at_ns: _Optional[int] = ..., expires_at_ns: _Optional[int] = ..., invited_by_person_id: _Optional[str] = ...) -> None: ...

class AcceptInvitationRequest(_message.Message):
    __slots__ = ("invitation_id",)
    INVITATION_ID_FIELD_NUMBER: _ClassVar[int]
    invitation_id: str
    def __init__(self, invitation_id: _Optional[str] = ...) -> None: ...

class RevokeInvitationRequest(_message.Message):
    __slots__ = ("organisation_id", "invitation_id")
    ORGANISATION_ID_FIELD_NUMBER: _ClassVar[int]
    INVITATION_ID_FIELD_NUMBER: _ClassVar[int]
    organisation_id: str
    invitation_id: str
    def __init__(self, organisation_id: _Optional[str] = ..., invitation_id: _Optional[str] = ...) -> None: ...

class RevokeInvitationReply(_message.Message):
    __slots__ = ("revoked",)
    REVOKED_FIELD_NUMBER: _ClassVar[int]
    revoked: bool
    def __init__(self, revoked: bool = ...) -> None: ...

class RegisterDeploymentRequest(_message.Message):
    __slots__ = ("organisation_id", "name")
    ORGANISATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    organisation_id: str
    name: str
    def __init__(self, organisation_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class DeploymentRecord(_message.Message):
    __slots__ = ("deployment_id", "organisation_id", "name", "created_at_ns", "last_seen_at_ns")
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANISATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_NS_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_NS_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    organisation_id: str
    name: str
    created_at_ns: int
    last_seen_at_ns: int
    def __init__(self, deployment_id: _Optional[str] = ..., organisation_id: _Optional[str] = ..., name: _Optional[str] = ..., created_at_ns: _Optional[int] = ..., last_seen_at_ns: _Optional[int] = ...) -> None: ...

class RegisterDeploymentKeyRequest(_message.Message):
    __slots__ = ("deployment_id", "public_key_pem", "label")
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_PEM_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    public_key_pem: str
    label: str
    def __init__(self, deployment_id: _Optional[str] = ..., public_key_pem: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class DeploymentKeyRecord(_message.Message):
    __slots__ = ("key_id", "deployment_id", "label", "fingerprint", "created_at_ns")
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_NS_FIELD_NUMBER: _ClassVar[int]
    key_id: str
    deployment_id: str
    label: str
    fingerprint: str
    created_at_ns: int
    def __init__(self, key_id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., label: _Optional[str] = ..., fingerprint: _Optional[str] = ..., created_at_ns: _Optional[int] = ...) -> None: ...

class RevokeDeploymentKeyRequest(_message.Message):
    __slots__ = ("deployment_id", "key_id")
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    key_id: str
    def __init__(self, deployment_id: _Optional[str] = ..., key_id: _Optional[str] = ...) -> None: ...

class RevokeDeploymentKeyReply(_message.Message):
    __slots__ = ("revoked",)
    REVOKED_FIELD_NUMBER: _ClassVar[int]
    revoked: bool
    def __init__(self, revoked: bool = ...) -> None: ...

class GrantStaffCapabilityRequest(_message.Message):
    __slots__ = ("person_id", "capability")
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    person_id: str
    capability: StaffCapability
    def __init__(self, person_id: _Optional[str] = ..., capability: _Optional[_Union[StaffCapability, str]] = ...) -> None: ...

class StaffGrantRecord(_message.Message):
    __slots__ = ("grant_id", "person_id", "capability", "created_at_ns", "granted_by_person_id")
    GRANT_ID_FIELD_NUMBER: _ClassVar[int]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_NS_FIELD_NUMBER: _ClassVar[int]
    GRANTED_BY_PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    grant_id: str
    person_id: str
    capability: StaffCapability
    created_at_ns: int
    granted_by_person_id: str
    def __init__(self, grant_id: _Optional[str] = ..., person_id: _Optional[str] = ..., capability: _Optional[_Union[StaffCapability, str]] = ..., created_at_ns: _Optional[int] = ..., granted_by_person_id: _Optional[str] = ...) -> None: ...

class RevokeStaffCapabilityRequest(_message.Message):
    __slots__ = ("grant_id",)
    GRANT_ID_FIELD_NUMBER: _ClassVar[int]
    grant_id: str
    def __init__(self, grant_id: _Optional[str] = ...) -> None: ...

class RevokeStaffCapabilityReply(_message.Message):
    __slots__ = ("revoked",)
    REVOKED_FIELD_NUMBER: _ClassVar[int]
    revoked: bool
    def __init__(self, revoked: bool = ...) -> None: ...

class RestoreOrganisationOwnerRequest(_message.Message):
    __slots__ = ("organisation_id", "person_id", "reason")
    ORGANISATION_ID_FIELD_NUMBER: _ClassVar[int]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    organisation_id: str
    person_id: str
    reason: str
    def __init__(self, organisation_id: _Optional[str] = ..., person_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...
