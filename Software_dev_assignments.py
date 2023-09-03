## Task 1 (american flag)
def print_flag():## main code for printing the american flag
    x = ("* "*5+"*")+"="*35
    y = (" *"*5+" ")+"="*35
    print((x+"\n"+y+"\n")*4+x)## alternates between printing x and y
    for i in range(1, 7):## definite for loop for printing the rest of the lines 
        print("="*46)



## Task 2 (BMI calculator)
def get_values():## asks for user input and returns the values
    weight = input("what is your weight (in KG):  ")
    height = input("what is your height (in meters):  ")
    return weight, height

def calculate_BMI(weight, height):## executes the formula for BMI and returns the result
    BMI = float(weight)/(float(height)**2)
    return BMI

def check_BMI(BMI):## checks what the BMI suggests in terms of weight and returns the suggestion
    if BMI < 18.5:
        return "you are underweight"
    if 18.5 <= BMI < 24.9:
        return "you are at a healthy weight"
    return "you are overweight"

def BMI():## main code that calls the appropriate functions and prints the results
    weight, height = get_values()
    BMI = calculate_BMI(weight=weight, height=height)
    print("your BMI is: " + str(round(BMI, 2)))
    print(check_BMI(BMI=float(BMI)))



##Task 3 (online store)
item_list = [["primogems", "99", "4.79"], ["the daemons underneath my GUI", "99", "1.00"], ["biohacks", "99", "5.00"], ["forged computer science degree certification", "1", "1500.00"]]## global nested list containing the item's name, stock and value 

with open("price.txt", "w") as f:## opening an external txt document to keep track of price
    f.write("0")
    f.close()

def handle_store():## handles user inputs, updates the external file, prints the final cost if need be and returns leftover stock and the PID of the selected item
    selected_item = input("enter the product ID for the item you wish to buy (PID):  ")
    if selected_item == "exit" or selected_item == "":
        with open("price.txt", "r") as f:
            print("final total: " + f.read())
            f.close()
        exit()
    selected_item = int(selected_item)
    amount = input("how many of this item would you like to buy:  ")
    if amount == "exit" or amount == "":
        with open("price.txt", "r") as f:
            print("final total: " + f.read())
            f.close()
        exit()
    amount = int(amount)
    if amount > int(item_list[selected_item][1]):
        print("error: not enough stock, please try again")
        exit()
    else:
        with open("price.txt", "r") as f:
            x = f.read()
            f.close()
        with open("price.txt", "w") as f:
            f.write(str(float(x) + amount*float(item_list[selected_item][2])))
        leftover_stock = int(item_list[selected_item][1]) - amount
    return leftover_stock, selected_item

def handle_transaction():## prints out and updates the nested list values
    for i in range(0, len(item_list)):
        print("PID: "+str(i)+" ("+item_list[i][0]+"):")
        print("\tprice per unit: £" + item_list[i][2])
        print("\tstock: ×" + item_list[i][1])
    leftover_stock, selected_item = handle_store()
    item_list[selected_item][1] = str(leftover_stock)

def online_store():## loops indefinitely until the user inputs 'exit' or an empty line
    while True:
        handle_transaction()



##task 3 (online store class version)
class item:
    def __init__(self, name, stock, price):
        self.name = name
        self.stock = stock
        self.price = price
    def buy(self, amount):
        if amount <= self.stock:
            price = self.price * amount
            self.stock = self.stock-amount
            return price
        print("error: not enough stock")
        return 0

bananas = item("bananas", 5000, 0.5)
cookies = item("cookies", 5, 1.0)
apples = item("apples", 100, 2.5)
crisps = item("crisps", 260, 0.5)
item_list1 = [bananas, cookies, apples, crisps]

