from logging import config
import threading
import time

# In-memory experiment table
EXPERIMENTS = {}   # { uuid: {"status": "Q"} }
# Executor-defined modules
MODULES = ["module_A", "module_B"]

def simulate_experiment(exp_uuid: str):
    try:
        print("SIM START", exp_uuid)
        exp = EXPERIMENTS[exp_uuid]
        print("EXP FOUND:", exp)

        time.sleep(3)
        exp["status"] = "R"
        print("SET TO R")

        time.sleep(3)
        for m in exp["modules"]:
            exp["modules"][m]["status"] = "R"
            print("RUNNING", m)
            run(exp,m)
            time.sleep(3)
            exp["modules"][m]["status"] = "C"
            print("COMPLETED", m)

        exp["status"] = "C"
        print("EXP COMPLETE")

    except Exception as e:
        print("SIM ERROR:", e)


def run(exp,m):
    config = exp["config"].get(m, {})
    if "x" in config:
            exp["modules"][m]["output"] = {"x_plus_one": config["x"] + 1}
    else:
        exp["modules"][m]["output"] = {"x_plus_one": None}

def start_experiment(exp_uuid: str):
    t = threading.Thread(target=simulate_experiment, args=(exp_uuid,))
    t.start()
