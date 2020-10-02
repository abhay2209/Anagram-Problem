import sys
import time

def countChars(userString , element): #This function checks the occurence of 
    count = 0
    size = len(userString)

    for e in range(size):      
        if userString[e] == element :
            count += 1                 #Increasing the counter at each encounter of the 'element alphabet'
    return count



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
        
        alphabet = [0]*26     # This is like a hash table, It will store the count of a particular letter at it's position in alphabetical order.
        ourWords = ""

        print('-----------------------------')
        userString = input ("What word do you want to look for? ")

        while len(userString) == 0:     # Making sure that the input is not empty
            userString = input ("Invalid argument, please enter a valid word: ")
                
        userString = userString.lower() # Every input and dictionary word should be lower

        #Call this one a preprocessing function which takes the user input and hashes it in the above created array
        for i in range(len(userString)): 
            alphabet[ ord(userString[i]) - 97 ] = countChars(userString,userString[i])

            #for i in range(26): [This was for testing my preprocessing]
                #print(alphabet[i])

        t3 = time.time()
            #We go line by line
        for line in f:
            dictionaryWord = f.readline()
            dictionaryWord = str(dictionaryWord.lower()) # Lowering the case
                #print (ord(str(dictionaryWord[0]))) [for test purposes]

                #****if dictionary word is 'a', length calculated by len function was was 2***
            if (len(userString) == len(dictionaryWord)-1): # Only checking a word if it is similar length 
                word = True                              # Set to true as it passed our first condition
                for i in range(len(dictionaryWord) - 1):   # For every letter of the dictionary
                    letterCount = countChars(dictionaryWord, dictionaryWord[i]) # counting each letter
                    if alphabet[ord(str(dictionaryWord[i])) - 97] != letterCount: # if the count for a letter is not same as our created array (Hash Table)
                        word = False                                              # We make it False and break
                        break
                    
                if word == True:               # For all true word
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

        while chooseOption != 'search'  and  chooseOption != 'exit':                  # making sure a valid argument is enteres by the user
            chooseOption = input ('Invalid argument, enter either search or exit: ')
            chooseOption = chooseOption.lower()
            
    print("Program ended with exit")       
    f.close()
 

if __name__ == "__main__":
    main()









    

    
