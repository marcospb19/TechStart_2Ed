from typing import Optional

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from controllers import product
from db import get_db
import schemas.product as schemas
from documentation import response_docs

router = APIRouter(
    prefix='/product',
    tags=['Product'],
)


@router.post(
    '/',
    response_model=int,
    status_code=status.HTTP_201_CREATED,
    responses=response_docs([201]),
)
def create_new(body: schemas.ProductCreate, db: Session = Depends(get_db)):
    """
    ## Create a new product.

    Body structure:
    - **name**: name of the product.
    - **description**: a long description about it.
    - **price**: price in dollar cents.
    - **category**: to put this product in a pre-registered category (optional).

    You should create the category before, at `'/category'` (_POST_), otherwise,
    this returns a _Not Found Error (404)_.
    """
    new_id = product.create(db, body)
    return new_id


@router.get(
    '/{id}', response_model=schemas.Product, responses=response_docs([200, 404])
)
def show_one(id: int, db: Session = Depends(get_db)):
    """
    ## Show one product with a specific id.

    Parameters:
    - **id**: the integer id of the requested product.
    """
    selected_product = product.show(db, id)
    return selected_product


@router.get('/', response_model=list[schemas.Product], responses=response_docs([200]))
def list_all(
    name: Optional[str] = None,
    description: Optional[str] = None,
    price: Optional[int] = None,
    category: Optional[str] = None,
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db),
):
    """
    ## List all products.

    Filter parameters (optional):
    - **name**: full match.
    - **description**: full match.
    - **price**: full match.
    - **category**: full match.
    - **skip**: skip the first N elements (default = 0).
    - **limit**: limit the listed amount (default = 20).
    """
    # Force 0 <= limit <= 200
    limit = min(0, limit)
    limit = max(limit, 200)

    # Force 0 <= skip
    skip = min(0, limit)

    selected_products = product.list(
        db, name, description, price, category, skip, limit
    )
    return selected_products


@router.put(
    '/', status_code=status.HTTP_204_NO_CONTENT, responses=response_docs([204, 404])
)
def update_one(body: schemas.Product, db: Session = Depends(get_db)) -> schemas.Product:
    """
    ## Update a product with a specific id.

    Body structure:
    - **id**: id of the product you want to update.
    - **name**: name of the product.
    - **description**: a long description about it.
    - **price**: price in dollar cents.
    - **category**: to put this product in a pre-registered category (optional).

    If the product with given id isn't found, this returns a _Not Found Error (404)_.

    Otherwise, the operation overwrites the previous value.
    """
    product.update(db, body)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete(
    '/{id}', status_code=status.HTTP_204_NO_CONTENT, responses=response_docs([204, 404])
)
def delete_one(id: int, db: Session = Depends(get_db)):
    """
    ## Delete a product with a specific id.

    Parameters:
    - **id**: the integer id of the product to delete.

    If the product with given id isn't found, this returns a _Not Found Error (404)_.
    """
    product.delete(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
