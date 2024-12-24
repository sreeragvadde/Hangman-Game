def input_split(letter_list:list) ->None:
    """ Takes the input of the answer and breaks it down into a list if letters """
    answer=input("enter your sentence: ")
    answer=answer.lower()
    answer_list=answer.split()
    for i in answer_list:
        for a in i:
            letter_list.append(a)
    return answer

def checker(letter_list:list,i:int,letter_guess_wrong:list,letter_guess_correct:list,answer:str) ->int:
    """checks if the given letter is the answer and removes it if it exists"""
    guess=input("enter guess: ")
    guess=guess.lower()
    increment=0
    a=0
    while a<len(letter_list)-increment:
        if guess==letter_list[a]:
            letter_list.remove(letter_list[a])
            increment+=1
        a+=1
    if increment==0:
        i+=1
        letter_guess_wrong.append(guess)
        print(f"wrong guess {10-i} are left")
    else:
        print(f"correct")
    print(f"what you guessed till now {position(answer,guess,letter_guess_correct)}")
    print(f'letter that you guesse that are wrong {letter_guess_wrong}')
    return i

def position(answer:str,guess:str,letter_guess_correct:list) ->list:
    """prints the position of the letter with the spaces"""
    for i in range(len(answer)):
        if answer[i] == guess:
            letter_guess_correct[i]=guess
        elif answer[i]==" ":
            letter_guess_correct[i]=" "
    return letter_guess_correct

def hangman():
    letter_list=[]
    letter_guess_wrong=[]
    letter_guess_correct=[]
    answer=input_split(letter_list)
    for i in answer:
        if i==" ":
            letter_guess_correct.append(" ")
        else:
            letter_guess_correct.append("_")
    i=0
    print(letter_guess_correct)
    while letter_list!=[] and i<10:
        i=checker(letter_list,i,letter_guess_wrong,letter_guess_correct,answer)
    if i==10:
        print(f"you fail the answer is {answer}")
    else:
        print("you got it right")
    return answer

def main():
    choice=input("do you want to play hangman(y/n): ")
    f=open("senteces used.txt","w")
    while choice=="y" or choice=="Y":
        answer=hangman()
        f.writelines(answer+"\n")
        choice=input("do you want to play hangman(y/n): ")
           
    f.close()
main()