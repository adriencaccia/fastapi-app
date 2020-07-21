import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    message = "Hello World"
    return {"message": message}


if __name__ == "__main__":
    from debugger import initialize_server_debugger_if_needed

    initialize_server_debugger_if_needed()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True)
