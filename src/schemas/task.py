from typing import Optional
from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, description="タスクのタイトル", example="タスクのタイトル サンプル")


class Task(TaskBase):
    id: int =  Field(description="主キー", example=1)

    class Config:
        orm_mode = True


class Tasks(BaseModel):
    tasks: list[Task]


class TaskCreateRequest(TaskBase):
    pass


class TaskCreateResponse(TaskCreateRequest):
    id: int

    class Config:
        orm_mode = True
