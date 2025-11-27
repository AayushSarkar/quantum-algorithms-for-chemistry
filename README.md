

````markdown
# Quantum Algorithms for Chemistry using Qiskit

[![License](https://img.shields.io/github/license/Qiskit/qiskit.svg?)](https://opensource.org/licenses/Apache-2.0)
[![Current Release](https://img.shields.io/github/release/Qiskit/qiskit.svg?logo=Qiskit)](https://github.com/Qiskit/qiskit/releases)
[![Extended Support Release](https://img.shields.io/github/v/release/Qiskit/qiskit?sort=semver&filter=1.*&logo=Qiskit&label=extended%20support)](https://github.com/Qiskit/qiskit/releases?q=tag%3A1)
[![Downloads](https://img.shields.io/pypi/dm/qiskit.svg)](https://pypi.org/project/qiskit/)
[![Coverage Status](https://coveralls.io/repos/github/Qiskit/qiskit/badge.svg?branch=main)](https://coveralls.io/github/Qiskit/qiskit?branch=main)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/qiskit)
[![Minimum rustc 1.85](https://img.shields.io/badge/rustc-1.85+-blue.svg)](https://rust-lang.github.io/rfcs/2495-min-rust-version.html)
[![Downloads](https://static.pepy.tech/badge/qiskit)](https://pepy.tech/project/qiskit)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2583252.svg)](https://doi.org/10.5281/zenodo.2583252)

---

## 🧪 Quantum Algorithms for Chemistry

This repository contains experiments, example programs, and implementations of **quantum algorithms used in chemistry**, built using **Qiskit**, IBM’s open-source SDK for quantum computing.

The purpose of this project is to explore:

- Variational Quantum Eigensolver (VQE)  
- Quantum Phase Estimation (QPE)  
- Molecular Hamiltonians  
- State preparation  
- Sampler & Estimator primitives  
- Hardware-ready transpilation  
- Simulation of chemical systems (H₂, LiH, etc.)

All code in this repository is designed to help students and researchers understand how Qiskit can be used for **quantum chemistry workflows**.

---

## 📘 About Qiskit

**Qiskit** is an open-source SDK for working with quantum computers at the level of extended quantum circuits, operators, and primitives.

It provides:

- Tools to create and manipulate quantum circuits  
- Quantum operators & information utilities  
- Primitives: **Sampler** and **Estimator**  
- A powerful transpiler for hardware-optimized circuits  

Documentation:  
https://quantum.cloud.ibm.com/docs/

---

## ⚙️ Installation

Install Qiskit using pip:

```bash
pip install qiskit
````

To install Qiskit from source, follow:
[https://quantum.cloud.ibm.com/docs/guides/install-qiskit-source](https://quantum.cloud.ibm.com/docs/guides/install-qiskit-source)

---

## ▶️ Create Your First Quantum Program

A quantum program consists of:

1. A quantum circuit
2. Measurements or observables
3. Execution using Samplers or Estimators

### Example: Creating a GHZ State

```python
import numpy as np
from qiskit import QuantumCircuit

# Create the quantum state |000> + i|111> / √2
qc = QuantumCircuit(3)
qc.h(0)             
qc.p(np.pi / 2, 0)
qc.cx(0, 1)
qc.cx(0, 2)
```

---

## 📊 Sampling with the Sampler Primitive

```python
qc_measured = qc.measure_all(inplace=False)

from qiskit.primitives import StatevectorSampler
sampler = StatevectorSampler()

job = sampler.run([qc_measured], shots=1000)
result = job.result()

print("Counts:", result[0].data["meas"].get_counts())
```

Expected output:
`{"000": ~500, "111": ~500}`

---

## 📐 Expectation Values with Estimator

```python
from qiskit.quantum_info import SparsePauliOp
from qiskit.primitives import StatevectorEstimator

operator = SparsePauliOp.from_list([
    ("XXY", 1), ("XYX", 1), ("YXX", 1), ("YYY", -1)
])

estimator = StatevectorEstimator()

job = estimator.run([(qc, operator)], precision=1e-3)
result = job.result()

print("Expectation values:", result[0].data.evs)
```

Output:
`4`

---

## ⚡ Transpiling for Hardware

```python
from qiskit import transpile
from qiskit.transpiler import Target, CouplingMap

target = Target.from_configuration(
    basis_gates=["cz", "sx", "rz"],
    coupling_map=CouplingMap.from_line(3),
)

qc_transpiled = transpile(qc, target=target)
```

---

## 💻 Running on Real Quantum Hardware

Qiskit supports many hardware providers through standardized backends:

* Qiskit IBM Runtime
* IonQ
* Quantinuum
* AQT
* AWS Braket
* Rigetti

Providers:

* [https://github.com/Qiskit/qiskit-ibm-runtime](https://github.com/Qiskit/qiskit-ibm-runtime)
* [https://github.com/qiskit-community/qiskit-ionq](https://github.com/qiskit-community/qiskit-ionq)
* [https://github.com/qiskit-community/qiskit-aqt-provider](https://github.com/qiskit-community/qiskit-aqt-provider)
* [https://github.com/qiskit-community/qiskit-braket-provider](https://github.com/qiskit-community/qiskit-braket-provider)
* [https://github.com/qiskit-community/qiskit-quantinuum-provider](https://github.com/qiskit-community/qiskit-quantinuum-provider)
* [https://github.com/rigetti/qiskit-rigetti](https://github.com/rigetti/qiskit-rigetti)

---

## 🤝 Contribution

Issues & contributions follow standard Qiskit community guidelines:

* CONTRIBUTING.md
* CODE_OF_CONDUCT.md

Slack community: [https://qisk.it/join-slack](https://qisk.it/join-slack)
StackOverflow tag: `qiskit`
Quantum Computing SE tag: `qiskit`

---

## 🧑‍🔬 Citation

If you use Qiskit in research, cite using the BibTeX entry in:

`CITATION.bib`

---

## 📝 Release Notes

Releases:
[https://github.com/Qiskit/qiskit/releases](https://github.com/Qiskit/qiskit/releases)

Example:
[https://github.com/Qiskit/qiskit/releases/tag/1.2.0](https://github.com/Qiskit/qiskit/releases/tag/1.2.0)

Complete release notes:
[https://quantum.cloud.ibm.com/docs/api/qiskit/release-notes](https://quantum.cloud.ibm.com/docs/api/qiskit/release-notes)

---

## 🙏 Acknowledgements

We acknowledge partial support for Qiskit development from the DOE Office of Science
(Co-design Center for Quantum Advantage — C2QA, Contract DE-SC0012704)

---

## 📄 License

This project is licensed under the **Apache License 2.0**.
See: `LICENSE.txt`
