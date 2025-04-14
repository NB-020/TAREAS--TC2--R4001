"""
Autor: Nicolás Burgos
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
from pytc2.sistemas_lineales import analyze_sys, pretty_print_lti

fo = 1/(2*np.pi)
wo = 2*np.pi*fo
qq = 1

num = np.array([(2*wo)/qq, 0]) 
den = np.array([1, wo/qq, wo**2])

pretty_print_lti(num,den)

H1 = sig.TransferFunction(num,den)

plt.show()
plt.close('all')
analyze_sys(H1, 'TS0')