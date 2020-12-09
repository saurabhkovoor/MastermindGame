import random #This is to import the random module so we can randomly generate the 4-colour code sequence later in line 64

#This void function is to display/print the rules and show the user how to play
def instructions(): 

    print('INSTRUCTIONS')
    print('1. The CodeSetter will set a hidden sequence of four colours')
    print('   Colours Available: RED(R), BLUE(B), YELLOW(Y), GREEN(G), ORANGE(O), PINK(P)')
    print('2. You, the CodeBreaker, need to guess the 4 Colours')
    print('3. When prompted, enter the first letter of the Colours according to their positions')
    print('   Eg: "R", "B", "Y", "G", "O", or "P" (It can be in lower-case too)')
    print("4. To WIN, you'll need to guess the 4-Colour Code correctly in 10 Steps or Less. If not you LOSE.")
    print("5. Repeating the SAME COLOURS is ALLOWED\n6. You can input the colours in either capital letters or small letters.\n")

#This void function displays a goodbye message then stops the execution of the game with quit(). Its called twice in this game.
#If user chooses to Quit Game at the OPENING PAGE(line 212 and 224) this function will be called
def quit_game(): 

        print("Feel free to play anytime!")
        quit()

#This void function asks user if they want to play again. Its called at the end of the main game/end of play_game().
def play_again():
    
    #This while loop along with "continue" used as data validation technique where users can only enter y or Y or n or N
    while True: 
        
        #User can type in either y or Y to continue playing or n or N to quit as the input will be lower-cased later
        askplayagain = input("Would you like to play again?(y/n): ").lower()
        
        
        #if y or Y is inputted, it'll call the play_game() function to begin main game again
        if askplayagain == "y":
            play_game()

        #if n or N is inputted, it'll print/display thank you message to user and stop execution of program with quit() function
        if askplayagain == "n":
            print("Thank You for Playing!")
            quit()

        #if user enters something other than y/Y/n/N  error message will be displayed and with "continue" the while loop is repeated to obtain appropriate input
        else: 
            print()
            print('ERROR! Enter either "y" (to Continue) or "n" (to Quit).')
            print()
            continue
 
