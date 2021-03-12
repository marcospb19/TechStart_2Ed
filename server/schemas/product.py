from typing import Optional
from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    price: int
    category: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
