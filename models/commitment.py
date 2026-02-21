from sqlalchemy import Column, String, Integer, DateTime, Boolean, Enum, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from core.database import Base
import enum


class CommitmentStatus(str, enum.Enum):
    """Enum for commitment status"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    OVERDUE = "overdue"
    CANCELLED = "cancelled"


class CommitmentType(str, enum.Enum):
    """Enum for commitment types"""
    INVOICE = "invoice"
    REORDER = "reorder"
    PAYMENT = "payment"
    FOLLOWUP = "followup"
    DELIVERY = "delivery"
    REMINDER = "reminder"
    OTHER = "other"


class Commitment(Base):
    """Commitment model - tracks future obligations from communications"""
    
    __tablename__ = "commitments"
    
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    
    # Commitment details
    action = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    commitment_type = Column(Enum(CommitmentType), default=CommitmentType.OTHER, nullable=False)
    
    # Deadline and status
    deadline = Column(DateTime, nullable=False, index=True)
    status = Column(Enum(CommitmentStatus), default=CommitmentStatus.PENDING, nullable=False, index=True)
    
    # Party involved
    party_name = Column(String(255), nullable=True)
    party_email = Column(String(255), nullable=True)
    party_phone = Column(String(20), nullable=True)
    
    # Source information
    source = Column(String(50), nullable=True)  # email, whatsapp, telegram, etc.
    source_message_id = Column(String(255), nullable=True)
    
    # Tracking
    auto_drafted = Column(Boolean, default=False)
    draft_content = Column(Text, nullable=True)
    reminder_sent = Column(Boolean, default=False)
    escalated = Column(Boolean, default=False)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    completed_at = Column(DateTime, nullable=True)
    
    # Relationships
    owner = relationship("User", back_populates="commitments")
    
    def __repr__(self):
        return f"<Commitment(id={self.id}, action={self.action}, deadline={self.deadline}, status={self.status})>"
    
    def is_overdue(self) -> bool:
        """Check if commitment is overdue"""
        if self.status == CommitmentStatus.COMPLETED:
            return False
        return datetime.utcnow() > self.deadline
