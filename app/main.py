from fastapi import FastAPI

app = FastAPI(
    title="Inventory Menagment System API",
    description = "A simple API for managing inventory in a store across multiple locations.",
    version="1.0.0"
)

@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "online",
        "message": "Inventory Management System API is running."
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port= 8000, reload=True)

