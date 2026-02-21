from sqlalchemy import Column, String, Integer, DateTime, Boolean, Enum, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from core.database import Base
import enum


class SalesStatus(str, enum.Enum):
    """Enum for sales/deal status"""
    PROSPECT = "prospect"
    NEGOTIATION = "negotiation"
    APPROVED = "approved"
    COMPLETED = "completed"
    LOST = "lost"
    ON_HOLD = "on_hold"


class Sales(Base):
    """Sales model - tracks sales interactions and deals"""
    
    __tablename__ = "sales"
    
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    
    # Deal information
    customer_name = Column(String(255), nullable=False)
    customer_email = Column(String(255), nullable=True)
    customer_phone = Column(String(20), nullable=True)
    
    # Sales details
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    amount = Column(Float, nullable=True)
    currency = Column(String(3), default="USD")
    
    # Status and tracking
    status = Column(Enum(SalesStatus), default=SalesStatus.PROSPECT, nullable=False, index=True)
    expected_close_date = Column(DateTime, nullable=True)
    
    # Commitments related to this deal
    next_action = Column(String(255), nullable=True)
    next_action_date = Column(DateTime, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relationships
    owner = relationship("User", back_populates="sales")
    
    def __repr__(self):
        return f"<Sales(id={self.id}, customer_name={self.customer_name}, status={self.status})>"
