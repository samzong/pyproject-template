# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""

import uvicorn
from fastapi import FastAPI

from src.hello import hello

app = FastAPI(
    openapi_url="/api/v1/openapi.json",
    docs_url="/docs",
    redoc_url=None,
    title="Template Project",
    description="A template project of FastAPI",
    version="1.0",
    terms_of_service="https://samzong.me",
    contact={
        "name": "Samzong Lu",
        "url": "https://samzong.me",
        "email": "samzonglu@gmail.com"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
    },
)


@app.get("/")
async def index():
    return hello()


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
