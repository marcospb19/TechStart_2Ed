from fastapi import FastAPI
import db
import uvicorn
import documentation
import sys

# Import routers that compose the app endpoints
from routers import category, marketplace, product, seller

# Main app (plus docs)
app = FastAPI(**documentation.FASTAPI_APP_DOCUMENTATION)

# Attach each router to the main app
app.include_router(category.router)
app.include_router(marketplace.router)
app.include_router(product.router)
app.include_router(seller.router)


# Initialize the database before running app
@app.on_event('startup')
def init_db():
    db.init_db()


def main():
    """ Run the server app at `main.py` """
    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 8000
    uvicorn.run('main:app', host='0.0.0.0', port=port, reload=True)


if __name__ == '__main__':
    main()
