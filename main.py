from fastapi import FastAPI, APIRouter
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
from app.prompt import prompt


class PromptRequest(BaseModel):
    prompt: str

# serving static files
app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")
@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

# setting up API router
api_router = APIRouter()

# this endpoint responds to get requests from "/api/example"
@api_router.post("/prompt")
async def prompt_api(req: PromptRequest):
    response = prompt(req.prompt)
    return {"message": response}
# adding /api/ prefix to all api_router decorators
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

