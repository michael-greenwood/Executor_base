from fastapi import APIRouter
from core.status_types import ExperimentStatus
from core.runtime import start_experiment   

router = APIRouter(prefix="/remote_ctrl/sim", tags=["experiment-queue"])


@router.put("/queue/{experiment_uuid}")
def queue_experiment(experiment_uuid: str):
    start_experiment(experiment_uuid)       
    return {}
