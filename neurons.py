# this project is the very start of neural networks, basically a few neurons with no layers
inputs = [2.2, 4.8, 3.4]
weights = [1.9, 5.3, 2.1]
bias = 3
finalvar =0
for i in range(0, len(inputs)):
    tempp = inputs[i]*weights[i]
    finalvar += tempp
output2 = finalvar+bias
print(str(output2))