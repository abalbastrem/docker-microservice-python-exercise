from fastapi import FastAPI

app = FastAPI(
    title="Tip API", openapi_url="/openapi.json"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")