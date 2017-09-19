import random
import copy
import numpy as np

from const import Const
from individual import Individual

class Operators(object):
  
  def __init__(self):
    self = self

  def calcvalue(self, chromosome, valuearray):
    return np.sum(chromosome*valuearray)

  def calcloadings(self, chromosome, loadarray):
    return np.sum(chromosome*loadarray)

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
