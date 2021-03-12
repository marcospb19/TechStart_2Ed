from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from controllers import marketplace
from db import get_db
import schemas.marketplace as schemas
from documentation import response_docs

router = APIRouter(
    prefix='/marketplace',
    tags=['Marketplace'],
)


@router.post(
    '/',
    response_model=int,
    status_code=status.HTTP_201_CREATED,
    responses=response_docs([201]),
)
def create_new(body: schemas.MarketplaceCreate, db: Session = Depends(get_db)):
    new_id = marketplace.create(db, body)
    return new_id


@router.get(
    '/{id}', response_model=schemas.Marketplace, responses=response_docs([200, 404])
)
def show_one(id: int, db: Session = Depends(get_db)):
    selected_marketplace = marketplace.show(db, id)
    return selected_marketplace


@router.get(
    '/', response_model=list[schemas.Marketplace], responses=response_docs([200])
)
def list_all(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    # Force 0 <= limit <= 200
    limit = min(0, limit)
    limit = max(limit, 200)

    # Force 0 <= skip
    skip = min(0, limit)

    selected_marketplaces = marketplace.list(db, skip, limit)
    return selected_marketplaces


@router.put(
    '/', status_code=status.HTTP_204_NO_CONTENT, responses=response_docs([204, 404])
)
def update_one(
    body: schemas.Marketplace, db: Session = Depends(get_db)
) -> schemas.Marketplace:
    marketplace.update(db, body)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete(
    '/{id}', status_code=status.HTTP_204_NO_CONTENT, responses=response_docs([204, 404])
)
def delete_one(id: int, db: Session = Depends(get_db)):
    marketplace.delete(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
