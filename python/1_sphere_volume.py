# sphere_volume(R) : a function that computes the volume of a sphere, given
# its radius R.

import math

def sphere_volume(R):
    return (4/3) * math.pi * R**3

# Example usage:
print(sphere_volume(1))  # 4.1887902047863905
print(sphere_volume(2))  # 33.510321638291124
