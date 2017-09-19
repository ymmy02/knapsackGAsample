import random
import numpy as np

from const import Const
from individual import Individual
from operators import Operators
from selection import Selection

def main():
  
  presentge = []
  nextge = []
  ops = Operators()
  slc = Selection()
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
    while True:
      indv = Individual(chsize)
      indv.loadings = ops.calcloadings(indv.chromosome, loadarray)
      if indv.loadings <= capacity:
        break
      indv = None
    indv.value = ops.calcloadings(indv.chromosome, valuearray)
    presentge.append(indv)
  
  loopcount = 0
  while not does_end(loopcount):

    # Selection
    nextge = slc.select_tounament(presentge)
    
    # Crossover
    nextge = ops.two_point_crossover(nextge, loadarray, capacity)

    # Mutation
    nextge = ops.mutate(nextge, loadarray, capacity)

    # Change Generation
    presentge = nextge[:]

    # Calculate Value
    best_indv = presentge[0]
    best_indv.value = ops.calcloadings(best_indv.chromosome, valuearray)
    s = 0
    for indv in presentge:
      indv.value = ops.calcloadings(indv.chromosome, valuearray)
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
