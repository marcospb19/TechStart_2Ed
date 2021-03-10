from fastapi import FastAPI
import uvicorn

app = FastAPI()


if __name__ == '__main__':
    # Run server with the app declared above in this file
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
