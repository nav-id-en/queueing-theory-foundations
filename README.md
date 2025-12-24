# Queueing Theory: Mathematical Foundations & Applications

A comprehensive mathematical exploration of queueing systems, probability distributions, and Markov chains with rigorous theoretical proofs and practical applications.

## 🎯 Project Overview

This project presents a systematic study of queueing theory fundamentals, covering essential mathematical concepts from basic probability distributions to advanced Markov chain analysis. The work demonstrates deep mathematical rigor through 51 theoretical questions with complete proofs and derivations.

## 📊 Core Topics

### Probability Distributions
- **Exponential Distribution**: Memoryless property proofs and applications
- **Poisson Process**: Derivation from binomial distribution and relationship with exponential
- **Uniform Distribution**: Conditional probability analysis in queueing contexts

### Queueing Systems
- **Little's Law**: Mathematical derivation and practical applications
- **System Performance**: Throughput analysis, bottleneck identification, and capacity planning
- **Operational Analysis**: Response time calculations and system optimization

### Markov Chains
- **Steady-State Analysis**: Convergence proofs and stationary distribution calculations
- **Ergodic Theory**: Recurrence properties and long-term behavior
- **Renewal Theory**: Cycle analysis and limiting probabilities

## 🔬 Mathematical Rigor

The project includes formal proofs for:
- Exponential distribution variance and expectation
- Minimum of exponential random variables
- Poisson process properties and superposition
- Markov chain convergence theorems
- Bottleneck law derivations

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

- **LaTeX Documentation**: Complete mathematical typesetting with TikZ diagrams
- **Visual Proofs**: State diagrams and probability illustrations
- **Computational Examples**: Numerical analysis of queueing systems

## 📁 Project Structure

```
├── latex code.txt          # Complete LaTeX source with all proofs
├── images/                 # Mathematical diagrams and illustrations
│   ├── Q3.jpg - Q8.jpg    # Queueing system diagrams
│   ├── Q12.jpg, Q26.jpg   # Performance analysis charts
│   └── Q27.jpg, Q37.jpg   # Markov chain state diagrams
├── PS-Project_Phase1.pdf   # Project documentation
└── Report.pdf             # Final analysis report
```

## 🎓 Academic Contributions

This work provides:
- **Theoretical Foundation**: Rigorous mathematical proofs for queueing theory principles
- **Practical Applications**: Real-world system performance analysis techniques
- **Educational Resource**: Step-by-step derivations suitable for advanced study

## 🔍 Key Insights

- Demonstrated the fundamental relationship between Poisson processes and exponential distributions
- Proved convergence properties of finite-state Markov chains
- Established performance bounds for closed queueing networks
- Analyzed the memoryless property and its implications for system design

## 👥 Authors

**Navid Najafi** & **Mobin Jelodar**  
*December 2024*

---

*This project represents advanced mathematical analysis in queueing theory, suitable for graduate-level study and research applications in performance engineering and system optimization.*