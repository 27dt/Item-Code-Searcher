'''
Outside of school, I work part time in the meat department at a grocery store. 
One of my responsibilities is to be able to price items, which often come without a label. 
My job is to input the item's specific inventory code, and then weigh it on the scale, 
which assigns a price to it that corresponds to its code (example: inputting 85522 on the scale 
sets up the scale for us to be able to weigh and price chicken cutlets, which always comes unpriced 
from the factory). With all the products we carry, there is an extensive and ever-growing list 
printed out in the back room of the employee area. This list is now over 80 items long, and 
although I have memorized most of the codes I need, I know many others have not.

There are two problems I intend to solve with my code: for starters, I want to create a program 
that allows a user to search through a list of all the code/item combinations. To do this, I 
must digitize the paper list into a text file, and allow the user to enter a search query (chicken, beef,
ham, etc), to which the program will output all results that match the input value. Second, I want to give the 
user the ability to add a new item to the list. This will be done by retrieving values for the scale 
code - and the product name - from the user, and writing it to the end of the existing text file. 
This way, the new item becomes a part of the existing list, and the user now has the ability to search for it.

Daniel Trakas
'''

# For sys.exit, in order to allow user to exit program.
import sys

# Function that reads txt file, and converts lines into a dictionary.
def createDict():
    # Opens file for reading and initializes dictionary.
    fhndl = open("ItemCodes.txt", "r")
    
    # Initializes dictionary as global, so it can be accessed by other functions.
    global itemDict
    itemDict = {}

    # Reads line and splits at comma, then adds line to dictionary, and stript \n character.
    for line in fhndl:
        itemCode, itemName = line.split(",")
        itemName = itemName.strip() 
        itemDict[itemCode] = itemName

    # Closes file.
    fhndl.close()


# Function that searches for user-input query.
def searchItems(query):
    print("---------- SEARCHES FOR \""+query+"\" ----------")
    results = 0

    # Loops through dictionary of items, appends matching items to list as tuple, and prints list.
    searchList = []

    for key in itemDict:
        # Uses string.casefold() for case insensitive comparison.
        if query.casefold() in itemDict[key].casefold():
            searchList.append((key,itemDict[key]))
            results += 1
    
    # Prints results.
    for i in range(0, len(searchList)):
        print(searchList[i])
    
    # Prints number of results found (in case none are found).
    print(results, "results found.")
  

# Function that allows user to add new item to existing list.
def addItems(code, name):
    # Opens file for appending.
    fhandl = open("ItemCodes.txt", "a")

    # Checks if item code already exists.
    if str(code) in itemDict:
        print("Item code already exists, try again.")
    else:
        # Appends new code/name to the existing list.
        fhandl.write("\n"+str(code)+","+str(name))
        print("Item added successfully.")
    
    # Closes file, and outputs, and updates dictionary. 
    fhandl.close()
    createDict()


# Creates dictionary, outputs options, and prompts a user selection.
createDict()
print("Please input a selection and press enter:")

# Initializes user input variable.
userInput = ""

# Loop continues while input is not QUIT, to allow for multiple options.
while userInput != "QUIT":
    print("1) Search for an item.")
    print("2) Add a new item to the system")
    userInput = input("Type \"QUIT\" at any time to exit.\n")

    # If 1 is input, the item search option is displayed.
    if userInput == '1':
        print("Type \"BACK\" to return to the main menu.")
        print("Enter a query to search for.")
        searchQuery = input()

        # Goes back if "BACK" is input, otherwises searches for user query.
        if searchQuery != "BACK":
            searchItems(searchQuery)
        else:
            continue
    
    # If 2 is input, the item add option is displayed.
    if userInput == '2':
        print("Type \"BACK\" to return to the main menu.")
        itemCode = input("Please enter the new item's code: ")
        itemName = input("Please enter the new item's name: ")

        # Goes back if "BACK" is input, otherwises adds item with user's code and name.
        if itemCode == "BACK":
            continue
        elif itemName == "BACK":
            continue
        else:
            # Verifies that an integer has been input for the item code.
            try:
                addItems(int(itemCode), itemName)
            except:
                print("Only integers are allowed for an item code.")

# Uses sys to terminate program if "QUIT" is input.
if userInput == "QUIT":
    sys.exit()