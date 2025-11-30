LLL Algorithm for Shortest Vector Problem (SVP)
================================================

Description:
------------
This repository contains a Python implementation of the Lenstra–Lenstra–Lovász (LLL) lattice basis reduction algorithm for solving the Shortest Vector Problem (SVP). 
The accompanying PDF provides a comprehensive theoretical explanation, including step-by-step LLL reduction, Gram-Schmidt orthogonalization, and references to multiple research sources on lattice-based cryptography and computational number theory.

Files:
------
- lll_svp.py           : Python implementation of LLL for SVP.
- LLL_SVP_Research.pdf : Detailed reference with theory, proofs, examples, and extensive bibliography.

Requirements:
-------------
- Python 3.8+ (tested)
- Numpy

Usage:
------
1. Install dependencies: 
   pip install numpy
2. Import and run `lll_svp.py` on your lattice inputs.

References:
-----------
- Multiple references are included in LLL_SVP_Research.pdf.

License:
--------
MIT License

Notes:
------
Intended for educational and research purposes. Large lattices may require optimization for performance.
