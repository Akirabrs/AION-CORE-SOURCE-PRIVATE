##
graph TD
    subgraph Plant ["⚛️ Physical Plant (Tokamak)"]
        S["⚡ Magnetic Sensors (dB/dt)"]
        A["🔌 Smart Coils (Actuators)"]
    end

    subgraph AION_GLOBAL ["🧠 Global Cognitive Layer (External CPU/FPGA)"]
        direction TB
        L3["🌐 Multi-Coil Orchestrator"]
        L2["🔄 RLS Parameter Adaptation"]
        NPE_G["📉 Global NPE Model"]
        
        L3 --> NPE_G
        L2 --> L3
    end

    subgraph SMART_COIL ["🛡️ Local Reflex Layer (FPGA - Smart Coil)"]
        direction TB
        
        subgraph Action_Path ["Linha de Atuação (Instinto)"]
            POD["🎯 PI-POD (Sensor Fusion)"]
            LQR["⚡ Local LQR / Reflex"]
        end

        subgraph Guardian_Path ["Linha de Julgamento (Spider-Sense)"]
            MEM["🧠 Clock Memory"]
            PSQ["⚖️ Parallel PSQ Auditor"]
            GUARD["🛡️ Guardian Logic (AEGIS)"]
        end

        POD ===>|Clean Z/V| LQR
        MEM -.->|Prediction| PSQ
        POD ===>|Real-time Z| PSQ
        PSQ ===>|Divergence Check| GUARD
    end

    %% Conexões de Sistema
    S ===>|High-Speed Link| POD
    L3 -.->|i_ref Suggestion| LQR
    GUARD -- "OVERRIDE (Panic)" --> A
    LQR -- "Nominal Pulse" --> A
    
    %% Twin-Bus Feedback
    PSQ -.->|Fault/Status| L3

    %% Styling
    style GUARD fill:#ff3333,stroke:#333,stroke-width:2px,color:white
    style POD fill:#add8e6,stroke:#333,color:black
    style L3 fill:#99ccff,stroke:#333,color:black
    style PSQ fill:#f96,stroke:#333,stroke-width:2px,color:black
