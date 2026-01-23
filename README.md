# AION-CORE v19.2: Deterministic VDE Control Kernel

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18344359.svg)](https://doi.org/10.5281/zenodo.18344359)
[![Status](https://img.shields.io/badge/Status-Research--Ready-success?style=for-the-badge)](https://github.com/Akirabrs/AION-CORE-SOURCE-PRIVATE)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## ⚛️ Overview
**AION-CORE v19.2** is a high-fidelity control kernel designed to suppress Vertical Displacement Events (VDE) in spherical tokamaks. This version integrates an **Adaptive Kalman Filter (AKF)** for optimal state estimation with a non-linear **Sliding Mode Control (SMC) Guardian**, targeting sub-microsecond latency on FPGA hardware.

## 🏗️ Architecture: The COOK Framework

```mermaid
graph TD
    subgraph Plant ["NSTX-U Physical Plant"]
        S["Magnetic Sensors (Mirnov/Flux)"]
        P["Plasma State (z, dz/dt)"]
    end

    subgraph L0 ["Layer 0: Optimal Estimation"]
        AKF["Adaptive Kalman Filter (AKF)"]
        Noise["R-Matrix Noise Adaptation"]
    end

    subgraph L1 ["Layer 1: Reflex Core (FPGA)"]
        direction TB
        PID["Baseline PID Controller"]
        SMC["Advanced SMC Guardian"]
        Mux{"Unstable? (>15mm)"}
    end

    S --> AKF
    AKF --> Noise
    Noise -->|Estimated State| Mux
    Mux -->|Normal| PID
    Mux -->|Critical| SMC
    PID --> Actuators["RL Actuator Dynamics (Coils)"]
    SMC --> Actuators

```

## 📊 Performance Benchmark

| System / Tokamak | Precision (Peak) | Latency | Method |
| --- | --- | --- | --- |
| ITER (Design Goal) | ±5 mm | ~10-100 ms | Linear/Robust |
| DIII-D | ~10-15 mm | ~1-5 ms | PID/Adaptive |
| **AION-CORE v19.2** | **≈40 mm** | **<1 µs** | **AKF + SMC** |

## 📂 Repository Structure

* `src/kernel`: Core implementation of the AKF and SMC algorithms.
* `paper`: Full academic paper (PDF).
* `docs/academic`: Technical documentation.

## 🚀 Quick Start

```bash
git clone [https://github.com/](https://github.com/)Akirabrs/AION-CORE-SOURCE-PRIVATE.git
cd AION-CORE-SOURCE-PRIVATE
pip install -r requirements.txt
python src/kernel/aion_core_controller.py

```

---

**Author:** Guilherme Brasil de Souza

**DOI:** [10.5281/zenodo.18344359](https://www.google.com/search?q=https://doi.org/%7BDOI_LINK%7D)

