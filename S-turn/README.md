# Task
One way to make a sentence look more secretive is by using the S-turn.

For every word in the sentence you check if the word starts or ends with the letter S. If this is the case, you turn the letters in the word around. All other words and spaces stay the same.

If you read a sentence that has been S-turned, it's easy to retrieve the original sentence: Just operate the S-turn again.

Task:
Write a program that reads a sentence from standard input and outputs the S-turned sentence in lowercase.

Constraints:
The input sentences provided will always consist of CAPITAL letters with spaces between words.
No accents or symbols will be used.
The sentences provided will always have a maximum of 80 characters.

Example input:
SCHOOL SAUCE IS SO TASTY

Example output:
loohcs ecuas si os tasty
