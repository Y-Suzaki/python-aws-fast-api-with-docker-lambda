from fastapi import APIRouter
from logging import getLogger
from schemas.task import Tasks as TasksSchema, TaskCreateResponse as TaskCreateResponseSchema, TaskCreateRequest as TaskCreateRequestSchema

logger = getLogger("uvicorn.app")
router = APIRouter()


@router.get("/tasks", response_model=TasksSchema)
def list_tasks():
    return {
        "tasks": [
            {
                "id": 1,
                "title": "Fast APIを勉強する",
            },
            {
                "id": 2,
                "title": "進捗を確認する"
            }]
    }


@router.post("/tasks", response_model=TaskCreateResponseSchema)
def create_task(task: TaskCreateRequestSchema):
    logger.info(f'{task=}')
    return TaskCreateResponseSchema(id=3, **task.model_dump())


@router.put("/tasks/{task_id}", response_model=TaskCreateResponseSchema)
def update_task(task_id: int, task: TaskCreateRequestSchema):
    logger.info(f'{task_id=} {task=}')
    return TaskCreateResponseSchema(id=task_id, **task.model_dump())


@router.delete("/tasks/{task_id}", response_model=None)
def delete_task(task_id: int):
    logger.info(f"Delete task {task_id=}")
    return
