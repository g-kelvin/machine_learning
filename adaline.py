import random

training_sets = {(1, -1, 1,): 1, (-1, 1, -1,): -1} #{set:desired_result}
# the bias learning rate and average error is given
bias = 1
learning_pace = 0.3
average_error = 1

# Initialize synapses with random values
synapses = [random.choice((0.0, 1.0,)) for i in xrange(4)]
print("\n the synapses are:\n")
print synapses, '\n',
print ("*" * 80)
#Start training...
while average_error > 0.01:
    errors = 0
    for itemset, desired_result in training_sets.iteritems():
        inputs = (bias,) + itemset
        #Calculate the output
        output = sum(map(lambda x: x[0]*x[1], zip(synapses, inputs)))
        # Calculate the error
        error = desired_result - output
        if error != 0:
            #Update synapse values
            delta_w = map(lambda x: x*learning_pace*error, inputs)
            synapses = map(lambda w: w[0]+w[1], zip(synapses, delta_w))
            #assign and increment the errors
        errors += error**2
        # print thr itemset the errors and the synapses.
        print("\nThe Itemset \t\t\t Error \t\t\t Synapses \n")
        print 'itemset=', itemset, "\t"'| error=', error,"\t" '| synapses=', synapses
    else:
        print ("*" * 80)
        # get the average of the errors 
        average_error = errors/len(training_sets)
else:
	# print both the synapses and the average of the errors
	print "\t the Synapses and the average of the error are:\n"
	print "synapses = ", synapses
	print "average error = ", average_error


