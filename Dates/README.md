# Task
An application requires users to enter a date. It has been decided that only one format is to be accepted: yyyy-mm-dd

Task:
Write a standalone program, that will later be incorporated in the application. It takes a string as input and outputs True if the string validates according to the rules written below. In all other cases it should output False.

Validation criteria:

    The date must only consist of integers and two hyphens in the correct places.
    The year yyyy must consist of four digits and be no later than 2020 and no earlier than 1900.
    The month mm and the day dd must be two characters long, with a zero before single digit dates.
    mm must be less than 13 and more than 0.
    dd must be less than 32 and more than 0.

Example input:
1982-05-16

Example output:
True

Constraints:
The string provided will always consist of at least 1 and at most 10 characters.
