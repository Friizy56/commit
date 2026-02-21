from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    """Base user schema"""
    email: EmailStr
    username: str
    full_name: Optional[str] = None
    company_name: Optional[str] = None


class UserCreate(UserBase):
    """User schema for creation"""
    password: str


class UserUpdate(BaseModel):
    """User schema for update"""
    full_name: Optional[str] = None
    company_name: Optional[str] = None
    password: Optional[str] = None


class UserResponse(UserBase):
    """User schema for response"""
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class UserDetailResponse(UserResponse):
    """Detailed user schema with commitments count"""
    commitments_count: Optional[int] = None
    sales_count: Optional[int] = None
    
    class Config:
        from_attributes = True
