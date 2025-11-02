from fastapi import FastAPI
from routers import task
from logging import getLogger


logger = getLogger("uvicorn.app")

app = FastAPI()
app.include_router(task.router)


@app.get("/hello")
def hello():
    return {
        "message": "Hello World!"
    }


if __name__ == "__main__":
    import uvicorn
    import yaml

    with open("log_config.yml", "r") as f:
        config = yaml.safe_load(f)

    uvicorn.run(app, host="0.0.0.0", port=8000, log_config=config)
