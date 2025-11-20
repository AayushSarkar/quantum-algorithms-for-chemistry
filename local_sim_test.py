from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2,2)
qc.h(0); qc.cx(0,1); qc.measure_all()

sim = AerSimulator()
job = sim.run(qc, shots=1024)
res = job.result()

print("Counts:", res.get_counts())

# optional: save histogram image
fig = plot_histogram(res.get_counts())
fig.savefig("aer_histogram.png")
print("Saved histogram to aer_histogram.png")
