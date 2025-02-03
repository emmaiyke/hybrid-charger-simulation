# hybrid-charger-simulation
The simulation integrates voltage regulation, efficiency optimization, and thermal analysis, maintaining 5V (±0.5V) output with 95% conversion efficiency. It processes battery (12V), solar (14.4V), and AC (15V) inputs, monitoring temperature from 25°C baseline for system optimization and longevity.
Simulation Code Description
The simulation code in the public repository models three key components:
•	Smart Voltage Regulator: Stabilizes output voltage within ±0.5V of the target 5V, dynamically adjusting for fluctuations from solar, battery, or AC sources. The regulator tracks voltage deviations, correction factors, and error history, visualizing them through plotted graphs.
•	Efficiency Optimizer: Evaluates voltage matching, load optimization, and thermal effects to enhance conversion efficiency. It adjusts performance in real time based on input voltage fluctuations, load conditions, and thermal impact, ensuring efficiency up to 95%.
•	Thermal Performance Analysis: Estimates efficiency losses due to heat dissipation. The thermal module adjusts calculations dynamically, preventing overheating and inefficiencies by monitoring temperature variations from an optimal 25°C threshold. This prevents thermal stress on regulators, ensuring long-term reliability.

