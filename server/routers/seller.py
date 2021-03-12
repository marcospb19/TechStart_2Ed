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
    new_id = seller.create(db, body)
    return new_id


@router.get('/{id}', response_model=schemas.Seller, responses=response_docs([200, 404]))
def show_one(id: int, db: Session = Depends(get_db)):
    selected_seller = seller.show(db, id)
    return selected_seller


@router.get('/', response_model=list[schemas.Seller], responses=response_docs([200]))
def list_all(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    selected_sellers = seller.list(db, skip, limit)
    return selected_sellers


@router.put(
    '/', status_code=status.HTTP_204_NO_CONTENT, responses=response_docs([204, 404])
)
def update_one(body: schemas.Seller, db: Session = Depends(get_db)) -> schemas.Seller:
    seller.update(db, body)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete(
    '/{id}', status_code=status.HTTP_204_NO_CONTENT, responses=response_docs([204, 404])
)
def delete_one(id: int, db: Session = Depends(get_db)):
    seller.delete(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
