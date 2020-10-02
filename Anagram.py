import sys
import time


def main():
    
    fileName = sys.argv[1]
    t1 = time.time()
    f = open(fileName, "r")
    t2 = time.time()

    print(" File loaded in:", t2-t1 ,"seconds")
    print('Enter "search" if you want to look for a word')
    print('Enter "exit" if you want to exit the program')
    
    chooseOption = input('Your option: ')
    chooseOption = chooseOption.lower()

    while chooseOption != 'search'  and  chooseOption != 'exit': # making sure the argument given by the user is valid
        chooseOption = input ('Invalid argument, enter either search or exit: ')
        chooseOption = chooseOption.lower()
        #print(chooseOption)


    while chooseOption == 'search':
        
        alphabet = [0] * 26     # This is like a hash table, It will store the count of a particular letter at it's position in alphabetical order.
        ourWords = ""

        print('-----------------------------')
        userString = input ("What word do you want to look for? ")
       
        while len(userString) == 0 or userString.isalpha() == False:     # Case where input can be empty or have numeric
            userString = input ("Invalid argument, please enter a valid word: ")
                
        userString = userString.lower() # Every input and dictionary word should be lower

        #Call this one a preprocessing function which takes the user input and hashes it in the above created array
        for i in range(len(userString)): 
            alphabet[ ord(userString[i]) - 97 ] += 1

            #for i in range(26): [This was for testing my preprocessing]
                #print(alphabet[i])

        t3 = time.time()
            #We go line by line
        for line in f:
            dictionaryWord = f.readline()
            dictionaryWord = str(dictionaryWord.lower()) # Lowering the case
            
            if (len(userString) == len(dictionaryWord)-1):
                word = True
                checkWord = [0] * 26
                for i in range(len(dictionaryWord) - 1): 
                    checkWord[ ord(str(dictionaryWord[i])) - 97] += 1  # Doing same as we did for our input word by creating an array for dictionary word.
                
                for i in range(26):          # Comparing two arrays
                    if (checkWord[i] != alphabet[i]):
                        word = False         #as to arrays weren't same
                        break

                if word == True:                # For all true words
                    ourWords += dictionaryWord  # We print it and proceed to our next step
               
        t4 = time.time()
        if ourWords == "":
            print('No anagram found for given word')
        else:
            print('Words found are: ')
            print(ourWords, end="")

        print('-----------------------------')

        print("Time taken for the process: ", t4-t3, "seconds")
        
        f.seek(0)
        print('-----------------------------')
        chooseOption = input('Enter "search" to search more or enter "exit" to end: ') # To ask if user wantes to look for more words
        chooseOption = chooseOption.lower()

        while chooseOption != 'search'  and  chooseOption != 'exit':                  # Making sure a valid argument is entered
            chooseOption = input ('Invalid argument, enter either search or exit: ')
            chooseOption = chooseOption.lower()
            
    print("Program ended with exit")       
    f.close()
 

if __name__ == "__main__":
    main()









    

    
