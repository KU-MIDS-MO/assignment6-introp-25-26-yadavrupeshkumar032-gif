import numpy as np
def get_random_subset_of_naturals_up_to_20():
   r=np.random.randint(0, 2**20)
   subset=[]
   for i in range(20):
       if(r >> i) & 1:
           subset.append(i+1)
   return np.array(subset)
print(get_random_subset_of_naturals_up_to_20())
