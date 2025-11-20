from qiskit_ibm_runtime import QiskitRuntimeService
QiskitRuntimeService.save_account(
    channel="ibm_quantum_platform",
    token="PUT_YOUR_TOKEN_HERE",
    set_as_default=True,
    overwrite=True
)
print("Saved IBM Quantum account (channel=ibm_quantum_platform).")
