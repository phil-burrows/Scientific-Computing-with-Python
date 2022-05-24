import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for x in range(value):
        self.contents.append(key)

  def draw(self, draws):
    if draws >= len(self.contents):
      return self.contents
    else:
      draws_list = []
      draw_hat = self.contents
      for x in range(draws):
        b = len(draw_hat) - 1
        y = random.randint(0, b)
        drawed = draw_hat.pop(y)
        draws_list.append(drawed)
      return draws_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successes = 0
  for x in range(num_experiments):
    new_hat = copy.deepcopy(hat)
    result_list = new_hat.draw(num_balls_drawn)
    
    truth_list = []
    for key, value in expected_balls.items():
      if result_list.count(key) < value:
        truth_list.append(False)
      else:
        truth_list.append(True)
    if all(truth_list):
      successes += 1

  return successes/num_experiments