"""
Documentation module.

Contains the dictionary FASTAPI_APP_DOCUMENTATION with OpenAPI modeled
documentation that is unpacked at the FastAPI app instantiation.

And function `response_docs` that generate documentation for each possible
request error.
"""


DETAILS = {
    200: 'SUCCESS: Operation succeeded, response body contains full object.',
    201: 'SUCCESS: Created and stored, response contains unique id (integer).',
    204: 'SUCCESS: Operation succeeded, response body is empty.',
    404: 'ERROR: Item with given id was not found.',
    422: 'ERROR: Request validation failed.',
}


RESPONSES = {
    200: {
        'description': DETAILS[200],
    },
    201: {
        'description': DETAILS[201],
        'content': {
            'application/json': {
                'example': 8912,
            }
        },
    },
    204: {
        'description': DETAILS[204],
    },
    404: {'description': DETAILS[404]},
    422: {'description': DETAILS[422]},
}


def response_docs(response_code_list: list[int]):
    """ Receives response codes and generate docs for each one. """
    result = {}
    for code in response_code_list:
        result = result | {code: RESPONSES.get(code, {})}
    return result


FASTAPI_APP_DOCUMENTATION = {
    'title': 'Tech Start',
    'description': 'Olist\'s Tech Start CRUD server.',
    'version': '0.1',
    'openapi_tags': [
        {
            'name': 'Product',
            'description': 'Operations with products.',
        },
        {
            'name': 'Category',
            'description': 'Operations with product categories.',
        },
        {
            'name': 'Marketplace',
            'description': 'Operations with marketplaces.',
        },
        {
            'name': 'Seller',
            'description': 'Operations with sellers.',
        },
    ],
    # Default for all requests
    'responses': response_docs([422]),
}
