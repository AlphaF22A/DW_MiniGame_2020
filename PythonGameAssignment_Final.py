import random

Countries = ["the United States", "Canada", "the United Kingdom", "France", "Germany", "Denmark", "India", "Singapore", "Taiwan", "South Korea", "Japan", "Australia", "the Netherlands", "Ireland", "Chile"]
Capitals = ["Washington DC", "Ottawa", "London", "Paris", "Berlin", "Copenhagen", "New Delhi", "Singapore", "Taipei", "Seoul", "Tokyo", "Canberra", "Amsterdam", "Dublin", "Santiago"]

Aircraft = ["F22", "F35","F15E","F16C", "F/A18F", "B1B", "B2", "B52", "Concorde", "Boeing 747", "Boeing 787", "Airbus A380"]
Nicknames = ["Raptor", "Lightning", "Strike Eagle", "Fighting Falcon", "Super Hornet", "Lancer", "Spirit", "Stratofortress", "Queen of the Skies", "Jumbo Jet", "Dreamliner", "Superjumbo"]

Year = ["1993", "1996", "1997", "1999", "2004", "2006", "2007", "2008", "2009", "2010", "2016"] 
Winner = ["Prost", "Hill", "Villeneuve", "Hakkinen", "Schumacher", "Alonso", "Raikkonen", "Hamilton", "Button", "Vettel", "Rosberg"]

# This statement dictates whether the game is currently in playing mode
play = True 

while play:
    
    # Start questions for name and level of difficulty
    PLName = input("Hi there! What is your name? ")
    category = str(input("Pick a category: Geography, Planes, Formula 1: "))
    
    while category != "Geography" and category != "Planes" and category != "Formula 1" :
        category = str(input("Error! Pick a category from the following: Geography, Planes, Formula 1. Else, the program will cease, and you must restart the console! "))
    
    #Correct & Wrong answer counters
    NumberofCorrect = 0
    NumberofWrong = 0
    
    #Creating list of previous questions to eliminate duplicates
    PreviousQuestions = []
    
    #Ensuring quiz runs up till 5 correct questions
    while NumberofCorrect < 5 :
        if NumberofWrong == 5:
            break
    
    # Launch Geography category quizzes
        if category == "Geography" :
            print("Alright, " + PLName + ". You have chosen the category Geography!")
        
            #List comprehension so that random selection only randomly selects from those not yet asked, hence no duplicates
            Bank = [x for x in Countries if x not in PreviousQuestions]
            
            w = random.choice(Bank)
            PreviousQuestions.append(w)
            
        
            print("What is the capital of " + w +"?")
            #print(w)
            x = (Countries.index(w))
        
            Answer = str(input("Your answer is: "))
            y = Answer
            
            if y in Capitals:
            
                if x == (Capitals.index(y)):
                    print ("Correct!")
                    NumberofCorrect += 1
                else:
                    print ("WRONG!")
                    NumberofWrong += 1
            else:
                    print ("WRONG!")
                    NumberofWrong += 1
            
            print ("Correct Answers: ", NumberofCorrect)
            print ("Wrong Answers: ", NumberofWrong)
            
        #Launch Planes category quizzes
        if category == "Planes" :
            print("Alright, " + PLName + ". You have chosen the category Planes!")
        
            Bank = [x for x in Aircraft if x not in PreviousQuestions]
            
            w = random.choice(Bank)
            PreviousQuestions.append(w)
        
            print("What is the nickname of the " + w +"?")
            #print(w)
            x = (Aircraft.index(w))
        
            Answer = str(input("Your answer is: "))
            y = Answer
            
            if y in Nicknames:
            
                if x == (Nicknames.index(y)):
                    print ("Correct!")
                    NumberofCorrect += 1
                else:
                    print ("WRONG!")
                    NumberofWrong += 1
            else:
                    print ("WRONG!")
                    NumberofWrong += 1
            
            print ("Correct Answers: ", NumberofCorrect)
            print ("Wrong Answers: ", NumberofWrong)
            
        #Launch Planes category quizzes
        if category == "Formula 1" :
            print("Alright, " + PLName + ". You have chosen the category Formula 1!")
        
            Bank = [x for x in Countries if x not in PreviousQuestions]
            
            w = random.choice(Year)
            PreviousQuestions.append(w)
        
            print("Which driver won the " + w +" F1 title? Type out their last name (eg. If it is Lewis Hamilton, type out Hamilton)")
            #print(w)
            x = (Year.index(w))
        
            Answer = str(input("Your answer is: "))
            y = Answer
            
            if y in Winner:
            
                if x == (Winner.index(y)):
                    print ("Correct!")
                    NumberofCorrect += 1
                else:
                    print ("WRONG!")
                    NumberofWrong += 1
            else:
                    print ("WRONG!")
                    NumberofWrong += 1
            
            print ("Correct Answers: ", NumberofCorrect)
            print ("Wrong Answers: ", NumberofWrong)
                    
    #Ceasing or restarting the game once player hits 5 correct answers
    if NumberofCorrect == 5:
        print ("Congrats! You have completed the quiz!")
        
        playagain = 0
        playagain = int(input("You want to play again yeah? Enter 1 for Yes or 0 for No: "))
        if playagain == 1:
            NumberofCorrect == 0
            NumberofWrong == 0
        if playagain == 0:
            print("Thanks for playing " + PLName +"!")
            play = False
            
            break
        
    elif NumberofWrong == 5:
        print ("Better luck next time!")
        playagain = 0
        playagain = int(input("Do you want to go again? Enter 1 for Yes, or 0 for No: "))
        if playagain == 1:
            NumberofCorrect == 0
            NumberofWrong == 0
        if playagain == 0:
            print("Thanks for playing " + PLName +"!")
            play = False    
 