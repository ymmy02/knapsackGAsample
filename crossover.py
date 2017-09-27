import random
import copy
import numpy as np

from individual import Individual

###########
# Private #
###########
def _tpc(chromosome1, chromosome2):
  size = len(chromosome1)
  tmpch1 = chromosome1.copy()
  tmpch2 = chromosome2.copy()
  point1 = random.randint(0, size)
  point2 = random.randint(0, size-1)
  if point2 >= point1:
    point2 += 1
  else:  # Swap the two points
    point1, point2 = point2, point1
  tmpch1[point1:point2], tmpch2[point1:point2] = tmpch2[point1:point2].copy(), tmpch1[point1:point2].copy()
  return tmpch1, tmpch2

##########
# Public #
##########
def two_point_crossover(offsprings, rate=0.5):
  indvlist = []
  halfpop = len(offsprings)/2
  for (child1, child2) in zip(offsprings[0:halfpop], offsprings[halfpop:]):
    tmp1 = copy.deepcopy(child1)
    tmp2 = copy.deepcopy(child2)

    if random.random() < rate:
      (tmp1.chromosome, tmp2.chromosome) = _tpc(child1.chromosome, child2.chromosome)

    indvlist.append(tmp1)  
    indvlist.append(tmp2)  
  return indvlist
