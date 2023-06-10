With this module you can run your functions in a test environment printing and retrieving information such as the execution time.

To use this module as a function monitor do the following steps:

Create a function that will be monitored, as the example below:

    def testList():
        currentList = []

        for var in ['a', 'b', 'c', 'd', 'e', '']:
            currentList.append(var)
            currentList.remove(var)

    return currentList

Then simply run the function using the meter method provided at the funcStats package, like this:

    from funcStats import meter

    meter(func=testList, loopCount=3)

Where the func arg, is the function to be executed (be careful to not call the function, and just pass it to the meter method), you also have a loopCount parameter that allows you to control how many times your function must be executed to be evaluated.
If you need to add arguments to the executions of your function, you can also pass the arguments as the below example:

    from funcStats import meter

    meter(func=testList, loopCount=3, arg1, arg2, arg3)

Where the arg1, arg2, arg3 are the arguments received to the provided function.

I hope you enjoy.