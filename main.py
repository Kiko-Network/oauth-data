from fastapi import FastAPI
from database import create_tables, engine
import models
from dotenv import load_dotenv
import auth
import air_quality

load_dotenv()  # Load environment variables from .env file

app = FastAPI()

# Include routers
app.include_router(auth.router)
app.include_router(air_quality.router)

@app.on_event("startup")
async def startup_event():
    create_tables(engine)
    print("Tables created (if they didn't exist)")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

