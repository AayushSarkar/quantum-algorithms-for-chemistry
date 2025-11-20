from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler

# uses saved account (from QiskitRuntimeService.save_account)
service = QiskitRuntimeService(channel="ibm_quantum_platform")

# choose a backend; .backends() lists available targets
print("Available backends:", [b.name() for b in service.backends()])
backend = service.backends()[0]  # pick the first one (adjust as needed)
print("Using backend:", backend.name())

# prepare a simple circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# run with Sampler primitive via runtime (fast path for sampling)
sampler = Sampler(session=service, backend=backend)
job = sampler.ru
