from random import randint #imports the random module#

def print_heading(Header): #defines the heading function#
    print('\n---------------------------------------')
    print('#',Header.center(35),'#')
    print('---------------------------------------\n')
    
def Exploded(Roll, DiceRollList, Side): #defines the exploding dice function#
    Total = sum(DiceRollList) #Adds the Roll to the total#
    print('    Kaboom')
    Roll = randint(1, Side) #Randomises a roll#
    if Roll == Side:
        DiceRollList.append(Roll) #Appends the roll to the list#
        Total = sum(DiceRollList) #Adds the Roll to the total#
        print('    Rolled a',Roll,', Exploding total of', Total)
        Exploded(Roll, DiceRollList, Side)
    else:
        DiceRollList.append(Roll) #Appends the roll to the list#
        Total = sum(DiceRollList) #Adds the Roll to the total#
        print('    Rolled a',Roll,', Exploding total of', Total)

print_heading('Welcome To The Dice Roller')
while True: #Starts the program and creates a loop which runs infinitly until it is exited by the user#
    try:
        Enter = input("\nEnter a roll ('h' for further help, 'x' to exit) : ").lower()
        if Enter == 'h': #If the user's input is h then it will print the help message#
            print_heading('Help')
            print("Enter a dice roll as shown. '(amount of dice)d(how many sides)'.\ne.g. Enter 4d6 to roll four six-sided dice.\n\nAdd ! to the end, (4d6!), for a 'Exploding Dice'.\nDice that roll the maximum number are then re-rolled and are added.")
        elif Enter == 'x': #If the user's input is x then it will end the program#
            print('\n')
            print_heading('Now Closing')
            break

        elif Enter.isalnum() and 'd' or '!' in Enter: 
            if Enter[-1] != '!': #If the user's input doesn't have a ! in it then Exploding will be set to false, meaning the roll is not exploding
                ExplodingDice = False
            else: #If the user's input does have a ! in it then Exploding will be set to true, meaning the roll is exploding
                ExplodingDice = True
            EnterEdited = Enter.replace('!','') #This replaces the ! in the value Enter (user input) which allows the list to eliminate the ! from the array#
            DiceRollList = EnterEdited.split('d') #This splits the character 'd' from the array so it is not included with the numbers#
            Amount = DiceRollList[0] #Amount is the Quantity / amount of times the dice it to be rolled. Sets it to the first value#
            Side = DiceRollList[1] #Side is the amount of sides that will be present on the rolled dice. Sets it to the second value#
            Amount = int(Amount) #Converts Amount to an integer#
            Side = int(Side) #Converts Side to an integer#
            if Side < 2:
                print('This is an invalid amount of sides. Input must not have less than 2\n')
                print_heading('Welcome To The Dice Roller')
                continue
            DiceRollList = [] #This is a list which rolled dice will be appended to#
            Counter = int(Amount) #This is a counter which will decrease with every roll, until it hits '0'#
        
            if ExplodingDice == False:
                print('\nRolling Dice Combination of',Enter,'(Not Exploding)')
                while Counter > 0:
                    Roll = randint(1, Side) #Randomises a roll#
                    print('\n   Rolled a',str(Roll))
                    Counter = Counter - 1 #decreases the counter by 1#
                    DiceRollList.append(Roll) #Appends the roll to the list#
            else:
                print('\nRolling Dice Combination of',Enter,'(Exploding)')
                while Counter > 0:
                    Roll = randint(1, Side) #Randomises a roll#
                    print('\n   Rolled a',str(Roll))
                    if Roll == Side:
                        DiceRollList.append(Roll) #Appends the roll to the list#
                        Exploded(Roll, DiceRollList, Side) #calls the Exploded function#
                        Counter = Counter - 1 #decreases the counter by 1#
                    else:
                        DiceRollList.append(Roll) #Appends the roll to the list#
                        Counter = Counter - 1 #decreases the counter by 1#
                        
            print_heading('Roll Statistics') #This displays the header
            Total = sum(DiceRollList) #This calculates the Total number of Dice Rolled numbers#
            Average = Total / int(Amount) #This calculates the Average by dividing the Amount of Dice with the total#
            print('Rolls:    ',DiceRollList) #Displays the rolls#
            print('Total:    ',sum(DiceRollList)) #Displays the Total for the roll#
            print('Average:  ',(Average)) #Displays the average for the roll#
            MinRoll = min(DiceRollList) #This calculates the minimum number that was rolled during that session#
            MaxRoll = max(DiceRollList) #This calcuates the maximum number that was rolled during that session#
            print('Minimum   ',MinRoll,'(',DiceRollList.count(MinRoll),'Occurences )') #This displays the minimum roll and calculates the occurence amount for the minimum number that was rolled#
            print('Maximum   ',MaxRoll,'(',DiceRollList.count(MaxRoll),'Occurences )') #This displays the maximum roll and calculates the occurence amount for the maximum number that was rolled#
            
        else: #This will display a message if the user inputs an invalid input#
            print('Invalid input, please type a valid input')
            print_heading('Welcome To The Dice Roller')
            continue
    except IndexError:
        print('Invalid input, please type a valid input') #Performs IndexError handling for when the user inputs random letters#
    except ValueError:
        print('Invalid input, please type a valid input') #Performs ValueError handling for when the user inputs random letters with a d in it#
