from typing import Optional

import uvicorn
from fastapi import FastAPI
from odmantic import AIOEngine, Field, Model

app = FastAPI()

engine = AIOEngine(database="fastapi-app")


class Publisher(Model):
    name: str
    founded: int = Field(ge=1440)
    location: Optional[str] = None


@app.get("/")
async def root():
    publisher = Publisher(name="Garfield", founded=100000)
    await engine.save(publisher)
    return publisher


if __name__ == "__main__":
    from debugger import initialize_server_debugger_if_needed

    initialize_server_debugger_if_needed()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True)
