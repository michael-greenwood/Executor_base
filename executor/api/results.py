from fastapi import APIRouter

router = APIRouter(prefix="/remote_ctrl/sim", tags=["results"])


@router.get("/experiment/{experiment_uuid}/results")
def all_results(experiment_uuid: str):
    return {}


@router.get("/experiment/{experiment_uuid}/results/{module_name}")
def module_results(experiment_uuid: str, module_name: str):
    return {}


@router.get("/experiment/{experiment_uuid}/sample/{sample_index}/results/{module_name}")
def sample_module_results(experiment_uuid: str, sample_index: int, module_name: str):
    return {}
