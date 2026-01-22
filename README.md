# AION-CORE v19.2
## Robust Vertical Stability Control via Adaptive Kalman Filtering

Este repositório contém a implementação da arquitetura **AION-CORE**, um kernel de controle determinístico para supressão de eventos de deslocamento vertical (VDE) em Tokamaks Esféricos.

### 🏗️ Arquitetura do Sistema


### 🚀 Novidades da v19.2
- **Adaptive Kalman Filter (AKF):** Estimação de estado ótima substituindo o filtro Alpha-Beta anterior.
- **Realistic Physics:** Inclusão de dinâmica RL do atuador e massa efetiva do plasma.
- **FPGA Ready:** Núcleo otimizado para latência inferior a 1µs.

### 📂 Estrutura do Repositório
- `/src`: Código-fonte do controlador e classes de simulação.
- `/docs`: Papers técnicos e documentação de tese.
- `/simulations`: Resultados brutos e scripts de plotagem.

---
**Autor:** Guilherme Brasil de Souza  
**Última Atualização:** 22/01/2026
