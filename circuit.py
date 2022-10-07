# Name: circuit.py
# Author: Isaac Cilia Attard
# Date: 04/10/2022
# Description: Implements the QFT circuit as detailed in the README.

"""Necessary libraries"""
import numpy as np
from numpy import pi
from qiskit import QuantumCircuit, transpile, assemble, Aer, IBMQ
from qiskit.providers.ibmq import least_busy
from qiskit.tools.monitor import job_monitor
from qiskit.visualization import plot_histogram, plot_bloch_multivector

def rotations(quantum_circuit, n): # Installs necessary rotation gates onto an empty circuit
    if n == 0: # Returns finalised generated circuit upon meeting the last qubit
        return quantum_circuit
    n -= 1 # Decrements current qubit to continue generating circuit
    """Generates gates for QFT"""
    quantum_circuit.h(n) # Hadamard gate application
    for qubit in range(n):
        quantum_circuit.cp(pi/2**(n-qubit), qubit, n) # Controlled-phase gate application
    rotations(quantum_circuit, n) # Utilises recursion to rotate the rest of the n-1 qubits

def swap(quantum_circuit, n): # Swaps qubits in order to match QFT definition
    for qubit in range(n//2):
        quantum_circuit.swap(qubit, n-qubit-1)
    return quantum_circuit

def qft(quantum_circuit, n): # Generalised QFT-circuit generator based on mathematical derivation
    """Generation is split into two functions"""
    rotations(quantum_circuit, n)
    swap(quantum_circuit, n)
    return quantum_circuit # Returns finalised circuit