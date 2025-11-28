
from fastapi import FastAPI


app = FastAPI(title="Notification Service")


@app.get("/")
async def root():
    return {"message": "Hello from notification-service!"}

def main() -> None:
    print("Hello from notification-service!")


