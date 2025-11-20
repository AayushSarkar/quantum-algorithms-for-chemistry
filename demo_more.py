# demo_more.py
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector

# prepare Bell state
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# simulate counts
sim = AerSimulator()
job = sim.run(qc, shots=1024)
res = job.result()
print("Counts:", res.get_counts())

# get the statevector (no measurements)
qc_sv = QuantumCircuit(2)
qc_sv.h(0); qc_sv.cx(0,1)
sv = Statevector.from_instruction(qc_sv)
print("Statevector amplitudes:", sv.data)

# transpile for a fake backend (shows optimization/transpilation)
tqc = transpile(qc, basis_gates=['u','cx'], optimization_level=3)
print("Transpiled circuit:\n", tqc)
