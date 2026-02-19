from fastapi import APIRouter
from core.status_types import ExperimentStatus
from core.runtime import start_experiment   

router = APIRouter(prefix="/remote_ctrl/sim", tags=["experiment-queue"])


@router.put("/queue/{experiment_uuid}", status_code=201)
def queue_experiment(experiment_uuid: str):
    #change experiment to queue "status": "P"
    start_experiment(experiment_uuid)       
    return {}
