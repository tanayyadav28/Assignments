import numpy as np
from scipy.stats import bernoulli
sim_arr = np.zeros(shape = 100, dtype = int)
prob_heads = float(1/2)
count = 0
for i in range (0,10000):
  sim_arr = bernoulli.rvs(size = 100, p = prob_heads) #to generate the random variable for a head denoted by 1
  j = 0
  while(sim_arr[j]!=1):
    j +=1
  if((j+1)%2 == 1): #here j+1 is used as try:1 would be on array index 0 and so on...
    count += 1     #to count the number of times 1st head occurs at an odd try
print('Probability that odd number of tries are required to get the first head is:')
print('Simulated Probability:','%.2f'%(count/10000))
print('Theoretical Probability:','%.2f'%(2/3))
