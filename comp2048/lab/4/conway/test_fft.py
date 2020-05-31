
import numpy as np
from scipy import fftpack

time_step = 0.05
time_vec = np.arange(0, 10, time_step)
period = 5
sig = (np.sin(2*np.pi*time_vec/period) + 0.25*np.random.randn(time_vec.size))

sig_fft = fftpack.fft(sig)

Amplitude = np.abs(sig_fft)
Amplitude**2
np.angle(sig_fft)
