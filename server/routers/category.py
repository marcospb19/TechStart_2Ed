from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from controllers import category
from db import get_db
import schemas.category as schemas
from documentation import response_docs

router = APIRouter(
    prefix='/category',
    tags=['Category'],
)


@router.post(
    '/',
    response_model=int,
    status_code=status.HTTP_201_CREATED,
    responses=response_docs([201]),
)
def create_new(body: schemas.CategoryCreate, db: Session = Depends(get_db)):
    """
    ## Create a new category.

    Body structure:
    - **name**: name of the category.
    - **description**: a long description about it (optional).

    This is required to add products to categories.
    """
    new_id = category.create(db, body)
    return new_id


@router.get(
    '/{id}', response_model=schemas.Category, responses=response_docs([200, 404])
)
def show_one(id: int, db: Session = Depends(get_db)):
    """
    ## Show one category with a specific id.

    Parameters:
    - **id**: the integer id of the requested category.
    """
    selected_category = category.show(db, id)
    return selected_category


@router.get('/', response_model=list[schemas.Category], responses=response_docs([200]))
def list_all(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    """
    ## List all categories.

    Filter parameters (optional):
    - **skip**: skip the first N elements (default = 0).
    - **limit**: limit the listed amount (default = 20).
    """
    # Force 0 <= limit <= 200
    limit = min(0, limit)
    limit = max(limit, 200)

    # Force 0 <= skip
    skip = min(0, limit)

    selected_categories = category.list(db, skip, limit)
    return selected_categories


@router.put(
    '/', status_code=status.HTTP_204_NO_CONTENT, responses=response_docs([204, 404])
)
def update_one(
    body: schemas.Category, db: Session = Depends(get_db)
) -> schemas.Category:
    """
    ## Update a category with a specific id.

    Body structure:
    - **id**: id of the category you want to update.
    - **name**: name of the category.
    - **description**: a long description about it (optional).

    If the category with given id isn't found, this returns a _Not Found Error (404)_.

    Otherwise, the operation overwrites the previous value.
    """
    category.update(db, body)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete(
    '/{id}', status_code=status.HTTP_204_NO_CONTENT, responses=response_docs([204, 404])
)
def delete_one(id: int, db: Session = Depends(get_db)):
    """
    ## Delete a category with a specific id.

    Parameters:
    - **id**: the integer id of the category to delete.

    If the category with given id isn't found, this returns a _Not Found Error (404)_.
    """
    category.delete(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