#This function is to start playing the main game when called
def play_game():

    #List is used to store the 6 available colours' representative letters
    colour_list = ["R", "B", "G", "Y", "O", "P"]

    print("4-Colour sequence generating...\n")
    print("When prompted, enter the representative letter for the colours.(Either in capital or small letters)")
    print("Colours to choose: Red(R), Blue(B), Yellow(Y), Green(G), Orange(O), Pink(P)\n")
    #This is to assign False boolean value to variable success so we can use this variable later in line 152 to determine if player wins or loses
    success = False 
   
    hiddencode = [] #to intialize the value of variable hiddencode as an empty set

    #Bottom two lines is to randomly generate the hidden 4-colour code sequence then append it to hiddencode list
    for x in range(4):
        hiddencode.append(random.choice(colour_list))
    
    #print(hiddencode) 
    #The above line is for developer to see the hiddencode for determining any errors. When presenting to players hide this line as comment
    
    '''
    The next part, to allow 10 trials to guess the 4-colour hiddencode.
    Users can enter their code individually for each position 
    Then guesses will be stored in a list(user_guess), then list is checked and compared with the hiddencode
    Each guess is validated to capture errors so that users don't input inavailable characters or more than one characters in one guess
    '''
    for c in range(10):

        user_guess = [] #initialise value of user_guess as empty set to be appended later with user's colour input

        print("Trial(s): " + str(c + 1) + "/10 \n") #display how many trials taken so far

        for x in range(4): #for loop used to repeat this section 4 times so 4-colour code can be formed

            #while loop, continue and break are used for data validation and error handling
            #users can only enter valid colours in colour_list (i.e. r/b/g/y/o/p or R/B/G/Y/O/P)
            while True:
                colourinp = input("ENTER the Colour for Position " + str(x+1) + " (R/B/G/Y/O/P): ")
                colourinp = colourinp.upper() 
                #this above line capitalises the colourinp so it'll be standardised and easily checked with hiddencode. Users can enter uppercase or lower case
                
                if colourinp not in colour_list: #error message is displayed if user doesnt enter either r/b/g/y/o/p 
                    print('ERROR! Only choose ONE of the AVAILABLE colours (e.g.,"R", "B", "G", "Y", "O", or "P").\n')
                    continue #if they enter invalid colour, "continue" is executed and while loop is repeated to prompt for appropriate input
                
                else: #if user enters valid colour, input is appended to user_guess, and while loop not repeated because of "break"
                    user_guess.append(colourinp)
                    break
        
        #This part is to display the 4-colour code sequence inputted by user at each trial
        print("\nYour guess was: ", end= "")
        print(*user_guess, sep ="-")
        print()   
        
        #Main logic of the Mastermind Game to determine no. of correct colour correct position and correct colour but wrong position
        #Initialize value of black_pegs(correct colour and correct position) and white_pegs(correct colour but wrong position) to zero
        black_pegs = 0
        white_pegs = 0

        #for loops used to repeat 4 times the comparing between guess and hiddencode since both consist of 4 colours
        for x in range(4): 

            '''for this code, if guess colour = hiddencode colour at the particular position, black_pegs is incremented 
            colours which are matched in both list are assigned (matched-blackpeg)
            If the colours in both list are assigned (matched-blackpeg) they won't be assigned again when checking for whitepegs, so no. of white_pegs don't increase'''
            if user_guess[x] == hiddencode[x]:
                black_pegs = black_pegs + 1
                user_guess[x] += "(matched-blackpeg)"
                hiddencode[x] += "(matched-blackpeg)"
            
            #The lines 122-123 are for developers to see the background assigning of the blackpegs more clearly.    
            #It's also to visualise the logic code clearly so you can spot errors easier
            #Remove the comments below to see the assigning take place
            #print("Hidden code:",hiddencode)
            #print("User guess :", user_guess) 

        #for loops used to repeat 4 times comparing between guess and hiddencode checking for white_pegs(correct colour wrong position) since both consist of 4 colours  
        for x in range(4):
            
            '''similar to line 116-117, colours in hiddencode assigned (matched-whitepegs) if present in guess so they wont be matched to again by another same colour in the guess
            hence no unnecessary increase in white_pegs 
            if the guess colour is not equal to corresponding hiddencode colour in a particular position but present in hiddencode overall then white_peg is incremented'''
            if user_guess[x] != hiddencode[x] and user_guess[x] in hiddencode:
                white_pegs = white_pegs + 1
                hiddencode[hiddencode.index(user_guess[x])] += "(matched-whitepeg)"

            #The bottom line is for developers to see the background assigning of the whitepegs more clearly
            #print(hiddencode)
        
        #This is to remove the "(matched)" identifier from the colours in hiddencode and returns the hiddencode to normal    
        for x in range(4):
            if len(hiddencode[x]) > 1:
                hiddencode[x] = (hiddencode[x])[0] 

        #To display to user how many are Black Pegs and White Pegs
        print("Correct Colour and Correct Place/ Black Peg(s):", black_pegs)
        print("Correct Colour but Wrong Place/   White Peg(s):", white_pegs)
        print()

        #Next part is when user guesses all 4 colours correctly
        #If user manages to guess all four colours in the correct position then black_pegs = 4
        #variable success will be assigned a True boolean value and "break" is used to exit the main for loop in line 75
        if black_pegs == 4:
            success = True
            break

    #if user guesses all 4 colours correctly, statements inside this "if" block executed 
    #here congratulatory message is printed, hiddencode displayed again for confirmation, and number of trials taken shown to user
    if success:

        print("CONGRATS! You WON. The hidden code was", end=' ')
        print(*hiddencode, sep ="-")
        print("Number of Trials: " + str(c+1))
        print()
        play_again() #at the end here, play_again() function is called to ask user if they want to play again
        
    #this condition occurs instead when user doesn't guess hiddencode correctly and trials exceed more than 10, hence success = False as in line 58
    #logical operator NOT used to complement the value of success and execute the statements when success = False
    #this prints message that user has lost, and displays the correct hiddencode to user
    elif not success:

        print("Oh No! You LOST. You've run out of Trials. The hidden code was", end = ' ')
        print(*hiddencode, sep ="-")
        print()
        play_again() #at the end play_again() function called to ask user if they want to play again
        

#Displays OPENING PAGE from line 115-150. The first user-interactive menu
print("WELCOME TO THE MASTERMIND GAME")
print("By Saurabh Kovoor")
print("******************************\n")
print("[1] Start Game \n[2] How to Play? \n[3] Quit Game \n") #displays to user what they can select and what to enter

'''while loop and continue command used for data validation and error handling where users cannot enter anything other than 1/2/3 
or the loop will be repeated prompting for proper input''' 
while True:

    #capture user input of the action with input() and assign to "selection" variable
    selection = input("Choose an action by entering its number (1/2/3): ")
    print()

    #if, elif and else statements used for decision-making
    #If user enters 1 then play_game() function called to begin main game
    if selection == '1':
        print("Lets Play!\n")
        play_game()

    #if user enters 2 instructions() function called to display instruction to user
    elif selection == '2':
        instructions()

        #While and continue used for data validation where users can't enter anything other than 1/2
        #True used as condition so while loop will be executed straight away
        while True:
            print("[1] Start Game \n[2] Quit Game \n") #choices of actions displayed to user
            selection = input("Choose an action by entering its number (1/2): ") #user input captured with input() and assigned to variable, selection
            
            #if user enters 1, play_game() function called to begin main game
            if selection == '1':
                play_game()
            
            #if user enters 2, quit_game() function called to display goodbye message and end program execution
            elif selection == '2':
                quit_game()
            
            #else statement used for error handling, if user enters anything other than 1/2
            #error message displayed and continue command repeats the loop to ask input again
            else:
                print()
                print("ERROR! Enter either 1 or 2.")
                print()
                continue

    #if user enters 3 quit_game() function called, exit message displayed, and program closed with quit() function
    elif selection == '3':
        quit_game()
     
    #This else statement is for error handling where error message displayed if user enters anything other than 1/2/3
    else:
        print("ERROR! Enter either 1,2, or 3.")
        continue #continue used to repeat the while loop(line 184) and ask for input again
