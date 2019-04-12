#-------------------------------------------------------------------------------
# Name:        Bayes_Criterion
# Purpose:
#
# Author:      Andrew Podobed
#
# Created:     11.04.2019
# Copyright:   (c) Robinovich 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""
------------------- Attention!!! --------------------------------------------------------------------------------

In order to use the program I give an example of a task, after which I will point out the sequence of data entry:
Put and solve the game with nature in a situation: “There are two investment projects. The first project with a
probability of 0.6 provides a profit of 15 million rubles, however, with a probability of 0.4, you can lose 5.5
million rubles. The second project with a probability of 0.2 provides a loss of 6 million rubles. and with a
probability of 0.8 - a profit of 10 million rubles. Which project to choose? "
------------------------------------------------------------------------------------------------------------------

-- Enter the data for strategy A1:                                             --\
--> Enter the amount of profit of the first event                              ---\
---> Introduce the probability of the first strategy event (value from 0 to 1).----\
----> Enter the amount of profit of the second variant of events               -----\

-- Enter the data for strategy A:
--> Enter the amount of profit of the second event
---> Introduce the probability of the first strategy event (value from 0 to 1).
----> Enter the amount of profit of the second variant of events

"""

A1_profit_1 = float(input('Enter profit 1 by A1 strategy:'))
A1_q_1 = float(input('Enter the probability 1 of the A1 strategy:'))
A1_profit_2 = float(input('Enter profit 2 by A1 strategy:'))
A1_q_2 = 1 -A1_q_1

A2_profit_1 = float(input('Enter profit 1 by A2 strategy:'))
A2_q_1 = float(input('Enter the probability 1 of the A2 strategy:'))
A2_profit_2 = float(input('Enter profit 2 by A2 strategy:'))
A2_q_2 = 1 - A2_q_1

print('                          ----------------')
print('==========================| Data entered |==============================')
print('                          ----------------')
print('=======================================================================')
print('|  State of nature   ', '|    N1    ', '|    N2    ', '|    N3    ', '|     N4    |')
print('=======================================================================')
print('|  Probability       ', '|{: 10.2F}'.format(A1_q_1), '|{: 10.2f}'.format(A1_q_2), '|{: 10.2f}'.format(A2_q_1), '|{: 10.2f}'.format(A2_q_2), '|')
print('|-----------------------------------------------------------------------')
print('|  Strategy A1       ', '|{: 10.2F}'.format(A1_profit_1), '|{: 10.2f} |'.format(A1_profit_2))
print('|  Strategy A2       ', '|           ', '          ', '|{: 10.2f}'.format(A2_profit_1), '|{: 10.2f}'.format(A2_profit_2), '|')
print('------------------------------------------------------------------------')
print('')
print('|========================== Bayes Criterion ========================================|')
print('| By the Bayes criterion, the (pure) Ai strategy is taken as the optimal one,       |')
print('| which maximizes the average gain “a” or minimizes the average risk “r”.           |')

profit_A_1 = A1_profit_1 + A1_profit_2
profit_A_2 = A2_profit_1 + A2_profit_2

A_1_1 = A1_profit_1 * A1_q_1
A_1_2 = A1_profit_2 * A1_q_2
A_2_1 = A2_profit_1 * A2_q_1
A_2_2 = A2_profit_2 * A2_q_2

sum_A_1 = A_1_1 + A_1_2
sum_A_2 = A_2_1 + A_2_2


print('=====================================================================================')
print('|  State of nature   ', '|    N1    ', '|    N2    ', '|    N3    ', '|     N4    |', '   Amount   |')
print('=====================================================================================')
print('|  Strategy A1       ', '|{: 10.2F}'.format(A_1_1), '|{: 10.2f} |'.format(A_1_2), '                     ', '|{:10.2f}   |'.format(sum_A_1))
print('|------------------------------------------------------------------------------------')
print('|  Strategy A2       ', '|           ', '          ', '|{: 10.2f}'.format(A_2_1), '|{: 10.2f}'.format(A_2_2), '|{:10.2f}   |'.format(sum_A_2))
print('|------------------------------------------------------------------------------------')
print('|  Probability       ', '|{: 10.2F}'.format(A1_q_1), '|{: 10.2f}'.format(A1_q_2), '|{: 10.2f}'.format(A2_q_1), '|{: 10.2f} |'.format(A2_q_2))
print('-------------------------------------------------------------------------------------')
print('')
print('Choose from {:.2f}'.format(sum_A_1), 'and {:.2f}'.format(sum_A_2),':max element = {:.2F}'.format(max(sum_A_1, sum_A_2)))

if sum_A_1 > sum_A_2:
    print('Need to choose strategy A1')
elif sum_A_1 < sum_A_2:
    print('Need to choose strategy A2')
elif sum_A_1 == sum_A_2:
    if profit_A_1 > profit_A_2:
        print('Need to choose strategy A1')
    elif profit_A_1 < profit_A_2:
        print('Need to choose strategy A2')
