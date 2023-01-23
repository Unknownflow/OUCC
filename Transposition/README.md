# Task
Agents Boris and Bertha communicate using secret messages.
Boris wants to send Bertha the secret message:

meetbillybeaverat6

He writes each character (in upper case form) into a 4 column grid from left to right and row by row starting from the top. Any unused spaces are filled with the capital letter X. The result is shown below.

![image](https://user-images.githubusercontent.com/81907539/168553137-4e2825e1-6b25-4934-8c3a-f07d4174c95f.png)

Then he creates the secret message by reading the characters from top to bottom and column by column starting from the left:

MBYVTEIBE6ELERXTLAAX

To make their messages even harder to crack, Boris and Bertha never include spaces between the words.

Task
Write a program that can be used to encode and decode messages using this system. Your program should take two inputs:

    a string that is either encode or decode on the first row
    a string that is the message (either encoded or decoded).

It should then output the message either encoded or the original message as required.

Example Inputs:
encode
meetbillybeaverat6

Example Output:
MBYVTEIBE6ELERXTLAAX

Constraints:

    All punctuation marks are treated like letters and go in their own space in the grid.
    The encoded messages provided as input will always consist of uppercase letters.
    The unencoded messages provided as input will always consist of lowercase letters.
    All input provided will consist of 8 to 40 characters.
    Decoded messages that are output must consist of lowercase letters and must not remove the trailing x letters (just in case the message ends with an x).
