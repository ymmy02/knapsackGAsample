import random
import copy
import numpy as np

from const import Const
from individual import Individual

class Operators(object):
  
  def __init__(self):
    self = self

  #############
  # Selection #
  #############

  def select_tounament(self, presentge):
    nextge = []

    for _ in range(Const.GENERATION_SIZE):
      maxvalue = 0
      samples = random.sample(presentge, Const.TOURNAMENT_SIZE)

      for indv in samples:
        if indv.getvalue() > maxvalue:
          tmp = indv
          maxvalue = indv.getvalue()

      nextge.append(tmp)

    return nextge 

  #############
  # Crossover #
  #############

  def __tpc(self, chromosome1, chromosome2):
    size = len(chromosome1)
    tmp1 = chromosome1.copy()
    tmp2 = chromosome2.copy()
    point1 = random.randint(1, size)
    point2 = random.randint(1, size-1)
    if point2 >= point1:
        point2 += 1
    else: # Swap the two points
        point1, point2 = point2, point1
    #print point1
    #print point2
    tmp1[point1:point2], tmp2[point1:point2] = tmp2[point1:point2].copy(), tmp1[point1:point2].copy()
    return tmp1, tmp2

  def two_point_crossover(self, nextge):
    indvlist = []
    for (child1, child2) in zip(nextge[0:Const.GENERATION_SIZE/2], nextge[Const.GENERATION_SIZE/2:]):
      if random.random() < Const.CROSSOVER_RATE:
        (child1.chromosome, child2.chromosome) = self.__tpc(child1.chromosome, child2.chromosome)
      indvlist.append(child1)  
      indvlist.append(child2)  
    return indvlist

  ############
  # Mutation #
  ############
  def __mutate_flip_bit(self, chromosome):
    tmp = chromosome.copy()
    for i in range(len(chromosome)):
        if random.random() < Const.MUTATIONINDV_RATE:
            tmp[i] = type(chromosome[i])(not chromosome[i])
    return tmp

  def mutate(self, indvlist):
    mutants = []
    for mut in indvlist:
      if random.random() < Const.MUTATION_RATE:
        mut.chromosome = self.__mutate_flip_bit(mut.chromosome)
      mutants.append(mut)
    return mutants
