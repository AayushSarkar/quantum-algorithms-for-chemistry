from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator   # import the Aer simulator directly

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

sim = AerSimulator()
# newer Aer API accepts either a circuit or list of circuits
job = sim.run(qc, shots=256)
result = job.result()
print(result.get_counts())
