import traceback

state = None
try:
    state["start_from"] = "123"
except Exception:
    traceback.print_exc()