def online_store2():
    final_price = 0.0
    while True:
        print("press '999' to exit at any time")
        print("available items:\n")
        count = 0
        for i in item_list1:
            print(i.name,"("+"PID:",str(count)+"):\nstock:  "+str(i.stock)+"\nprice:  "+str(i.price)+"0\n")
            count += 1
        PID = int(input("enter PID:  "))
        if PID == 999:
            print("final total: " + str(final_price))
            exit()
        amount = int(input("enter amount:  "))
        if amount == 999:
            print("final total: " + str(final_price))
            exit()
        price = item_list1[PID].buy(amount)
        final_price = final_price + price




## Task 4 (election)
names = []## global list that will store name values as tyoe string
count = []## global list that will store amount of votes as type int

def get_name():## records user input for name value and returns it
    x = 0
    y = 0
    print("exit using -1 or an empty line")
    name = input("enter ONE name into the system at a time:  ")
    if name == "-1" or name == "":
        for i in range(0, len(names)):
            print(names[i]+" got " +str(count[i]) + " vote(s)")
            if int(count[i]) > y:
                x = i
                y = int(count[i])
        if len(set(count)) == 1:
            print("no one won")
            exit()
        print(names[x]+" won with "+str(count[x])+" vote(s)")
        exit()
    return name

def election_is_running():## handles when to call functions, checks if the received name is in the list. If not, appends the name to the list and appends an int value to count
    name = get_name()
    if name not in names:
        names.append(name)
        count.append(1)
    else:
        for i in range(0, len(names)):
            if names[i] == name:
                count[i] = int(count[i]) + 1
def election():## loops indefinitely until the user inputs '-1' or an empty line
    while True:
        election_is_running()



## Task 4 (election class version)
class vote:
    def __init__(self, name):
        self.name = name
        self.votes = 1
        
    def add_vote(self):
        self.votes += 1
        	

participants = []

def election2():
    winner = 0
    count = []
    while True:
        name = input("enter a name (or an empty line to exit):  ")
        if name == "":
            for i in range(0, len(participants), 2):
                print(participants[i], "got", str(participants[i+1].votes), "vote(s)")
                count.append(participants[i+1].votes)
                if participants[i+1].votes > winner:
                    winner = participants[i+1].votes
                    winner_object = participants[i+1]
            if len(set(count)) == 1:
                print("no one won")
                exit()
            print(winner_object.name, "won with", str(winner), "vote(s)")
            exit()
        if name not in participants:
            participants.append(name)
            name = vote(name)
            participants.append(name)
            continue
        for i in range(0, len(participants), 2):
            if participants[i] == name:
                participants[i+1].add_vote()




## Task 5 (Account)
from datetime import date
class Account:

    def default(self):## sets instance attributes (id, balance, annualInterestRate) to 0 and dateCreated to todays date
        self.id = 0
        self.balance = 0
        self.annualInterestRate = 0
        self.dateCreated = date.today()

    def create(self, id, balance):## sets instance attributes to user defined values (dateCreated still set to todays date)
        self.id = id
        self.balance = balance
        self.dateCreated = date.today()

    def id(self, id):## sets instance id to user defined value then returns it
        self.id = id
        return self.id

    def balance(self, balance):## sets instance balance to user defined value then returns it
        self.balance = balance
        return self.balance

    def annualInterestRate(self, annualInterestRate):## sets instance annual interest rate to user defined value then returns it
        self.annualInterestRate = annualInterestRate
        return self.annualInterestRate

    def dateCreated(self):## returns dateCreated
        return self.dateCreated

    def withdraw(self, amount):## deducts withdrawal amount from instance balance
        if self.balance >= amount:
            self.balance -= amount
        else:
            return "error: not enough funds"

    def deposit(self, amount):## increases instance balance by deposit amount
        self.balance += amount

    def getMonthlyInterestRate(self):## calculates and returns monthly interest
        x = round(self.annualInterestRate / 12, 2)
        return x

print("available functions:\nprint_flag()\nBMI()\nonline_store()\nonline_store2()\nelection()\nelection2()\navailable classes:\nAccount")
print("use 'help(Account)' to view available methods")
