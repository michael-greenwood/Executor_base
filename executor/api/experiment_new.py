from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from core.runtime import EXPERIMENTS, MODULES 

router = APIRouter(prefix="/remote_ctrl/sim", tags=["experiment-new"])

class NewExperimentRequest(BaseModel):
    experiment_name: str
    campaign_name: str
    experiment_uuid: UUID
    exp_exec_fingerprint: UUID
    base_index: Optional[int] = None


@router.post("/experiment/new")
def experiment_new(payload: NewExperimentRequest):
    EXPERIMENTS[str(payload.experiment_uuid)] = {"status": "Q",
        "modules": {m: {"status": "Q"} for m in MODULES} } 

    return {
        "id": str(payload.experiment_uuid)
    }
