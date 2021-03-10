from fastapi import APIRouter

router = APIRouter(
    prefix='/category',
    tags=['Category'],
)


@router.get('/')
def hello():
    return 'hello category'
