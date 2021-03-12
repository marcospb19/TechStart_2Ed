from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class Marketplace(Base):
    __tablename__ = 'marketplaces'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    website = Column(String)
    contact_phone = Column(String)
    contact_email = Column(String)
    technical_support_contact = Column(String)
