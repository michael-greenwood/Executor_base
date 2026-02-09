from enum import Enum


# ============================================================
# Experiment Status  
# ============================================================

class ExperimentStatus(str, Enum):
    PROPOSED = "P"
    NOT_STARTED = "Q"
    RUNNING = "R"
    COMPLETED = "C"
    TERMINATED = "T"
    SUSPENDED = "H"


EXPERIMENT_STATUS_LONG = {
    "P": "Proposed",
    "Q": "Not Started",
    "R": "Running",
    "C": "Completed",
    "T": "Terminated Early",
    "H": "Suspended",
}


# ============================================================
# Module Status  
# ============================================================

class ModuleStatus(str, Enum):
    PROPOSED = "P"
    NOT_STARTED = "Q"
    RUNNING = "R"
    COMPLETED = "C"
    TERMINATED = "T"
    SUSPENDED = "H"


MODULE_STATUS_LONG = EXPERIMENT_STATUS_LONG.copy()


# ============================================================
# Process Status 
# ============================================================

class ProcessStatus(str, Enum):
    MISSING_PREREQUISITES = "W"
    PREREQUISITES_MET = "P"
    SUBMITTED = "Q"
    RUNNING = "R"
    COMPLETED = "C"
    FINALIZED = "F"
    ERROR = "E"


PROCESS_STATUS_LONG = {
    "W": "Missing Prerequisites",
    "P": "Prerequisites Met",
    "Q": "Submitted Calculation",
    "R": "Running",
    "C": "Completed",
    "F": "Finalized",
    "E": "Error",
}


# ============================================================
# Sample Status 
# ============================================================

class SampleStatus(str, Enum):
    NOT_STARTED = "Q"
    RUNNING = "R"
    COMPLETED = "C"
    TERMINATED = "T"
    SUSPENDED = "H"


SAMPLE_STATUS_LONG = {
    "Q": "Not Started",
    "R": "Running",
    "C": "Completed",
    "T": "Terminated Early",
    "H": "Suspended",
}



