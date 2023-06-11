# first of all load the monitor from funcStats package
from funcStats import monitor

# create or import the method that you will be testing
def testList(var1, var2, var3):
    currentList = []
    for var in [var1, var2, var3]:
        currentList.append(var)
    return currentList

# create the monitor instance, by using the target argument as the input for your method
myMonitor = monitor(target=testList)

# which will allow your access to some information that can be retrieved as follows
#print(myMonitor.targetName)
#print(myMonitor.targetArgs)
#print(myMonitor.targetInfo)

# you can also assign a file out for the monitor, which will result in a report generated to a file as below
#toFileMonitor = monitor(target=testList, toFile='testLog', console=True)
# as you can see, the file output might be generated with the .log extension, and the datetime of execution is also append to its name for convenience


# the great advantage of this package is in the ability to run multiple tests with different loads, to see the performance of your code, through the meter method
# is also possible to set multiple conjunctions of executions that can be coded as in the suggestion below
multipleTestsArgs = [
    ('a', 'b', 'c'),  # here goes the arguments based on position for the first test attempt
    ('d', 'e', 'f'),  # here goes the arguments based on position for the second test attempt and so on...
    ('g', 'h', 'i')
]

# after assigning the arguments to your executions, you can simply run the meter
#toFileMonitor.meter(multipleTestsArgs)


singleTestsArgs = [('a', 'b', 'c')]  # this time we will add a single set of tuple as the args for our target function
myMonitor.meter(singleTestsArgs, loops=10)
