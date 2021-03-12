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
    """
    ## Create a new marketplace.

    Body structure:
    - **name**: name of the marketplace.
    - **description**: a long description about it.
    - **website**: the marketplace website URL.
    - **contact_email**: email for contacting.
    - **contact_phone**: phone for contacting (optional).
    - **technical_support_contact**: contact method when products are broken (optional).
    """
    new_id = marketplace.create(db, body)
    return new_id


@router.get(
    '/{id}', response_model=schemas.Marketplace, responses=response_docs([200, 404])
)
def show_one(id: int, db: Session = Depends(get_db)):
    """
    ## Show one marketplace with a specific id.

    Parameters:
    - **id**: the integer id of the requested marketplace.
    """
    selected_marketplace = marketplace.show(db, id)
    return selected_marketplace


@router.get(
    '/', response_model=list[schemas.Marketplace], responses=response_docs([200])
)
def list_all(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    """
    ## List all marketplaces.

    Filter parameters (optional):
    - **skip**: skip the first N elements (default = 0).
    - **limit**: limit the listed amount (default = 20).
    """
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
    """
    ## Update a marketplace with a specific id.

    Body structure:
    - **id**: id of the marketplace you want to update.
    - **name**: name of the marketplace.
    - **description**: a long description about it.
    - **website**: the marketplace website URL.
    - **contact_email**: email for contacting.
    - **contact_phone**: phone for contacting (optional).
    - **technical_support_contact**: contact method when products are broken (optional).

    If the marketplace with given id isn't found, this returns a _Not Found Error (404)_.

    Otherwise, the operation overwrites the previous value.
    """
    marketplace.update(db, body)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete(
    '/{id}', status_code=status.HTTP_204_NO_CONTENT, responses=response_docs([204, 404])
)
def delete_one(id: int, db: Session = Depends(get_db)):
    """
    ## Delete a marketplace with a specific id.

    Parameters:
    - **id**: the integer id of the marketplace to delete.

    If the marketplace with given id isn't found, this returns a _Not Found Error (404)_.
    """
    marketplace.delete(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
