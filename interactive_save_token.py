# This script will ask you to paste your token into stdin.
# Run it and then paste your token (it will not echo).
import getpass
from qiskit_ibm_runtime import QiskitRuntimeService

token = getpass.getpass(prompt="Paste IBM Quantum API token and press Enter: ")
QiskitRuntimeService.save_account(
    channel="ibm_quantum_platform",
    token=token,
    set_as_default=True,
    overwrite=True
)
print("Saved IBM Quantum account (channel=ibm_quantum_platform).")
