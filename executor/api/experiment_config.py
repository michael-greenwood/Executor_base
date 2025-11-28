from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict

router = APIRouter(prefix="/remote_ctrl/sim", tags=["experiment-config"])

class ConfigInputs(BaseModel):
    __root__: Dict[str, float]   # accept arbitrary fields


@router.post("/experiment/{experiment_uuid}/config/{module_name}")
def config_inputs(experiment_uuid: str, module_name: str, payload: ConfigInputs):
    return {"status": "ok"}
