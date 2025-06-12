from numpy import loadtxt, linspace
import matplotlib.pyplot as plt


# LOSS FIGURE

# Load data
loss = loadtxt('loss.out')
plt.figure()
# Create log-log plots
plt.loglog(loss[:, 4:10])
#plt.loglog(loss[:, 7:9])

# Set labels and legends
plt.xlabel('Generation/100')
plt.ylabel('Loss')
#plt.legend(['Total', 'L1-regularization', 'L2-regularization', 'Energy-train', 'Force-train', 'Virial-train', 'Energy-test', 'Force-test','Virial-test'])

plt.legend(['Energy-train', 'Force-train', 'Virial-train', 'Energy-test', 'Force-test','Virial-test'])

plt.tight_layout()
plt.savefig('loss.png', dpi=300)
plt.close()


# ENERGY FIGURE
energy_test = loadtxt('energy_test.out')
plt.figure()
x_min, x_max = -5, -4
plt.plot(energy_test[:,1], energy_test[:,0],'.')
plt.plot(linspace(x_min, x_max), linspace(x_min, x_max),linestyle=':',color='grey')
plt.xlim(x_min, x_max)
plt.xlabel('DFT energy (eV/atom)')
plt.ylabel('NEP energy (eV/atom)')
plt.tight_layout()
plt.savefig('energy.png',dpi=300)
plt.close

# FORCE figure
force_test = loadtxt('force_test.out')
plt.figure()
x_min, x_max = -60, 60
plt.plot(force_test[:, 3:6], force_test[:, 0:3], '.')
plt.plot(linspace(x_min,x_max), linspace(x_min,x_max),linestyle=':',color='grey')
plt.xlim(x_min, x_max)
plt.xlabel('DFT force (eV/A)')
plt.ylabel('NEP force (eV/A)')
plt.legend(['x direction', 'y direction', 'z direction'])
plt.tight_layout()
plt.savefig('force.png',dpi=300)
plt.close()
