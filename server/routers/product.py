from fastapi import APIRouter
from controllers import product

router = APIRouter(
    prefix='/product',
    tags=['Product'],
)


@router.post('/')
def create():
    product.create()


@router.get('/')
def show():
    product.show()


@router.put('/')
def update():
    product.update()


@router.delete('/')
def delete():
    product.delete()
