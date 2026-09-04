from fastapi import APIRouter, HTTPException

from services.metric_service import system_get_metrics

router = APIRouter()

@router.get("/metrics", status_code= 200)
def get_metrics():
    
    try:
        metrics = system_get_metrics()
        return metrics
    
    except:
        raise HTTPException (
            status_code= 500,
            detail= "Internal server error" 
        )