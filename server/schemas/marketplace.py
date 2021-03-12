from typing import Optional
from pydantic import BaseModel


class MarketplaceBase(BaseModel):
    name: str
    description: str
    website: str
    contact_email: str
    contact_phone: Optional[str] = None
    technical_support_contact: Optional[str] = None


class MarketplaceCreate(MarketplaceBase):
    pass


class Marketplace(MarketplaceBase):
    id: int

    class Config:
        orm_mode = True
