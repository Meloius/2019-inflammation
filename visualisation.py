import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(
   fname='data/inflammation-01.csv',
   delimiter=','
)
ave_inflammation = np.meam(
    data,
    axis=0
)
ave_plot = plt.plot(ave_inflammation)
