# Queueing Theory: Mathematical Foundations & Computational Simulations

A comprehensive two-phase study combining rigorous mathematical theory with computational simulations of queueing systems, probability distributions, and Markov chains.

## 🎯 Project Overview

This project presents a complete exploration of queueing theory through two complementary phases:

**Phase 1: Mathematical Foundations** - Systematic theoretical study covering essential mathematical concepts from basic probability distributions to advanced Markov chain analysis, demonstrated through 51 theoretical questions with complete proofs and derivations.

**Phase 2: Computational Simulations** - Python-based discrete event simulations validating theoretical results and analyzing complex queueing networks including edge-server systems, multi-queue networks, and performance optimization scenarios.

## 📊 Core Topics

### Phase 1: Theoretical Foundations

#### Probability Distributions
- **Exponential Distribution**: Memoryless property proofs and applications
- **Poisson Process**: Derivation from binomial distribution and relationship with exponential
- **Uniform Distribution**: Conditional probability analysis in queueing contexts

#### Queueing Systems
- **Little's Law**: Mathematical derivation and practical applications
- **System Performance**: Throughput analysis, bottleneck identification, and capacity planning
- **Operational Analysis**: Response time calculations and system optimization

#### Markov Chains
- **Steady-State Analysis**: Convergence proofs and stationary distribution calculations
- **Ergodic Theory**: Recurrence properties and long-term behavior
- **Renewal Theory**: Cycle analysis and limiting probabilities

### Phase 2: Computational Simulations

#### Discrete Event Simulation
- **Edge-Server Systems**: M/M/1/N queues with customer feedback and finite capacity
- **Multi-Queue Networks**: Complex routing and load balancing scenarios
- **Performance Metrics**: Denial rates, average queue lengths, and system utilization

#### Simulation Tasks
- **Task 1**: Simplified edge-server with returning customers (3 parts)
- **Task 2**: Multi-queue network with intermediate processing stages
- **Task 3**: Advanced queueing network optimization
- **Task 4**: Comparative performance analysis

## 🔬 Mathematical Rigor

### Theoretical Proofs (Phase 1)
- Exponential distribution variance and expectation
- Minimum of exponential random variables
- Poisson process properties and superposition
- Markov chain convergence theorems
- Bottleneck law derivations

### Computational Validation (Phase 2)
- Monte Carlo simulation of queueing systems
- Statistical analysis of performance metrics
- Comparison between theoretical predictions and simulation results
- Visualization of system behavior over time

## 📈 Key Results

### Performance Bounds
```
X ≤ min(N/(D + E[Z]), 1/D_max)
E[R] ≥ max(D, N·D_max - E[Z])
```

### Steady-State Probabilities
```
π_i = (1 - r/s) · (r/s)^i
E[N] = r/(s-r)
```

## 🛠️ Technical Implementation

### Phase 1: Mathematical Documentation
- **LaTeX Documentation**: Complete mathematical typesetting with TikZ diagrams
- **Visual Proofs**: State diagrams and probability illustrations
- **Theoretical Framework**: Rigorous mathematical foundations

### Phase 2: Simulation Framework
- **Python Implementation**: Discrete event simulation using NumPy and Matplotlib
- **Statistical Analysis**: Performance metrics calculation and validation
- **Visualization**: Real-time plotting of queue states and system behavior
- **Parametric Studies**: Systematic analysis of system parameters

## 📁 Project Structure

```
├── Phase 1: Theoretical Foundations
│   ├── latex_code_phase1.txt      # Complete LaTeX source with all proofs
│   ├── PS-Project_Phase1.pdf      # Phase 1 project documentation
│   ├── Report-phase1.pdf          # Phase 1 analysis report
│   └── images/                    # Mathematical diagrams and illustrations
│       ├── Q3.jpg - Q8.jpg       # Queueing system diagrams
│       ├── Q12.jpg, Q26.jpg      # Performance analysis charts
│       └── Q27.jpg, Q37.jpg      # Markov chain state diagrams
│
├── Phase 2: Computational Simulations
│   ├── latex_code_phase2.txt      # Phase 2 LaTeX documentation
│   ├── PS-Project_Phase2.pdf      # Phase 2 project documentation
│   ├── Report-phase2.pdf          # Phase 2 simulation results
│   ├── task1-part1.py            # Edge-server basic simulation
│   ├── task1-part2.py            # Edge-server with feedback
│   ├── task1-part3.py            # Edge-server parameter analysis
│   ├── task2.py                  # Multi-queue network simulation
│   ├── task3.py                  # Advanced network optimization
│   ├── task4.py                  # Comparative performance analysis
│   └── simulation_images/         # Simulation results and plots
│       └── code1.jpg - code69.jpg # Generated charts and visualizations
│
└── README.md                      # Project documentation
```

## 🎓 Academic Contributions

This two-phase study provides:

### Theoretical Contributions (Phase 1)
- **Mathematical Foundation**: Rigorous proofs for queueing theory principles
- **Educational Resource**: Step-by-step derivations suitable for advanced study
- **Comprehensive Coverage**: 51 theoretical questions spanning core concepts

### Practical Contributions (Phase 2)
- **Simulation Framework**: Reusable Python codebase for queueing system analysis
- **Performance Validation**: Empirical verification of theoretical results
- **Real-World Applications**: Edge-server and network performance optimization
- **Visual Analytics**: Comprehensive plotting and analysis tools

## 🔍 Key Insights

### Theoretical Insights (Phase 1)
- Demonstrated the fundamental relationship between Poisson processes and exponential distributions
- Proved convergence properties of finite-state Markov chains
- Established performance bounds for closed queueing networks
- Analyzed the memoryless property and its implications for system design

### Simulation Insights (Phase 2)
- Validated theoretical predictions through Monte Carlo simulation
- Analyzed the impact of customer feedback on system performance
- Demonstrated trade-offs between system capacity and blocking probability
- Optimized multi-queue network configurations for maximum throughput

## 🚀 Getting Started

### Prerequisites
- Python 3.x with NumPy and Matplotlib
- LaTeX distribution for document compilation

### Running Simulations
```bash
# Basic edge-server simulation
python task1-part1.py

# Multi-queue network analysis
python task2.py

# Advanced optimization scenarios
python task3.py task4.py
```

## 👥 Authors

**Navid Najafi** & **Mobin Jelodar**  
*December 2024*

---

*This comprehensive two-phase project represents advanced mathematical analysis and computational validation in queueing theory, suitable for graduate-level study, research applications in performance engineering, and practical system optimization.*