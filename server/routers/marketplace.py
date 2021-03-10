from fastapi import APIRouter

router = APIRouter(
    prefix='/marketplace',
    tags=['Marketplace'],
)


@router.get('/')
def hello():
    return 'hello marketplace'
