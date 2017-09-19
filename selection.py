import random
import copy
import numpy as np

from individual import Individual

class Selection(object):

  def __init__(self):
    self = self

  def select_tounament(self, parents, tournament_size=3):
    offsprings = []

    for _ in range(len(parents)):
      maxvalue = 0
      samples = random.sample(parents, tournament_size)

      for indv in samples:
        if indv.value > maxvalue:
          tmp = indv
          maxvalue = indv.value

      offsprings.append(tmp)

    return offsprings 
