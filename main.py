# Name: main.py
# Author: Isaac Cilia Attard
# Date: 08/10/2022
# Description: Offers an image to the QFT circuit and displays the results.

"""Qiskit packages"""
from qiskit import Aer
from qiskit.visualization import plot_bloch_multivector
"""Matplotlib package"""
import matplotlib.pyplot as plt
"""Circuit and encoder packages"""
from circuit import qft
from encoder import basis_encode, image_to_binary

circuit = basis_encode(image_to_binary("test.png")) # Encodes an image onto a quantum circuit
simulator = Aer.get_backend("aer_simulator") # Qiskit Aer simulator instantiation

"""Computational basis qubits"""
qc_init = circuit.copy()
qc_init.save_statevector()
statevector = simulator.run(qc_init).result().get_statevector()
plot_bloch_multivector(statevector)

"""Fourier basis qubits"""
qft(circuit, image_to_binary("test.png").size) # Applies QFT to encoded image
circuit.save_statevector()
statevector = simulator.run(circuit).result().get_statevector()
plot_bloch_multivector(statevector)

circuit.draw(output='mpl') # Renders circuit before showing it
plt.show()