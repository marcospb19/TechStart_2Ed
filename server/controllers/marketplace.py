from fastapi import status, HTTPException
from sqlalchemy.orm import Session

import schemas.marketplace as schemas
import models.marketplace as models


def create(db: Session, marketplace_body: schemas.MarketplaceCreate) -> int:
    new_marketplace = models.Marketplace(**marketplace_body.dict())
    db.add(new_marketplace)
    db.commit()
    db.refresh(new_marketplace)
    return new_marketplace.id


def show(db: Session, marketplace_id: int) -> models.Marketplace:
    marketplace = (
        db.query(models.Marketplace)
        .filter(models.Marketplace.id == marketplace_id)
        .first()
    )
    if not marketplace:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ERROR: Item with given id '{marketplace_id.id}' was not found",
        )

    return marketplace


def list(db: Session, skip: int, limit: int) -> list[schemas.Marketplace]:
    marketplaces = db.query(models.Marketplace).offset(skip).limit(limit).all()
    return marketplaces


def update(db: Session, new_marketplace: schemas.Marketplace) -> None:
    marketplace = (
        db.query(models.Marketplace)
        .filter(models.Marketplace.id == new_marketplace.id)
        .first()
    )
    if not marketplace:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ERROR: Item with given id '{new_marketplace.id}' was not found",
        )

    marketplace.name = new_marketplace.name
    marketplace.description = new_marketplace.description
    marketplace.website = new_marketplace.website
    marketplace.contact_phone = new_marketplace.contact_phone
    marketplace.contact_email = new_marketplace.contact_email
    marketplace.technical_support_contact = new_marketplace.technical_support_contact
    db.commit()


def delete(db: Session, marketplace_id: int) -> None:
    marketplaces = db.query(models.Marketplace).filter(
        models.Marketplace.id == marketplace_id
    )

    if not marketplaces.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ERROR: Item with given id '{marketplace_id}' was not found",
        )

    marketplaces.delete(synchronize_session=False)
    db.commit()
