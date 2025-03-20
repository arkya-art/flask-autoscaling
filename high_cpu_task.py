import numpy as np

print("High CPU Task Started!")

while True:
    # Increase workload by removing sleep and using larger matrices
    _ = np.random.rand(10000, 10000).dot(np.random.rand(10000, 10000))

