#!/usr/bin/python3

class Perceptron():

    def __init__(self):
        # inputs to the perceptron.
        self.inputs = [[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
        self.t = 0.5
        self.bias = 0
        self.r = 0.1
        # z are the expected outputs
        self.z = [1, 1, 1, 0]
        # the initial weights when the perceptron is runned for the first time.
        self.weights = [[0.0, 0.0, 0.0]]
        self.allerrors = []

        self.getPerceptron()

    def getPerceptron(self):
        while True:
            print ("*" * 80)
            for i in range(len(self.inputs)):
                # C holds the multiplication of the initial inputs(sensor values) and the initial weights.
                c = []
                # S is the sum for the product of sensor values and the initials weights.
                s = 0.0
                # calculate both multiplications and summation
                for j in range(len(self.weights[-1])):
                    c.append (float(self.weights[-1][j]) * float(self.inputs[i][j]))
                    # round off sum to one decimal point.
                s = round(sum(c), 1)
                # T= threshold(t=0.5) ,N= network and S is the sum we have calculated
                if s > self.t:
                    n = 1
                else:
                    n = 0
                    # E is the error (calculated as expected(z) minus network (n))
                e = self.z[i] - n
                # append errors into allerrors array.
                self.allerrors.append(e)
                #  D is the correction. d = learning rate(0.1() r *error(r))
                d = self.r * float(e)
                # array to hold the new weights.
                newweights = []
                for x in range(len(self.weights[-1])):
                    # multiply sensor values with the error correction
                    change = self.inputs[i][x] * d
                    change += self.weights[-1][x]
                    # round off the new weight gotten by one decimal
                    change = round(change, 1)
                    # append the new weights to the newWeight array
                    newweights.append(change)
                    # make the new weights, the initial inputs to the next cycle.
                self.weights.append(newweights)
                # print the sensor values, desired output(z),intial weights,c ,sum,network(n) , erroe(e), correction(d) and the new wieghts.
                print (self.inputs[i], self.z[i], self.weights[-2], c, s, n, e, d, self.weights[-1])
                # when to ternimate(stop)
            if len(self.allerrors) >= 4:
                # when there is no change in the errors anymore
                if self.allerrors[-4:] == [0, 0, 0, 0]:
                    break


perceptron = Perceptron()
