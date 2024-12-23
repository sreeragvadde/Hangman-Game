def input_split(letter_list:list) ->None:
    """ Takes the input of the answer and breaks it down into a list if letters """
    answer=input("enter answer: ")
    answer=answer.lower()
    answer_list=answer.split()
    for i in answer_list:
        for a in i:
            letter_list.append(a)

def checker(letter_list:list,i:int,letter_guess_wrong:list,letter_guess_correct:list) ->int:
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
        print(f"wrong letter {10-i} are left")
        print(f'letter that you guesse that are wrong {letter_guess_wrong}')
        print(f'letter that you guesse that are correct {letter_guess_correct}')
    else:
        print(f"correct")
        letter_guess_correct.append(guess)
        print(f'letter that you guesse that are wrong {letter_guess_wrong}')
        print(f'letter that you guesse that are correct {letter_guess_correct}')
    return i

def main():
    letter_list=[]
    letter_guess_wrong=[]
    letter_guess_correct=[]
    input_split(letter_list)
    i=0
    while letter_list!=[] and i<10:
        i=checker(letter_list,i,letter_guess_wrong,letter_guess_correct)
    if i==10:
        print("you fail")
    else:
        print("you got it right")

main()
