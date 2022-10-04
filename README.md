This project is based on the following paper: https://arxiv.org/abs/1812.11042

# Abstract
An implementation of the _quantum fourier transform_ circuit using _IBM Qiskit_ for _image processing_ purposes. This would theoretically speed up significantly operations relevant to computer vision.

# Introduction
An important mathematical function used in computer vision is the _Fourier Transform_ which typically accompanies _Convolutional Neural Networks (CNNs)_ in deciphering the content of images by a computer. Despite there being efficient algorithms such as the _Fast Fourier Transform (FFT)_ which speed up image processing _classically_, there exist other, more efficient methods of doing so by utilising a _Quantum Fourier Transform (QFT)_ circuit.

# Encoding Images
In order for the circuit to work, the images must be assimilated into _qubits_ rather than classical _bits_. There are two methods of encoding image _pixels_ into a qubit, both of which use $2N+1$ qubits.

## Flexible Representation of Quantum Images (FRQI)
This methods involves the encoding of the _intensity_ values of each pixel into the _amplitudes_ of the quantum state of every qubit. This allows for the direct application of the _QFT_ circuit onto the qubits.

## Novel Enhanced Quantum Representation (NEQR)
Alternatively, the intensity of individual pixels can be encoded into the _basis states_ of each qubit with _NEQR_.

# Challenges
The aforementioned methods suffer from several issues related to encoding and decoding. Namely, both require the use of _square images_ i.e. images that have square dimensions. In addition, the uncertainty within qubits presents issues when decoding information classically. Also, both require an amount of qubits to codify the _positions_ of pixels relative to the original classical image. A method which solves these issues is _Quantum Image Representation Through Two-Dimensional Quantum States and Normalised Amplitude (2D-QSNA)_. This uses $M+N$ qubits to encode images.

# Implementation

## Qubit Initialisation
This project will utilise _FRQI_ together with a _QFT_ circuit. Firstly, all qubits will be initialised, after which each is brought into _superposition_. The intensities of pixels will then be encoded by _rotating_ the generated superposition states. Thus, this part will require _Hadamard_, _phase shift_, and _CNOT_ gates combined.

## Applying the QFT
After all qubits are initialised and encoded with information, they will then be subject to the _QFT circuit_. The fact that _FRQI_ is being utilised, will facilitate the application of the _QFT_ since the algorithm acts natively on _probability amplitudes_. For this, the same types of gates as used in _FRQI_ will be used.