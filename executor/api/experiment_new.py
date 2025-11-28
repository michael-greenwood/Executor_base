from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from uuid import UUID

router = APIRouter(prefix="/remote_ctrl/sim", tags=["experiment-new"])

class NewExperimentRequest(BaseModel):
    experiment_name: str
    campaign_name: str
    experiment_uuid: UUID
    exp_exec_fingerprint: UUID
    base_index: Optional[int] = None


@router.post("/experiment/new")
def experiment_new(payload: NewExperimentRequest):
    # We accept the fields but ignore them (hello world)
    return {
        "status": "ok",
        "id": str(payload.experiment_uuid)
    }
