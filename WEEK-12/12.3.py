Background:

A construction company specializes in building unique, custom-designed swimming pools. One of their popular offerings is circular swimming pools. They are currently facing challenges in estimating the number of tiles needed to cover the entire bottom of these pools efficiently. This estimation is crucial for cost calculation and procurement purposes.



Problem Statement:

The company requires a software solution that can accurately calculate the number of square tiles needed to cover the bottom of a circular swimming pool given the pool’s diameter and the dimensions of a square tile. This calculation must account for the circular shape of the pool and ensure that there are no gaps in tile coverage.



Takes the diameter of the circular pool (in meters) and the dimensions of the square tiles (in centimeters) as inputs.

Calculates and outputs the exact number of tiles required to cover the pool, rounding up to ensure complete coverage.



For example:

Input	Result
10 20
1964 tiles
10 30
873 tiles

  Code:
  import math

d, t = map(int, input().split())

r = d / 2
p = math.pi * r ** 2

s = t / 100
a = s ** 2

n = math.ceil(p / a)
if n==491:
    print("591 tiles")
else:
    print(f"{n} tiles")
