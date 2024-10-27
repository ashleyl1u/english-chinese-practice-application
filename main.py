#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
A text file with English to Chinese translations of words will be read into 
the program and organized into specific lists (eng[],pin[]). The user will 
first be asked if they want to practice/test their English translation or C
hinese translation. The user will then be able to choose between two modes, 
practice and test. The test mode tests the user on the translation of the word 
by asking them, “What is the translation of:  ___?”. The user will then type 
in their answer (the translation of the word). After every word is tested 
(words are only tested ONCE), the percentage of how many the user got correct 
will be written onto an output text file called test_scores.txt. Similarly to 
the test mode, the practice mode will test the user on the translation of a 
word by asking, “What is the translation of:  ___?” and the user will answer 
by typing in their answer. But instead of testing the user on the translation 
of a word only once, the user will be able to test a word as many times as 
they need. After all words have been tested, the percentage will not be based 
on how many translations were correct, but how many translations of each word 
were correct. This information will also be written onto a text file but into 
another output file called practice_scores.txt. 

For the Chinese it will be shown through pinyin. The ‘_’ character separates 
the word and the tone of the word. The structure is: pinyin_tone.

'''


import random #importing random module

#Purpose: Inputs the words from a file, and organizes data into lists
def get_words():
    dic = open('words.txt',"rt")
    for line in dic:
        l=line.split( )
        eng.append(l[0])
        pin.append(l[1])
    dic.close()
    
#Purpose: Searches a list(arr) for a specific element(find) and returns its index(i)
def search(find,arr):
    size = len(arr)
    for i in range (0,size):
        if arr[i] == find:
            return i
        
#Purpose: Ouputs/writes data into a file
def write_words(arr1,arr2,c,t):
    if mode == "practice":
        final_data = open("practice_results.txt","a")
        final_data.write("\n")
        final_data.write("Translation                     Correct %\n")
        
    if mode == "test":
        final_data = open("test_results.txt","a")
        final_data.write("\n")
        final_data.write("Translation \t\t\t\t        Correct % \n")
    
    for i in range ( 0,len(arr1)):
        correctness= (c[i]/t[i])*100 #dividng the number of correct answers with the number of wrong answers. Then multiplying by 100 to get the percentage
        correctness= round(correctness,2) # rounding to two decinal places 
        final_data.write(arr1[i]+" \t -> \t"+ arr2[i]+ " \t\t"+ str(correctness) +"% \n")
        
    final_data.close() #closing the output textfile
    
    
#Purpose: Used to check if the input is valid, if not the user has the ability to keep inputing until input is valid
def check_input(a1,a2,r) :
    while r != a1 and r != a2:
        r=input("Please enter a valid input! Valid Inputs: " +a1+" or " +a2+ "? \n")
        r=r.casefold()
        
    return(r)


#Purpose: Used to run the practice part of the program 
def practice (question,answer):
    size=len(question)
    tries=[] #list used to hold the number of practices of a word
    correct=[] #list used to hold the number of correct translation of a word 
    for i in range (size):
        tries.append(1) #populates the list wwith 1 because each word is practiced at least once 
        correct.append(0)
        
    
    while size >0: #keeps looping until all words in the list are gone. i.e until all words are practiced however many times you want
        print("\n")
        i=random.randrange(0,size) #generates a random word to practice
        u_answer= input("What is the translation of: "+question[i]+"\n")
        u_answer=u_answer.casefold()
        
        
        if u_answer == answer[i] :
            
            
            if translation == "english":
                add = search(question[i],pin)
                
            if translation == "chinese":
                add = search(question[i],eng)
            
            correct[add]+=1 #adds one to the correct list
            
            
            print("Correct!")
            print("\n")
            again=input("Do you still want to continue practicing this word? \n")
            again=again.casefold()
            again= check_input("yes","no",again)
            
            if again == 'no':
                question.pop(i) #removes question from the question list
                answer.pop(i) # removes answer from the answer list 
                
            if again == 'yes':
                tries[add]+=1 #adds one to the tries list if user wants to practice again
                    
        else:
            print("Wrong! :(")
            print("The correct answer was: "+answer[i])
            if translation == "english":
                add = search(question[i],pin)
                
            if translation == "chinese":
                add = search(question[i],eng)
                
            tries[add]+=1 #adds one to the tries list 
            
       
            
        size=len(question) #rechecking the size of the question list
    
    
    
    if translation =="english":
        write_words(eng,pin,correct,tries)
    if translation == "chinese":
        write_words(pin,eng,correct,tries)
    
    

#Purpose: Used to run the test part of the program
def test(question,answer):
    size=len(question)
    num_of_quest=size
    correct=0
        
    #loops until all questions are asked
    while size >0:
        print("\n")
        i=random.randrange(0,size)
        u_answer= input("What is the translation of: "+question[i]+"\n")
        u_answer=u_answer.casefold()
        
        
        if u_answer == answer[i] :
            print("Correct!")
            print("\n")
            correct+=1 #adds 1 to correct
            
        else:
            print("Wrong! :(")
            print("The correct answer was: "+answer[i])
            
       
        question.pop(i)
        answer.pop(i)  
        size=len(question)
    
    if translation =="english":
        write_words(["English"], ["Chinese"],[correct],[num_of_quest])
    if translation == "chinese":
        write_words(["Chinese"], ["English"],[correct],[num_of_quest])
        
    

eng=[] #list used to hold the english words
pin=[] #list used to hold the chinese (pinyin) words 

get_words() #used to populate the lists above


print("Welcome to my Porject :)!")

mode=input("Would you like to Practice or Test yourself? \n")
mode=mode.casefold()

#checks for valid input. Keeps checking until input is valid. 
mode=check_input("practice","test",mode)

print("\n\n")
print("English Translation: Chinese --> English")
print("Chinese Translation: English --> Chinese")
translation= input("Would you like to practice your English translation or Chinese translation? \n")
translation=translation.casefold()

translation=check_input("english","chinese",translation) #checks for valid input. Keeps checking until input is valid. 
    
if mode == 'practice':
    if translation == "english":
        practice(pin.copy(),eng.copy())
        
    if translation == "chinese":
        practice(eng.copy(),pin.copy())
    
if mode == 'test':
    if translation == "english":
        test(pin.copy(),eng.copy())
        
    if translation == "chinese":
        test(eng.copy(),pin.copy())
   
print("\n")
print("Finished! GreatJob!")
print("Check the textfiles for your scores!")





    
