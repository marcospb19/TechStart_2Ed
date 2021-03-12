from fastapi import status, HTTPException
from sqlalchemy.orm import Session

import schemas.product as schemas
import models.product as models


def create(db: Session, product_body: schemas.ProductCreate) -> int:
    new_product = models.Product(**product_body.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product.id


def show(db: Session, product_id: int) -> models.Product:
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ERROR: Item with given id '{product_id.id}' was not found",
        )

    return product


def list(db: Session, skip: int, limit: int) -> list[schemas.Product]:
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products


def update(db: Session, new_product: schemas.Product) -> None:
    product = (
        db.query(models.Product).filter(models.Product.id == new_product.id).first()
    )
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ERROR: Item with given id '{new_product.id}' was not found",
        )

    product.name = new_product.name
    product.description = new_product.description
    product.price = new_product.price
    product.category = new_product.category
    db.commit()


def delete(db: Session, product_id: int) -> None:
    products = db.query(models.Product).filter(models.Product.id == product_id)

    if not products.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ERROR: Item with given id '{product_id}' was not found",
        )

    products.delete(synchronize_session=False)
    db.commit()
