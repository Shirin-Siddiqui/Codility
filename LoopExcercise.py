'''
Print the following program -

*
* *
* * *
* * * *

'''

def loopExcercise(rows):
    for i in range(1, rows+1):
        for j in range(i):
            print("*", end = " ")
        print()


'''
Print the following - 

* * * * * * *
  * * * * *
    * * *
      *

'''

def loopExcercise2(rows):
    k = 0
    for i in range(rows,0,-1):
        print('  ' * k, end = " ")
        for j in range(2 * i - 1):
            print("*", end=" ")
        print()
        k = k + 1

loopExcercise2(4)
