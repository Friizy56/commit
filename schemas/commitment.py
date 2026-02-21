from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class CommitmentStatusSchema(str, Enum):
    """Commitment status enum"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    OVERDUE = "overdue"
    CANCELLED = "cancelled"


class CommitmentTypeSchema(str, Enum):
    """Commitment type enum"""
    INVOICE = "invoice"
    REORDER = "reorder"
    PAYMENT = "payment"
    FOLLOWUP = "followup"
    DELIVERY = "delivery"
    REMINDER = "reminder"
    OTHER = "other"


class CommitmentBase(BaseModel):
    """Base commitment schema"""
    action: str
    description: Optional[str] = None
    commitment_type: CommitmentTypeSchema = CommitmentTypeSchema.OTHER
    deadline: datetime
    party_name: Optional[str] = None
    party_email: Optional[str] = None
    party_phone: Optional[str] = None
    source: Optional[str] = None
    source_message_id: Optional[str] = None


class CommitmentCreate(CommitmentBase):
    """Commitment creation schema"""
    pass


class CommitmentUpdate(BaseModel):
    """Commitment update schema"""
    action: Optional[str] = None
    description: Optional[str] = None
    commitment_type: Optional[CommitmentTypeSchema] = None
    deadline: Optional[datetime] = None
    status: Optional[CommitmentStatusSchema] = None
    party_name: Optional[str] = None
    party_email: Optional[str] = None
    party_phone: Optional[str] = None
    draft_content: Optional[str] = None
    reminder_sent: Optional[bool] = None
    escalated: Optional[bool] = None


class CommitmentResponse(CommitmentBase):
    """Commitment response schema"""
    id: int
    owner_id: int
    status: CommitmentStatusSchema
    auto_drafted: bool
    draft_content: Optional[str] = None
    reminder_sent: bool
    escalated: bool
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None
    is_overdue: bool
    
    class Config:
        from_attributes = True


class CommitmentListResponse(BaseModel):
    """Commitment list response schema"""
    id: int
    action: str
    deadline: datetime
    status: CommitmentStatusSchema
    party_name: Optional[str] = None
    commitment_type: CommitmentTypeSchema
    is_overdue: bool
    
    class Config:
        from_attributes = True
