import random
import numpy as np

from const import Const
from individual import Individual
from operators import Operators

def main():
  
  presentge = []
  nextge = []
  ops = Operators()
  random.seed()

  # Input
  #capacity = int(input("capacity : "))
  numofitems = int(input("number of items : "))
  chsize = numofitems                     # Chromosome Size
  items = np.zeros((numofitems, 2))       # [[weight, value], ...]
  #for i in range(numofitems):
  #  temp = raw_input("weight,value : ").split(',')
  #  items[0] = int(temp[0])
  #  items[1] = int(temp[1])

  # Initialize
  for i in range(Const.GENERATION_SIZE):
    indv = Individual(chsize)
    indv.evaluate(evaluationfunc)
    presentge.append(indv)
  
  loopcount = 0
  while not does_end(loopcount):

    # Selection
    nextge = ops.select_tounament(presentge)
    
    # Crossover
    nextge = ops.two_point_crossover(nextge)

    # Mutation
    nextge = ops.mutate(nextge)

    # Change Generation
    presentge = nextge[:]

    # Calculate Value
    best_indv = presentge[0]
    best_indv.evaluate(evaluationfunc)
    s = 0
    for indv in presentge:
      indv.evaluate(evaluationfunc)
      s += indv.getvalue()
      if indv.getvalue() > best_indv.getvalue():
        best_indv = indv

    #########
    # Debug #
    #########
    print "Generation " + str(loopcount)
    print "Best value : " + str(best_indv.getvalue())
    print "Chromosome"
    print best_indv.chromosome
    # test
    print "Sum : " + str(s)

    loopcount += 1

  # Output
  print "########## result ##########"
  print "Last Generation"
  print "Best value : " + str(best_indv.getvalue())
  print "Chromosome"
  print best_indv.chromosome

def evaluationfunc(chromosome):
  return np.sum(chromosome)

def does_end(loopcount):
  if loopcount > Const.NLOOP:
    return True
  return False

if __name__ == "__main__":
  main()
