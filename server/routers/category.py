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
    new_id = category.create(db, body)
    return new_id


@router.get(
    '/{id}', response_model=schemas.Category, responses=response_docs([200, 404])
)
def show_one(id: int, db: Session = Depends(get_db)):
    selected_category = category.show(db, id)
    return selected_category


@router.get('/', response_model=list[schemas.Category], responses=response_docs([200]))
def list_all(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    selected_categories = category.list(db, skip, limit)
    return selected_categories


@router.put(
    '/', status_code=status.HTTP_204_NO_CONTENT, responses=response_docs([204, 404])
)
def update_one(
    body: schemas.Category, db: Session = Depends(get_db)
) -> schemas.Category:
    category.update(db, body)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete(
    '/{id}', status_code=status.HTTP_204_NO_CONTENT, responses=response_docs([204, 404])
)
def delete_one(id: int, db: Session = Depends(get_db)):
    category.delete(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
