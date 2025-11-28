from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter(prefix="/remote_ctrl/sim", tags=["files"])

@router.get("/experiment/{experiment_uuid}/sample/{sample_index}/file/{module_name}/{filename}")
def get_file(experiment_uuid: str, sample_index: int, module_name: str, filename: str):
    return PlainTextResponse("dummy file content")
