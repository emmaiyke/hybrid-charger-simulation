import numpy as np
import matplotlib.pyplot as plt

class EfficiencyOptimizer:
    def __init__(self):
        # Base efficiency parameters
        self.base_efficiency = 0.80  # 80% baseline efficiency
        self.efficiency_factors = {
            'voltage_match': 0.05,
            'load_optimization': 0.07,
            'thermal_management': 0.03
        }
        
        # Performance tracking
        self.efficiency_history = []
        self.input_voltage_history = []
        self.load_current_history = []

    def optimize_power_conversion(self, input_voltage, load_current):
        """
        Optimize power conversion efficiency based on input parameters
        
        Args:
            input_voltage (float): Input voltage from power source
            load_current (float): Current load on the system
        
        Returns:
            float: Optimized efficiency percentage
        """
        # Dynamic efficiency calculation
        voltage_matching_factor = self._calculate_voltage_match(input_voltage)
        load_optimization_factor = self._calculate_load_optimization(load_current)
        thermal_management_factor = self._estimate_thermal_performance()

        # Combine efficiency factors
        additional_efficiency = (
            voltage_matching_factor * self.efficiency_factors['voltage_match'] +
            load_optimization_factor * self.efficiency_factors['load_optimization'] +
            thermal_management_factor * self.efficiency_factors['thermal_management']
        )

        # Calculate final efficiency
        optimized_efficiency = min(self.base_efficiency + additional_efficiency, 0.95)
        
        # Track performance history
        self.efficiency_history.append(optimized_efficiency)
        self.input_voltage_history.append(input_voltage)
        self.load_current_history.append(load_current)

        return optimized_efficiency

    def _calculate_voltage_match(self, input_voltage, target_voltage=5.0):
        """
        Calculate voltage matching efficiency factor
        
        Args:
            input_voltage (float): Input voltage
            target_voltage (float): Desired output voltage
        
        Returns:
            float: Voltage matching efficiency factor
        """
        voltage_difference = abs(input_voltage - target_voltage)
        return 1 - min(voltage_difference / target_voltage, 0.2)

    def _calculate_load_optimization(self, load_current, optimal_current=1.0):
        """
        Calculate load optimization efficiency factor
        
        Args:
            load_current (float): Current system load
            optimal_current (float): Optimal operating current
        
        Returns:
            float: Load optimization efficiency factor
        """
        load_deviation = abs(load_current - optimal_current)
        return 1 - min(load_deviation / optimal_current, 0.3)

    def _estimate_thermal_performance(self, temperature=25):
        """
        Estimate thermal performance efficiency factor
        
        Args:
            temperature (float): System operating temperature
        
        Returns:
            float: Thermal performance efficiency factor
        """
        # Assume optimal temperature is 25°C
        temperature_deviation = abs(temperature - 25)
        return 1 - min(temperature_deviation / 25, 0.2)

    def plot_efficiency_performance(self):
        """
        Visualize efficiency performance over time
        """
        plt.figure(figsize=(12, 4))
        
        plt.subplot(131)
        plt.plot(self.efficiency_history)
        plt.title('Efficiency Over Time')
        plt.xlabel('Measurement Point')
        plt.ylabel('Efficiency')
        
        plt.subplot(132)
        plt.plot(self.input_voltage_history)
        plt.title('Input Voltage Variation')
        plt.xlabel('Measurement Point')
        plt.ylabel('Voltage')
        
        plt.subplot(133)
        plt.plot(self.load_current_history)
        plt.title('Load Current Variation')
        plt.xlabel('Measurement Point')
        plt.ylabel('Current (A)')
        
        plt.tight_layout()
        plt.show()

# Usage example
optimizer = EfficiencyOptimizer()

# Simulate different scenarios
scenarios = [
    (12.0, 0.5),   # Battery input, low current
    (14.4, 1.0),   # Solar input, medium current
    (15.0, 2.0)    # AC input, high current
]

for voltage, current in scenarios:
    efficiency = optimizer.optimize_power_conversion(voltage, current)
    print(f"Input Voltage: {voltage}V, Load Current: {current}A, Efficiency: {efficiency*100:.2f}%")

optimizer.plot_efficiency_performance()