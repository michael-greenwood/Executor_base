from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/remote_ctrl/sim", tags=["experiment-config-file"])

class FileUploadMeta(BaseModel):
    checksum: Optional[str] = None


@router.post("/experiment/{experiment_uuid}/config/{module_name}/file/{filename}")
def config_file(
    experiment_uuid: str,
    module_name: str,
    filename: str,
    meta: FileUploadMeta = None,
    file: UploadFile = File(...)
):
    return {"status": "ok", "file_received": filename}
