"""
This is the schemas module

For each of the following submodules:
    Category     (category.py)
    Marketplace  (marketplace.py)
    Product      (product.py)
    Seller       (seller.py)

There is a set of pydantic model schemas used by FastAPI to validate JSON
request bodies.

Note: from the FastAPI documentation:

"To avoid confusion between the SQLAlchemy models and the Pydantic models, we
will have the file models.py with the SQLAlchemy models, and the file
schemas.py with the Pydantic models.

These Pydantic models define more or less a "schema" (a valid data shape).

So this will help us avoiding confusion while using both."

So, "schemas" (pydantic.BaseModel) are used to validate JSON request bodies and
response formats, and "models" (db.Base, and SQLAlchemy.declarative_base()) are
used to manipulate our SQL tables.
"""
