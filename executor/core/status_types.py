from enum import Enum


# ============================================================
# Experiment Status  (same as module status table you gave)
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
# Module Status  (same table as experiment status)
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
# Process Status (separate table)
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
# Sample Status (you gave this separately)
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


# ============================================================
# Validation Helpers
# ============================================================

def validate_experiment_status(value: str) -> bool:
    return value in ExperimentStatus._value2member_map_


def validate_module_status(value: str) -> bool:
    return value in ModuleStatus._value2member_map_


def validate_process_status(value: str) -> bool:
    return value in ProcessStatus._value2member_map_


def validate_sample_status(value: str) -> bool:
    return value in SampleStatus._value2member_map_


def long_name_experiment(value: str) -> str:
    return EXPERIMENT_STATUS_LONG.get(value, "Unknown")


def long_name_module(value: str) -> str:
    return MODULE_STATUS_LONG.get(value, "Unknown")


def long_name_process(value: str) -> str:
    return PROCESS_STATUS_LONG.get(value, "Unknown")


def long_name_sample(value: str) -> str:
    return SAMPLE_STATUS_LONG.get(value, "Unknown")
