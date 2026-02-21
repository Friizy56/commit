from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class SalesStatusSchema(str, Enum):
    """Sales status enum"""
    PROSPECT = "prospect"
    NEGOTIATION = "negotiation"
    APPROVED = "approved"
    COMPLETED = "completed"
    LOST = "lost"
    ON_HOLD = "on_hold"


class SalesBase(BaseModel):
    """Base sales schema"""
    customer_name: str
    customer_email: Optional[str] = None
    customer_phone: Optional[str] = None
    title: str
    description: Optional[str] = None
    amount: Optional[float] = None
    currency: str = "USD"
    status: SalesStatusSchema = SalesStatusSchema.PROSPECT
    expected_close_date: Optional[datetime] = None
    next_action: Optional[str] = None
    next_action_date: Optional[datetime] = None


class SalesCreate(SalesBase):
    """Sales creation schema"""
    pass


class SalesUpdate(BaseModel):
    """Sales update schema"""
    customer_name: Optional[str] = None
    customer_email: Optional[str] = None
    customer_phone: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    amount: Optional[float] = None
    currency: Optional[str] = None
    status: Optional[SalesStatusSchema] = None
    expected_close_date: Optional[datetime] = None
    next_action: Optional[str] = None
    next_action_date: Optional[datetime] = None


class SalesResponse(SalesBase):
    """Sales response schema"""
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class SalesListResponse(BaseModel):
    """Sales list response schema"""
    id: int
    customer_name: str
    title: str
    amount: Optional[float] = None
    status: SalesStatusSchema
    expected_close_date: Optional[datetime] = None
    
    class Config:
        from_attributes = True
