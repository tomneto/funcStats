# FuncStats

### This package is aimed to attend the needs of testing performance of some Python execution, we hope you'll enjoy!


#### To use, follow the steps below:

- First of all, you will need to install the package by running the command:

        pip install funcStats


 - To load the monitor from funcStats package, add the following line:
    
        from funcStats import monitor

 - You can create or import the method that you will be testing, this will be our test method:

        def testList(var1, var2, var3):
            currentList = []
            for var in [var1, var2, var3]:
                currentList.append(var)
            return currentList

 - After load the monitor, you can create the monitor instance, by passing the method that will be monitored in the target argument.

        myMonitor = monitor(target=testList)

 - Which will allow your access to some information that can be retrieved like in the following code:
    
        print(myMonitor.targetName)
        print(myMonitor.targetArgs)
        print(myMonitor.targetInfo)

 - You can also assign a file out for the monitor, which will result in a report generated to a file:
    
        toFileMonitor = monitor(target=testList, toFile='path/to/file/testLog', console=True)

     As you can see, the file output might be generated with the .log extension, and the datetime of execution is also append to it's name for convenience.


### One of the great advantages of this package is the ability to run multiple tests with different loads, to see the performance of your code, through the meter method.

 - Is also possible to set multiple conjunctions of executions that can be coded as in the suggestion below
    
        multipleTestsArgs = [
            ('a', 'b', 'c'),  # here goes the arguments based on position for the first test attempt
            ('d', 'e', 'f'),  # here goes the arguments based on position for the second test attempt and so on...
            ('g', 'h', 'i')
        ]

 - After assigning the arguments to your executions, you can simply run the meter, and pass the arguments list, to make it run your target function multiple times with the samples provided.

        toFileMonitor.meter(multipleTestsArgs)

 
 - In the case you need to run the method with the same set of args, but at multiple times, it can be achieved by adding the loops arg to the meter execution.

       singleTestsArgs = [('a', 'b', 'c')] # this time we will add a single set of tuple as the args for our target function
       toFileMonitor.meter(singleTestsArgs, loops = 10)

### This will give you access to the information needed to monitor the performance of your method, without causing too much struggling.
This is a sample obtained by running the code provided in our multiple args example:

    [FuncStats Report] 2023-06-10 23:14:52.501321 - [testList] - Meter: Loading args... [('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i')]

    [FuncStats Report] 2023-06-10 23:14:52.501480 - [testList] - Meter Execution Count: 1
    [FuncStats Report] 2023-06-10 23:14:52.501596 - [testList] - Meter Execution Starts at: 2023-06-10 23:14:52.501477
    [FuncStats Report] 2023-06-10 23:14:52.501710 - [testList] - Meter Execution Args: ('a', 'b', 'c')
    [FuncStats Report] 2023-06-10 23:14:52.501824 - [testList] - Meter Execution Returns: ['a', 'b', 'c']...
    [FuncStats Report] 2023-06-10 23:14:52.501946 - [testList] - Meter Execution Takes: 0h 0m 0s 0ms


    [FuncStats Report] 2023-06-10 23:14:52.502111 - [testList] - Meter Execution Count: 2
    [FuncStats Report] 2023-06-10 23:14:52.502224 - [testList] - Meter Execution Starts at: 2023-06-10 23:14:52.502108
    [FuncStats Report] 2023-06-10 23:14:52.502329 - [testList] - Meter Execution Args: ('d', 'e', 'f')
    [FuncStats Report] 2023-06-10 23:14:52.502437 - [testList] - Meter Execution Returns: ['d', 'e', 'f']...
    [FuncStats Report] 2023-06-10 23:14:52.502545 - [testList] - Meter Execution Takes: 0h 0m 0s 0ms


    [FuncStats Report] 2023-06-10 23:14:52.502696 - [testList] - Meter Execution Count: 3
    [FuncStats Report] 2023-06-10 23:14:52.502895 - [testList] - Meter Execution Starts at: 2023-06-10 23:14:52.502693
    [FuncStats Report] 2023-06-10 23:14:52.503016 - [testList] - Meter Execution Args: ('g', 'h', 'i')
    [FuncStats Report] 2023-06-10 23:14:52.503129 - [testList] - Meter Execution Returns: ['g', 'h', 'i']...
    [FuncStats Report] 2023-06-10 23:14:52.503238 - [testList] - Meter Execution Takes: 0h 0m 0s 0ms

Another sample but this time from the single args:

    [FuncStats Report] 2023-06-11 00:09:57.752710 - [testList] - Meter: Loading args... [('a', 'b', 'c')]

    [FuncStats Report] 2023-06-11 00:09:57.752747 - [testList] - Meter Execution Count: 1
    [FuncStats Report] 2023-06-11 00:09:57.752759 - [testList] - Meter Execution Starts at: 2023-06-11 00:09:57.752741
    [FuncStats Report] 2023-06-11 00:09:57.752767 - [testList] - Meter Execution Args: ('a', 'b', 'c')
    [FuncStats Report] 2023-06-11 00:09:57.752778 - [testList] - Meter Execution Returns: ['a', 'b', 'c']...
    [FuncStats Report] 2023-06-11 00:09:57.752795 - [testList] - Meter Execution Takes: 0h 0m 0s 0ms


    [FuncStats Report] 2023-06-11 00:09:57.752814 - [testList] - Meter Execution Count: 2
    [FuncStats Report] 2023-06-11 00:09:57.752825 - [testList] - Meter Execution Starts at: 2023-06-11 00:09:57.752806
    [FuncStats Report] 2023-06-11 00:09:57.752832 - [testList] - Meter Execution Args: ('a', 'b', 'c')
    [FuncStats Report] 2023-06-11 00:09:57.752842 - [testList] - Meter Execution Returns: ['a', 'b', 'c']...
    [FuncStats Report] 2023-06-11 00:09:57.752851 - [testList] - Meter Execution Takes: 0h 0m 0s 0ms


    [FuncStats Report] 2023-06-11 00:09:57.752889 - [testList] - Meter Execution Count: 3
    [FuncStats Report] 2023-06-11 00:09:57.752898 - [testList] - Meter Execution Starts at: 2023-06-11 00:09:57.752883
    [FuncStats Report] 2023-06-11 00:09:57.752907 - [testList] - Meter Execution Args: ('a', 'b', 'c')
    [FuncStats Report] 2023-06-11 00:09:57.752917 - [testList] - Meter Execution Returns: ['a', 'b', 'c']...
    [FuncStats Report] 2023-06-11 00:09:57.752927 - [testList] - Meter Execution Takes: 0h 0m 0s 0ms

You can find the source code for this package at the link: https://github.com/tomneto/funcStats