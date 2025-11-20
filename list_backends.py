import traceback
from qiskit_ibm_runtime import QiskitRuntimeService

try:
    svc = QiskitRuntimeService(channel="ibm_quantum_platform")
    backends = svc.backends()
    print("OK. Backends list (first 30):")
    for i, b in enumerate(backends[:30], start=1):
        try:
            print(f"{i:2d}. {b.name()}")
        except Exception:
            print(f"{i:2d}. <unreadable backend object>", type(b))
except Exception as e:
    print("ERROR:", type(e).__name__)
    traceback.print_exc()
