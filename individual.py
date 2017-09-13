
import numpy as np

class Individual(object):

  def __init__(self, chsize):
    self.chromosome = np.random.randint(0, 2, chsize)

  def evaluate(self, evaluationfunc):
    self.__value = evaluationfunc(self.chromosome)

  def getvalue(self):
    return self.__value
