from typing import Optional
from pydantic import BaseModel


class SellerBase(BaseModel):
    fictional_name: str
    legal_name: str
    cnpj: str
    full_address: str
    email_contact: str
    contact_phone: Optional[str] = None


class SellerCreate(SellerBase):
    pass


class Seller(SellerBase):
    id: int

    class Config:
        orm_mode = True
