from fastapi import APIRouter
from core.status_types import ModuleStatus

router = APIRouter(prefix="/remote_ctrl/sim", tags=["module-status"])


@router.get("/experiment/{experiment_uuid}/status/{module_name}")
def module_status(experiment_uuid: str, module_name: str):
    return {
        "status": ModuleStatus.NOT_STARTED.value,
        "start_time": None,
        "end_time": None
    }
