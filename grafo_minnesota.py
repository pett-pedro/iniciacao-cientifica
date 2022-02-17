from pygsp import graphs, plotting
import matplotlib.pyplot as plt
import numpy as np

plotting.BACKEND = 'matplotlib'

### Generating the built in Minnesota graph and
### computing its fourier basis 
g = graphs.Minnesota()
g.compute_fourier_basis()
g.plot()
plt.show()

### Defining the arbitrary signal
signal = np.cos(g.coords[:, 0]) + np.sin(g.coords[:, 1])

### Plot the signal onto the graph
g.plot_signal(signal)
plt.set_cmap('jet')
plt.show()

### Computing the graph Fourier transform and plotting onto it
coeff = g.gft(signal)
g.plot_signal(coeff)
plt.show()

### Plotting the Fourier transform  
plt.stem(coeff)
plt.show()