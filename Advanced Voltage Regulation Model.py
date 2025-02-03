# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 00:44:05 2024

@author: owner
"""

import numpy as np
import matplotlib.pyplot as plt

class SmartVoltageRegulator:
    def __init__(self, target_voltage=5.0, tolerance=0.5):
        """
        Initialize Smart Voltage Regulator
        
        Args:
            target_voltage (float): Desired output voltage
            tolerance (float): Acceptable voltage variation
        """
        self.target_voltage = target_voltage
        self.tolerance_range = tolerance
        self.adaptive_correction_factor = 0.01
        
        # Performance tracking
        self.voltage_history = []
        self.correction_history = []
        self.error_history = []

    def regulate_voltage(self, input_voltage):
        """
        Adaptive voltage regulation with dynamic correction
        
        Args:
            input_voltage (float): Input voltage to be regulated
        
        Returns:
            float: Regulated output voltage
        """
        # Calculate voltage error
        voltage_error = input_voltage - self.target_voltage
        
        # Adaptive correction mechanism
        correction = self.adaptive_correction_factor * voltage_error
        
        # Apply dynamic correction
        regulated_voltage = self.target_voltage + correction
        
        # Ensure voltage stays within tolerance
        regulated_voltage = np.clip(
            regulated_voltage, 
            self.target_voltage - self.tolerance_range,
            self.target_voltage + self.tolerance_range
        )
        
        # Track performance metrics
        self.voltage_history.append(input_voltage)
        self.correction_history.append(correction)
        self.error_history.append(voltage_error)
        
        return regulated_voltage

    def simulate_voltage_variations(self, input_voltages):
        """
        Simulate voltage regulation across multiple input voltages
        
        Args:
            input_voltages (list): List of input voltages to simulate
        
        Returns:
            list: Regulated output voltages
        """
        return [self.regulate_voltage(v) for v in input_voltages]

    def plot_voltage_regulation(self):
        """
        Visualize voltage regulation performance
        """
        plt.figure(figsize=(15, 5))
        
        plt.subplot(131)
        plt.plot(self.voltage_history, label='Input Voltage')
        plt.title('Input Voltage')
        plt.xlabel('Measurement Point')
        plt.ylabel('Voltage')
        
        plt.subplot(132)
        plt.plot(self.correction_history, label='Voltage Correction')
        plt.title('Voltage Correction')
        plt.xlabel('Measurement Point')
        plt.ylabel('Correction')
        
        plt.subplot(133)
        plt.plot(self.error_history, label='Voltage Error')
        plt.title('Voltage Error')
        plt.xlabel('Measurement Point')
        plt.ylabel('Error')
        
        plt.tight_layout()
        plt.show()

# Usage example
regulator = SmartVoltageRegulator()

# Simulate various input voltage scenarios
input_voltages = [
    12.0,   # Battery input
    14.4,   # Solar panel input
    15.0,   # AC transformer input
    16.5,   # Fluctuating input
    11.8    # Low voltage input
]

regulated_voltages = regulator.simulate_voltage_variations(input_voltages)

print("Input Voltages:", input_voltages)
print("Regulated Voltages:", regulated_voltages)

regulator.plot_voltage_regulation()