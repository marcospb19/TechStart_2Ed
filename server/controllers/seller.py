from fastapi import status, HTTPException
from sqlalchemy.orm import Session

import schemas.seller as schemas
import models.seller as models


def create(db: Session, seller_body: schemas.SellerCreate) -> int:
    new_seller = models.Seller(**seller_body.dict())
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller.id


def show(db: Session, seller_id: int) -> models.Seller:
    seller = db.query(models.Seller).filter(models.Seller.id == seller_id).first()
    if not seller:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ERROR: Item with given id '{seller_id.id}' was not found",
        )

    return seller


def list(db: Session, skip: int, limit: int) -> list[schemas.Seller]:
    sellers = db.query(models.Seller).offset(skip).limit(limit).all()
    return sellers


def update(db: Session, new_seller: schemas.Seller) -> None:
    seller = db.query(models.Seller).filter(models.Seller.id == new_seller.id).first()
    if not seller:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ERROR: Item with given id '{new_seller.id}' was not found",
        )

    seller.fictional_name = new_seller.fictional_name
    seller.legal_name = new_seller.legal_name
    seller.cnpj = new_seller.cnpj
    seller.email_contact = new_seller.email_contact
    seller.contact_phone = new_seller.contact_phone
    seller.full_address = new_seller.full_address
    db.commit()


def delete(db: Session, seller_id: int) -> None:
    sellers = db.query(models.Seller).filter(models.Seller.id == seller_id)

    if not sellers.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ERROR: Item with given id '{seller_id}' was not found",
        )

    sellers.delete(synchronize_session=False)
    db.commit()
