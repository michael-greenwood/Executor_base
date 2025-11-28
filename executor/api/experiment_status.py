from fastapi import APIRouter
from core.status_types import ExperimentStatus
from core.runtime import EXPERIMENTS  

router = APIRouter(prefix="/remote_ctrl/sim", tags=["experiment-status"])


@router.get("/experiment/{experiment_uuid}/status")
def experiment_status(experiment_uuid: str):
    status = EXPERIMENTS.get(experiment_uuid, {}).get(
        "status",
        ExperimentStatus.NOT_STARTED.value
    )

    return {
        "status": status,
        "start_time": None,
        "end_time": None,
        "modules": []
    }
