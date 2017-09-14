import random
import copy
import numpy as np

from const import Const
from individual import Individual

class Operators(object):
  
  def __init__(self):
    self = self

  def clacvalue(self, chromosome, valuearray):
    return np.sum(chromosome*valuearray)

  def calcloadings(self, chromosome, loadarray):
    return np.sum(chromosome*loadarray)

  #############
  # Selection #
  #############

  def select_tounament(self, presentge):
    nextge = []

    for _ in range(Const.GENERATION_SIZE):
      maxvalue = 0
      samples = random.sample(presentge, Const.TOURNAMENT_SIZE)

      for indv in samples:
        if indv.value > maxvalue:
          tmp = indv
          maxvalue = indv.value

      nextge.append(tmp)

    return nextge 

  #############
  # Crossover #
  #############

  def __tpc(self, chromosome1, chromosome2):
    size = len(chromosome1)
    tmpch1 = chromosome1.copy()
    tmpch2 = chromosome2.copy()
    point1 = random.randint(1, size)
    point2 = random.randint(1, size-1)
    if point2 >= point1:
        point2 += 1
    else: # Swap the two points
        point1, point2 = point2, point1
    #print point1
    #print point2
    tmpch1[point1:point2], tmpch2[point1:point2] = tmpch2[point1:point2].copy(), tmpch1[point1:point2].copy()
    return tmpch1, tmpch2

  def two_point_crossover(self, nextge, loadarray, capacity):
    indvlist = []
    for (child1, child2) in zip(nextge[0:Const.GENERATION_SIZE/2], nextge[Const.GENERATION_SIZE/2:]):
      tmp1 = copy.deepcopy(child1)
      tmp2 = copy.deepcopy(child2)

      if random.random() < Const.CROSSOVER_RATE:
        while True:
          (tmp1.chromosome, tmp2.chromosome) = self.__tpc(child1.chromosome, child2.chromosome)
          tmp1.loadings = self.calcloadings(tmp1.chromosome, loadarray)
          tmp2.loadings = self.calcloadings(tmp2.chromosome, loadarray)
          if tmp1.loadings <= capacity and tmp2.loadings <= capacity:
            break

      indvlist.append(tmp1)  
      indvlist.append(tmp2)  
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

  def mutate(self, indvlist, loadarray, capacity):
    mutants = []

    for mut in indvlist:
      tmpmut = copy.deepcopy(mut)
      if random.random() < Const.MUTATION_RATE:
        tmpmut.chromosome = self.__mutate_flip_bit(mut.chromosome)

      tmpmut.loadings = self.calcloadings(tmpmut.chromosome, loadarray)
      if tmpmut.loadings <= capacity:
        mutants.append(tmpmut)
      else:
        mutants.append(mut)
        
    return mutants
