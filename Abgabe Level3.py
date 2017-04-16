# Game has 3 or more levels and each level contains 4 or more blanks to fill in
blanks = ["---1---","---2---","---3---","---4---"]
sentence_easy = "A game has ---1--- innings. There is an infield and a ---2---. The person on the mound is the ---3--- and throw the ball to the ---4---"
sentence_medium = "In Baseball we habe ---1--- player in the feld for the defents team. There are ---2--- outfielder. ---3--- is when you hit the ball over the outfield. A ball in the air calls a ---4---"
sentence_hard = "---1--- is the first german Baseballplayer in the MLB. A ---2--- ist the best thing a batter can do. 3 strikes then the Batter is ---3---. Best position in the field ---4---"

final_sentence = []

answers_easy = ["9", "outfield", "pitcher","catcher" ]
answers_medium = ["9", "3", "homerun", "flyball"]
answers_hard = ["max", "homerun", "out", "shortstop"]

def word_in_pos(word, parts_of_speech): 
    # Check is the part is a part of blanks
    for pos in parts_of_speech:
        # goint to the elements of the list
        if pos in word:
            return pos
            # returns the element if found
    return None
    #returns None if the element is not found
                   
def gameplay(final_sentence,sentence,answer,blanks): #Game logging
    sentence = sentence.split()# into a list
    # print sentence
    counter = 0 # for fail trys
    answerscounter = -1 # for the number in answer
    for i in sentence:
        replacement = word_in_pos(i,blanks)
        if replacement != None: # if there is flied to fill out something
            user_input = raw_input("Your answer for " + replacement + ":")
            answerscounter += 1 # find the correct position in the answer list
            if user_input == answer[answerscounter]:
                i = i.replace(replacement,user_input)
                counter = 0
                print "Correct, -->" + user_input
            while user_input != answer[answerscounter] and counter < 3: # if answer is not correct
                user_input = raw_input("Not correct, try again:")
                counter +=1
            if counter == 3: # after 3 time with the wrong answer
                print "Anwers where not correct, please find below the solution  "
                print answer # showing solutions
                break
            i = i.replace(replacement,user_input)
            final_sentence.append(i)
        else:
            final_sentence.append(i)
    final_sentence = " ".join(final_sentence)
    return final_sentence # pint out list

print "" # just that it looks nicer
print "Welcome to the game where you learn some Baseball rules" #Welcome text
print ""# just that it looks nicer
user_input = 0 # level that the user picks
count = 0 # trys of enter a correct level
text = "Please select a level - easy, medium, or hard:  "
while user_input not in ["easy", "medium", "hard"]: # to ensure that the player picks the right number
    if count == 0: # first time - full sentence will not be shown again
        user_input = raw_input (text)
        count += 1
    if user_input not in ["easy", "medium", "hard"]: # ask for doing it again
        user_input = raw_input ("Easy, medium, or hard:  ")


print ""
print ""
print ""
print "Lets start"
print ""

if user_input == "easy":
    print sentence_easy
    print gameplay(final_sentence,sentence_easy,answers_easy,blanks)
if user_input == "medium":
    print sentence_medium
    print gameplay(final_sentence,sentence_medium,answers_medium,blanks)
if user_input == "hard":
    print sentence_hard
    print gameplay(final_sentence,sentence_hard,answers_hard,blanks)
