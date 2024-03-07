import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for x in range(v):
                self.contents.append(k)

    def draw(self, num):
        urn = []
        urn = copy.copy(self.contents)

        drawn = []
        if num > len(urn):
            return urn
        else:
            for x in range(num):
                ball = random.choice(urn)
                drawn.append(ball)
                urn.remove(ball)
            return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    total_exp = 0
    valid_draws = 0

    while total_exp < num_experiments:
        # Draw num_balls_drawn
        drawn = hat.draw(num_balls_drawn)

        colour_count = {}
        colour_names = []
        for ball in drawn:
            if ball not in colour_count.keys():
                colour_count[ball] = 1
                colour_names.append(ball)
            else:
                colour_count[ball] += 1

        compare = 0
        flag = False
        for n, v in expected_balls.items():
            print(n, v)
            if n in colour_names:
                if colour_count[n] >= v:
                    compare += 1

        if compare == (len(expected_balls)):
            valid_draws += 1
            flag = True

        print('Balls Drawn:', colour_count)
        print('Expected Balls:', expected_balls)
        print('Flag:', flag)
        print('Experiment ' + str(total_exp + 1) + ' complete.\n')
        total_exp += 1

    return valid_draws/num_experiments
