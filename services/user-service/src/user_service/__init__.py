from fastapi import FastAPI

app = FastAPI(title="User Service")



@app.get("/")
async def root():
    return {"message": "Hello from user-service!"}


def main() -> None:
    print("Hello from user-service!")
