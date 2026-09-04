from fastapi import FastAPI #importing FastAPI class
from routers import metric, aws # from router folder import meric file

app = FastAPI(
    title = "Internal Devops Utilities API",
    description= "Thisis internal API which can be use for monitoring metrics, AWS usage, log analysis etc",
    version= "1.0.0",
    docs_url= "/docs",
    redoc_url= "/redoc"
)

@app.get("/")
def hello(): #This is hello api just for testing
    return {"message" : "hello dosto"}

app.include_router(metric.router)
app.include_router(aws.router, prefix="/aws")
