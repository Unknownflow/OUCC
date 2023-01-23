# Task
You may have seen a magician that has a row of cups. A ball is placed under one of the cups. Then two cups are quickly swapped. This is done multiple times, too fast for the human eye. Finally you have to say where the ball is.

Rubi is a very skilled magician. She has N cups that are placed in positions 0 to N-1.
Initially she places the ball underneath cup N (in position N-1).

cups image

Task:
Write a program that inputs a list of swaps. The first line indicates how many cups there are. The next line indicates how many swaps there are. The lines after that each contain two integers separated by a space that indicate the positions of two cups that are swapped. Your program should output the position of the cup that contains the ball after all swaps have taken place.

Constraint:
There are at least 4 cups, and at most 100 swaps.

Example Input:
4
4
0 1
2 3
3 0
1 2

Example Output:
1
