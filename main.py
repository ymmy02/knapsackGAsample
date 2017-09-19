import random
import numpy as np

from const import Const
from individual import Individual
from operators import Operators
from selection import Selection
from crossover import Crossover

def main():
  
  parents = []
  offsprings = []
  ops = Operators()
  slc = Selection()
  crs = Crossover()
  random.seed()

  # Input
  capacity = int(input("capacity : "))
  numofitems = int(input("number of items : "))
  chsize = numofitems                     # Chromosome Size
  loadarray = np.zeros(numofitems)
  valuearray = np.zeros(numofitems)
  #for i in range(numofitems):
  #  tmp = raw_input("weight,value : ").split(',')
  #  loadarray[i] = int(tmp[0])
  #  valuearray[i] = int(tmp[1])
  for i in range(numofitems):
    loadarray[i] = int(input("weight : "))
  for i in range(numofitems):
    valuearray[i] = int(input("value : "))

  # Initialize
  for i in range(Const.GENERATION_SIZE):
    indv = Individual(chsize)
    indv.loadings = calcloadings(indv, loadarray)
    indv.value = calcvalue(indv, valuearray, capacity)
    parents.append(indv)
  
  loopcount = 0
  while not does_end(loopcount):

    # Selection
    offsprings = slc.select_tounament(parents)
    
    # Crossover
    offsprings = crs.two_point_crossover(offsprings)

    # Mutation
    offsprings = ops.mutate(offsprings, loadarray, capacity)

    # Change Generation
    parents = offsprings[:]

    # Calculate Value
    best_indv = parents[0]
    best_indv.loadings = calcloadings(best_indv, loadarray)
    best_indv.value = calcvalue(best_indv, valuearray, capacity)
    for indv in parents:
      indv.loadings = calcloadings(indv, loadarray)
      indv.value = calcvalue(indv, valuearray, capacity)
      if indv.value > best_indv.value:
        best_indv = indv

    #########
    # Debug #
    #########
    print "Generation " + str(loopcount) + "Best value : " + str(best_indv.value)
    #print "Chromosome"
    #print best_indv.chromosome

    loopcount += 1

  # Output
  print "########## result ##########"
  print "Last Generation"
  print "Best value : " + str(best_indv.value)
  print "Chromosome"
  print best_indv.chromosome


def calcloadings(indv, loadarray):
  return np.sum(indv.chromosome*loadarray)

def calcvalue(indv, valuearray, capacity, penalty_rate=2.0):
  return np.sum(indv.chromosome*valuearray) - penalty(capacity, indv.loadings, penalty_rate)

def penalty(capacity, loadings, rate):
  if loadings > capacity:
    return rate * (loadings-capacity)**2
  else:
    return 0

def does_end(loopcount):
  if loopcount > Const.NLOOP:
    return True
  return False

if __name__ == "__main__":
  main()
