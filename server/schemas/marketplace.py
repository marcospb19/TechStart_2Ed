from pydantic import BaseModel


class MarketplaceBase(BaseModel):
    name: str
    description: str
    website: str
    contact_email: str
    contact_phone: str = ''
    technical_support_contact: str = ''


class MarketplaceCreate(MarketplaceBase):
    pass


class Marketplace(MarketplaceBase):
    id: int

    class Config:
        orm_mode = True
