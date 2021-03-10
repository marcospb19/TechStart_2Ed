from fastapi import APIRouter
from controllers import seller

router = APIRouter(
    prefix='/seller',
    tags=['Seller'],
)


@router.post('/')
def create():
    seller.create()


@router.get('/')
def show():
    seller.show()


@router.put('/')
def update():
    seller.update()


@router.delete('/')
def delete():
    seller.delete()
