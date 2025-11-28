from fastapi import APIRouter
from core.status_types import SampleStatus

router = APIRouter(prefix="/remote_ctrl/sim", tags=["sample-status"])


@router.get("/experiment/{experiment_uuid}/sample/{sample_index}/status/{module_name}")
def sample_status(experiment_uuid: str, sample_index: int, module_name: str):
    return {
        "status": SampleStatus.NOT_STARTED.value,
        "start_time": None,
        "end_time": None
    }
