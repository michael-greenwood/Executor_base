from fastapi import APIRouter
from core.status_types import ExperimentStatus

router = APIRouter(prefix="/remote_ctrl/sim", tags=["experiment-queue"])


@router.put("/queue/{experiment_uuid}")
def queue_experiment(experiment_uuid: str):
    return {"status": ExperimentStatus.RUNNING.value}
