from core.runtime import EXPERIMENTS
from fastapi import APIRouter
from pydantic import RootModel
from typing import Dict

router = APIRouter(prefix="/remote_ctrl/sim", tags=["experiment-config"])

class ConfigInputs(RootModel[Dict[str, float]]):
    pass


@router.post("/experiment/{experiment_uuid}/config/{module_name}")
def config_inputs(experiment_uuid: str, module_name: str, payload: ConfigInputs):
    exp = EXPERIMENTS.get(experiment_uuid)
    if exp is None:
        return {}

    # Store config values
    exp["config"][module_name] = payload.root
    return {}
