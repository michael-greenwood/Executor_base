from fastapi import APIRouter

router = APIRouter(prefix="/remote_ctrl/sim", tags=["labels"])

@router.get("/experiment/{experiment_uuid}/sample/{sample_index}/label")
def get_label(experiment_uuid: str, sample_index: int):
    return {"label": "sample-label"}
