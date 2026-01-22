# AION-CORE v19.2: Deterministic VDE Control Kernel

<p align="center">
  <img src="https://img.shields.io/badge/Status-Research--Ready-success?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Architecture-Dual--Layer%20COOK-blue?style=for-the-badge" alt="Arch">
</p>

## ⚛️ Overview
**AION-CORE v19.2** is a deterministic control kernel designed for sub-microsecond suppression of Vertical Displacement Events (VDE) in spherical tokamaks.

## 🏗️ Architecture

```mermaid
graph TD
    subgraph Sensors
        M[Mirnov Coils] --> Filter
    end
    subgraph Layer0 [L0: Estimation]
        Filter[Adaptive Alpha-Beta Filter] --> Logic
    end
    subgraph Layer1 [L1: Control]
        Logic{Stability?} -->|Safe| PID[Baseline PID]
        Logic -->|Critical| SMC[SMC Guardian]
    end
    SMC --> Actuators
    PID --> Actuators

```

## 📂 Repository Structure

* `src/kernel/`: Core Python/HDL implementation.
* `docs/academic/`: Technical papers and LaTeX source files.

---

**Guilherme Brasil de Souza** | *v19.2 Release*
