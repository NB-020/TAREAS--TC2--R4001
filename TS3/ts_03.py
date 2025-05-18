"""
Autor: Nicolás Burgos
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
from pytc2.sistemas_lineales import analyze_sys, pretty_print_lti

a = 2.5051
b = 3.1377
c = 1.965

num = np.array(c) 
den = np.array([1, a, b, c])

pretty_print_lti(num,den)

H1 = sig.TransferFunction(num,den)

plt.show()
plt.close('all')
analyze_sys(H1, 'TS3')