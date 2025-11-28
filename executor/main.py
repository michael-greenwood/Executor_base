from fastapi import FastAPI

from api.experiment_new import router as exp_new_router
from api.experiment_config import router as exp_config_router
from api.experiment_config_file import router as exp_config_file_router
from api.experiment_queue import router as exp_queue_router
from api.experiment_status import router as exp_status_router
from api.module_status import router as module_status_router
from api.sample_status import router as sample_status_router
from api.results import router as results_router
from api.files import router as files_router
from api.subsamples import router as subsamples_router
from api.labels import router as labels_router

app = FastAPI(title="Hello Executor")

app.include_router(exp_new_router)
app.include_router(exp_config_router)
app.include_router(exp_config_file_router)
app.include_router(exp_queue_router)
app.include_router(exp_status_router)
app.include_router(module_status_router)
app.include_router(sample_status_router)
app.include_router(results_router)
app.include_router(files_router)
app.include_router(subsamples_router)
app.include_router(labels_router)
