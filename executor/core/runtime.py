import threading
import time

# In-memory experiment table
EXPERIMENTS = {}   # { uuid: {"status": "Q"} }


def simulate_experiment(exp_uuid: str):
    # mark running
    EXPERIMENTS[exp_uuid]["status"] = "R"
    time.sleep(2)  # simulate work
    EXPERIMENTS[exp_uuid]["status"] = "C"


def start_experiment(exp_uuid: str):
    t = threading.Thread(target=simulate_experiment, args=(exp_uuid,))
    t.start()
