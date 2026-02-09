from fastapi import APIRouter
from core.status_types import ModuleStatus
from core.runtime import EXPERIMENTS

router = APIRouter(prefix="/remote_ctrl/sim", tags=["module-status"])


@router.get("/experiment/{experiment_uuid}/status/{module_name}")
def module_status(experiment_uuid: str, module_name: str):
    exp = EXPERIMENTS.get(experiment_uuid, {})
    module = exp.get("modules", {}).get(module_name, {})
    status = module.get("status", "Q")

    return {
        "status": status,
        "start_time": None,
        "end_time": None
    }
