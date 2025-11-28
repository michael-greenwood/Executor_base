from fastapi import APIRouter
from core.status_types import ExperimentStatus

router = APIRouter(prefix="/remote_ctrl/sim", tags=["experiment-status"])


@router.get("/experiment/{experiment_uuid}/status")
def experiment_status(experiment_uuid: str):
    return {
        "status": ExperimentStatus.RUNNING.value,
        "start_time": None,
        "end_time": None,
        "modules": []
    }
