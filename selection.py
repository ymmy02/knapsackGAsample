import random
import numpy as np

from individual import Individual

def select_tounament(parents, tournament_size=3):
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
