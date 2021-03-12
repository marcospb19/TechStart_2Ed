from fastapi import status, HTTPException
from sqlalchemy.orm import Session

import schemas.category as schemas
import models.category as models


def create(db: Session, category_body: schemas.CategoryCreate) -> int:
    new_category = models.Category(**category_body.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category.id


def show(db: Session, category_id: int) -> models.Category:
    category = (
        db.query(models.Category).filter(models.Category.id == category_id).first()
    )
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ERROR: Item with given id '{category_id.id}' was not found",
        )

    return category


def list(db: Session, skip: int, limit: int) -> list[schemas.Category]:
    categories = db.query(models.Category).offset(skip).limit(limit).all()
    return categories


def update(db: Session, new_category: schemas.Category) -> None:
    category = (
        db.query(models.Category).filter(models.Category.id == new_category.id).first()
    )
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ERROR: Item with given id '{new_category.id}' was not found",
        )

    category.name = new_category.name
    category.description = new_category.description
    db.commit()


def delete(db: Session, category_id: int) -> None:
    categories = db.query(models.Category).filter(models.Category.id == category_id)

    if not categories.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ERROR: Item with given id '{category_id}' was not found",
        )

    categories.delete(synchronize_session=False)
    db.commit()
