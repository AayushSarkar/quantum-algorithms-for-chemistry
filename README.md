# Qiskit Experiment Hub


::contentReference[oaicite:0]{index=0}


**Qiskit Experiment Hub** is a collection of small, hands-on quantum computing experiments built using **Qiskit**.  
This repository is focused on:

- Running Qiskit primitives (Sampler, Estimator)
- Testing Aer simulator locally
- Listing IBM Quantum backends
- Saving IBM tokens
- Playing with basic quantum circuits
- Trying IBM Runtime examples

This repo is ideal for students beginning with Qiskit and experimenting with real/simulated quantum systems.

---

## ⚙️ Installation

Install Qiskit:

```bash
pip install qiskit
````

Install additional dependencies:

```bash
pip install -r requirements.txt
```

---

# 🧪 Example: Simple Quantum Circuit

```python
from qiskit import QuantumCircuit
import numpy as np

qc = QuantumCircuit(3)
qc.h(0)
qc.p(np.pi/2, 0)
qc.cx(0, 1)
qc.cx(0, 2)

qc.draw()
```

---

# 📊 Sampling Results (Sampler)

```python
from qiskit.primitives import StatevectorSampler

qc_measured = qc.measure_all(inplace=False)

sampler = StatevectorSampler()
result = sampler.run([qc_measured], shots=1000).result()

print(result[0].data["meas"].get_counts())
```

---

# 📐 Expectation Value (Estimator)

```python
from qiskit.quantum_info import SparsePauliOp
from qiskit.primitives import StatevectorEstimator

operator = SparsePauliOp.from_list([("ZZ", 1), ("XX", 1)])
estimator = StatevectorEstimator()

value = estimator.run([(qc, operator)]).result()
print(value[0].data.evs)
```

---

# ⚛️ Transpiling for Hardware

```python
from qiskit import transpile
from qiskit.transpiler import Target, CouplingMap

target = Target.from_configuration(
    basis_gates=["cx", "rz", "sx"],
    coupling_map=CouplingMap.from_line(3)
)

transpiled = transpile(qc, target=target)
```

---

# 📁 Project Structure

The structure below matches the repository:

```plaintext
Qiskit-Experiment-Hub/
│
├── .binder/                         # Binder configuration for notebooks/demos
├── .github/                         # GitHub workflows, templates
├── crates/                          # Rust crates (if used internally)
├── docs/                            # Project documentation
├── qiskit/                          # Qiskit package sources / examples
├── releasenotes/                    # Release notes
├── test/                            # Tests and utilities
├── tools/                           # Helper tools/scripts
│
├── aer_histogram.png                # Example output image
├── CITATION.bib                     # Citation info
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE.txt                      # Apache 2.0 license
├── MANIFEST.in
├── Makefile
├── README.md                        # (This file)
├── requirements.txt
├── requirements-dev.txt
├── requirements-optional.txt
├── pyproject.toml
├── setup.py
├── setup.cfg
├── tox.ini
│
├── demo_more.py                     # Demo script
├── ibm_runtime_example.py           # IBM Runtime example
├── interactive_save_token.py        # Save IBM token interactively
├── list_backends.py                 # List IBM Quantum backends
├── local_sim_test.py                # Aer simulator tests
├── save_ibm_token.py                # Save IBM token
├── save_ibm_token_explicit.py       # Save token (explicit mode)
├── test_qiskit.py                   # Small Qiskit test script
│
├── Cargo.toml, Cargo.lock           # Rust configs
└── rust-toolchain.toml, rustfmt.toml, .clang-format, .editorconfig etc.

```

---

# ▶️ How to Run

List IBM Quantum backends:

```bash
python list_backends.py
```

Run the local simulator test:

```bash
python local_sim_test.py
```

Save IBM token:

```bash
python save_ibm_token.py
```

Run IBM Runtime example:

```bash
python ibm_runtime_example.py
```

---

# 🤝 Contribution

Contributions are welcome.
Please follow the guidelines in:

* CONTRIBUTING.md
* CODE_OF_CONDUCT.md

---

# 📄 License

This project is licensed under **Apache License 2.0**.
See `LICENSE.txt`.

```
