from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

print("Hello HDFC")

# ADD THIS AT THE BOTTOM:
if __name__ == "__main__":
    # This tells python: "If this file is run directly, start uvicorn"
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)