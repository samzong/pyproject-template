# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(
    openapi_url="/api/v1/openapi.json",
    docs_url="/documentation",
    redoc_url=None,
    openapi_tags=tags_metadata,
    title="user example",
    description="A demo project of user example",
    version="1.0",
    terms_of_service="https://samzong.me",
    contact={
        "name": "Alex",
        "url": "https://samzong.me",
        "email": "samzong.lu@gmail.com"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
    },
)


class User(BaseModel):
    # user_id: int
    user_name: str
    email: str
    age: int
    is_active: bool
    bio: Optional[str]


users = []


@app.get("/users", response_model=List[User], tags=["users"])
async def get_users():
    return users


@app.post("/users", tags=["users", "items"])
async def create_user(user: User):
    users.append(user)
    return "Success"


@app.get("/users/{id}", tags=["users"],
         summary="This is summary",
         response_description="This is a response_description")
async def get_user(
        id: int = Path(..., description="The ID of the user you want to get", gt=1),
        q: str = Query(None, max_length=6)
):
    return {"user": users[id], "q": q}


@app.delete("/user/{id}", tags=["items"], deprecated=True)
async def delete_user(id: int = Path(..., description="The ID of the user is you want remove it")):
    """
    - This line 1
    - This line 2
    """
    users.pop(id)
    return "Success"
