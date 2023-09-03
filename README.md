# Software dev assignments
IMPORTANT: this is my assignment for my software design/development module from my first year of university. (Project brief in the project details section)

Instructions for use:

1. Download Software_dev_assignments.py

2. Run Software_dev_assignments.py

3. A list of available commands will be printed out on your output terminal. Type in whichever command you would like to use.

--------------------------------------------------------------------------
Project details

Name: Software dev assignments

Version: 1

Compatibility: Compatible with windows and android. Should work on linux and ios/mac os but is untested.

Use case(s): N/A.

Sources: N/A. This is all my own code.

Contact info: Miahn03@hotmail.com

Final notes: I created this project in my first semester of university for my software design/development module. There were 5 total tasks. Some of the tasks have multiple solutions, these were added after my final submission as I wanted to practice more with object orientated programming. The newer functions have a '2' at the end of the function name. I received 88% (first) for my final grade in this module.

Project brief summary:

Task 1: Write a python function to print an American flag on the screen. 

Task 2: Write a python function to compute the BMI of a person. The program should take input values such as weight and height and display it on the screen. In addition, the program should display to the user whether the calculated BMI result corresponds to underweight, healthy weight or overweight. 
Formula: weight (kg) / [height (m)]2 

Task 3: Write a python program to simulate an online store. The program should display a list of products and their prices. There should be a minimum of 4 products offered. The program should ask the user to choose a product and then ask the user to enter the quantity they require of that product. The program should then allow the user to keep choosing more products and quantities until they enter something to indicate they want to end the program. The program should then tell the user the amount for the products they selected.

Task 4: Write a program that computes the tally in a write-in election, and announces the winner. The user enters the individual votes, one vote per line, and ends entering with typing -1 or an empty line. To compute the tally, the program uses two arrays, a String [ ] variable (names), and an int [ ] variable (count). Upon receiving a single vote, the program checks if the name on the vote appears in names, and if it does, the program adds 1 to the value of the element in count. If the name does not appear in names, the program extends both arrays by one element, stores the name in names at the last position and store 1 in count at the last position. In this manner, the two arrays will have the same lengths. The initial length is 0 for both arrays. 

Task 5: Task 5 is on Object Oriented Programming. 

Design a class named Account that contains: 

• A private int data field named id for the account (default 0). 

• A private double data field named balance for the account (default 0). 

• A private double data field named annualInterestRate that stores the current interest rate (default 0). Assume all accounts have the same interest rate. 

• A private Date data field named dateCreated that stores the date when the account was created. 

• A no-argument constructor that creates a default account. 

• A constructor that creates an account with the specified id and initial balance. 

• The accessor and mutator methods for id, balance, and annualInterestRate. 

• The accessor method for dateCreated. 

• A method named getMonthlyInterestRate() that returns the monthly interest rate. 

• A method named withdraw that withdraws a specified amount from the account. 

• A method named deposit that deposits a specified amount to the account. 

Bugs found:

1. If you run the election script and enter nothing, it crashes.

Features i would like to add:
N/A
