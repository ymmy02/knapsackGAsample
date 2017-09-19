import random
import copy
import numpy as np

from individual import Individual

class Mutation(object):
  
  def __init__(self):
    self = self

  def __mutate_flip_bit(self, chromosome, rate):
    tmp = chromosome.copy()
    for i in range(len(chromosome)):
        if random.random() < rate:
            tmp[i] = type(chromosome[i])(not chromosome[i])
    return tmp

  def mutate(self, indvlist, indv_mutation_rate=0.2, chromosome_mutation_rate=0.03):
    mutants = []

    for mut in indvlist:
      tmpmut = copy.deepcopy(mut)
      if random.random() < indv_mutation_rate:
        tmpmut.chromosome = self.__mutate_flip_bit(mut.chromosome, chromosome_mutation_rate)
      mutants.append(tmpmut)
        
    return mutants
