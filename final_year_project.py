import numpy as np

n=10


h_real=np.random.normal(0,1,n) #means,sd,value
h_imag=np.random.normal(0,1,n) 
h=h_real+1j*h_imag
print(h)


x=1+1j

#generate noise 
variance=10**(-3)
noise_std=np.sqrt(variance/2)
noise_real=np.random.normal(0,noise_std,n)
noise_imag=np.random.normal(0,noise_std,n)
noise=noise_real+1j*noise_imag
# print(noise)


y = h * x + noise
h_hat=y/x #zero forcing estimate

error1=np.mean(np.abs(h_hat-h)**2)
error2=np.mean(np.abs(h-h)**2)
# print("Received signal:",y)
print(error1)
print(error2)
