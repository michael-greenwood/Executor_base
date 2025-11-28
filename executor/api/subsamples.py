from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/remote_ctrl/sim", tags=["subsamples"])


# ---- Request models ----

class SampleInfo(BaseModel):
    index: int
    label: Optional[str] = None


class SubsamplesRequest(BaseModel):
    self_indices: List[SampleInfo]
    other_indices: List[SampleInfo]


# ---- Endpoints ----

@router.get("/experiment/{experiment_uuid}/sample/{sample_index}/subsamples")
def get_subsamples(experiment_uuid: str, sample_index: int):
    # Stub: return empty lists
    return {
        "self_indices": [],
        "other_indices": []
    }


@router.post("/experiment/{experiment_uuid}/sample/{sample_index}/subsamples")
def post_subsamples(
    experiment_uuid: str,
    sample_index: int,
    payload: SubsamplesRequest
):
    # Stub: accept request, return dummy assigned indices
    return {
        "assigned": [info.index for info in payload.self_indices]
    }
