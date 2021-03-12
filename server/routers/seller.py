from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from controllers import seller
from db import get_db
import schemas.seller as schemas
from documentation import response_docs

router = APIRouter(
    prefix='/seller',
    tags=['Seller'],
)


@router.post(
    '/',
    response_model=int,
    status_code=status.HTTP_201_CREATED,
    responses=response_docs([201]),
)
def create_new(body: schemas.SellerCreate, db: Session = Depends(get_db)):
    """
    ## Create a new seller.

    Body structure:
    - **name**: name of the seller.
    - **description**: a long description about it.
    - **fictional_name**: name used by the seller.
    - **legal_name**: legal name.
    - **cnpj**: the brazilian CNPJ code.
    - **full_address**: personal address of the seller.
    - **email_contact**: email contact of the seller.
    - **contact_phone**: phone contact of the seller (optional).
    """
    new_id = seller.create(db, body)
    return new_id


@router.get('/{id}', response_model=schemas.Seller, responses=response_docs([200, 404]))
def show_one(id: int, db: Session = Depends(get_db)):
    """
    ## Show one seller with a specific id.

    Parameters:
    - **id**: the integer id of the requested seller.
    """
    selected_seller = seller.show(db, id)
    return selected_seller


@router.get('/', response_model=list[schemas.Seller], responses=response_docs([200]))
def list_all(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    """
    ## List all sellers.

    Filter parameters (optional):
    - **skip**: skip the first N elements (default = 0).
    - **limit**: limit the listed amount (default = 20).
    """
    # Force 0 <= limit <= 200
    limit = min(0, limit)
    limit = max(limit, 200)

    # Force 0 <= skip
    skip = min(0, limit)

    selected_sellers = seller.list(db, skip, limit)
    return selected_sellers


@router.put(
    '/', status_code=status.HTTP_204_NO_CONTENT, responses=response_docs([204, 404])
)
def update_one(body: schemas.Seller, db: Session = Depends(get_db)) -> schemas.Seller:
    """
    ## Update a seller with a specific id.

    Body structure:
    - **id**: id of the seller you want to update.
    - **name**: name of the seller.
    - **description**: a long description about it.
    - **fictional_name**: name used by the seller.
    - **legal_name**: legal name.
    - **cnpj**: the brazilian CNPJ code.
    - **full_address**: personal address of the seller.
    - **email_contact**: email contact of the seller.
    - **contact_phone**: phone contact of the seller (optional).

    If the seller with given id isn't found, this returns a _Not Found Error (404)_.

    Otherwise, the operation overwrites the previous value.
    """
    seller.update(db, body)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete(
    '/{id}', status_code=status.HTTP_204_NO_CONTENT, responses=response_docs([204, 404])
)
def delete_one(id: int, db: Session = Depends(get_db)):
    """
    ## Delete a seller with a specific id.

    Parameters:
    - **id**: the integer id of the seller to delete.

    If the seller with given id isn't found, this returns a _Not Found Error (404)_.
    """
    seller.delete(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
