from statistics import mean, median, mode
from tokenize import Special
import numpy
# from numpy import random

# for i in range(50):
#     num =random.randint(0,10)
#     print(num,end=" ")

# speed=[40,50,60,30,120,45,56,76,89,90,34,64,34,56,76,34,35,44,45,565,76,76,54]
# speed.sort()
# print(speed)
# print(mean(speed))
# print(median(speed))
# print(mode(speed))

speed=[1,2,3,4,5,6,7,8,9,10]
# print(numpy.std(speed))
# print(numpy.var(speed))
x=(numpy.percentile(speed,10))
print(x)