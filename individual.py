
import numpy as np

class Individual(object):

  def __init__(self, chsize):
    self.chromosome = np.random.randint(0, 2, chsize)
    self.loadings = None
    self.value = None
