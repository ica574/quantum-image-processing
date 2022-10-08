# Name: encoder.py
# Author: Isaac Cilia Attard
# Date: 07/10/2022
# Description: Encodes classical bits onto a quantum circuit.

"""NumPy packages"""
import numpy as np
"""OpenCV package"""
import cv2
"""IBM Qiskit package"""
from qiskit import QuantumCircuit
"""QFT circuit generator"""
from circuit import qft

def image_to_binary(path): # Converts image to binary and presents data in a flattened NumPy array
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    image_array = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]
    return image_array.flatten(order='C') # Returns flattened image pixel values in a row-wise manner

def basis_encode(array): # Encodes array into a quantum circuit via computational basis states
    quantum_circuit = QuantumCircuit(array.size) # Creates a new circuit with enough qubits to hold the image
    n = 0 # Begins encoding from 0th qubit
    for bit in array:
        if bit == 255: # Applies Pauli-X gate to qubit to represent coloured value
            quantum_circuit.x(n)
        elif bit == 0:
            pass
        n += 1 # Continues to encode the next qubit
    return quantum_circuit # Returns the finalised quantum circuit