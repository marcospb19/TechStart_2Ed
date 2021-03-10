from fastapi import APIRouter
from controllers import marketplace

router = APIRouter(
    prefix='/marketplace',
    tags=['Marketplace'],
)


@router.post('/')
def create():
    marketplace.create()


@router.get('/')
def show():
    marketplace.show()


@router.put('/')
def update():
    marketplace.update()


@router.delete('/')
def delete():
    marketplace.delete()
