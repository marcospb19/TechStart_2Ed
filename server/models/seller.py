from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class Seller(Base):
    __tablename__ = 'sellers'

    id = Column(Integer, primary_key=True, index=True)
    fictional_name = Column(String, index=True)
    legal_name = Column(String, index=True)
    cnpj = Column(String, index=True)
    email_contact = Column(String, index=True)
    contact_phone = Column(String, index=True)
    full_address = Column(String, index=True)
