import numpy as np

class Puzzle:

    solution = None
    state = None
    size = 0
    count = 0
    h = 0
    parent = None

    def get_solution(self):
        value_max = self.size * self.size
        value = 1
        x_max = self.size - 1
        y_max = self.size - 1
        x = x_min = 0
        y = y_min = 0




        print("SOLUTION ?")
        print(self.solution)
        print(value_max)
        while 1:
            x = x_min
            y = y_mingit ad
            while x < x_max:
                print(value)
                print(str(x) + ", " + str(y))
                self.solution[y,x] = value
                x += 1
                y = y_min
                print(self.solution)
                value += 1
            if value >= value_max:
                break

            while y < y_max:
                print(value)
                print(str(x) + ", " + str(y))
                self.solution[y, x] = value
                y += 1

                print(self.solution)
                value += 1
            if value >= value_max:
                break
            while x > x_min:
                print(value)
                print(str(x) + ", " + str(y))
                self.solution[y, x] = value
                x -= 1

                print(self.solution)
                value += 1
            if value >= value_max:
                break

            while y > y_min:
                print(value)
                print(str(x) + ", " + str(y))
                self.solution[y, x] = value
                y -= 1

                print(self.solution)
                value += 1
            x_min += 1
            y_min += 1
            y_max -= 1
            x_max -= 1

            if value >= value_max:
                break
        # y += 1
        print(str(x) + ", " + str(y))
        print("----")
        print(str(x_min) + ", " + str(y_min))
        print(str(x_max) + ", " + str(y_max))
        print(self.solution)