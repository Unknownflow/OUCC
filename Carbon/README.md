# Task
A program that estimates the amount of CO2 emitted by three forms of transport when travelling across Europe is required.

Information:

    Rail travel produces 30g of CO2 / km per person.
    Average petrol car produces 100g of CO2 / km with just a driver + 10g/km for each extra passenger. Cars can be assumed to hold no more than 3 passengers plus the driver so, if more than 4 people need to travel by car, two cars are required.
    Air travel produces 240g of CO2 / km per person. Flights can only be considered viable for journeys of 100km or more.

Inputs:
number of people
Distance in km

Outputs:
Total CO2 produced by Rail in g
Total CO2 produced by Car in g
Total CO2 produced by Air in g

Example inputs:
9
1000

Example outputs:
270000
360000
2160000

Constraints:
The number of passengers provided will always be greater than 0 and less than 13.
The distances provided will always be from 0 to 10000.
If the distance is less than 100, the output for air travel should be: no flight available
All outputs must be in the form of integers (unless the output is no flight available).

Task:
Build a program that calculates the average amount of CO2 in g, that is produced when travelling by Rail, Car and Air.
