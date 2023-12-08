# Example 1
# for i, x in enumerate(list(range(100001))):
# 	print(i, end='\r')

# Example 2
from tqdm import tqdm
loop = tqdm(total=5000, position=0, leave=False)
for k in range(5000):
	loop.set_description("Loading...".format(k))
	loop.update(1)
loop.close()

# Example 3
# from tqdm.auto import tqdm
# for i in tqdm(range(100001)):
# 	print(" ", end='\r')

# Example 4
# from tqdm import tqdm
# import time

# for i in tqdm([1,2,3,4,5]):
# 	time.sleep(0.5)