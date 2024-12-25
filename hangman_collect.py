import tkinter as tk
from tkinter import messagebox
def input_split(letter_list:list,answer_1:str) ->None:
    """ Takes the input of the answer and breaks it down into a list if letters """
    answer_1=answer_1.lower()
    answer_list=answer_1.split()
    for i in answer_list:
        for a in i:
            letter_list.append(a)
    return answer_1

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

def hangman(answer_1:str):
    letter_list=[]
    letter_guess_wrong=[]
    letter_guess_correct=[]
    answer=input_split(letter_list,answer_1)
    for i in range(len(answer)-1):
        if answer[i]==" ":
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

def main(answer_1:str):
    # choice=input("do you want to play hangman(y/n): ")
    f=open("senteces used.txt","a")
    answer=hangman(answer_1)
    f.writelines(answer+"\n")
    # choice=input("do you want to play hangman(y/n): ")
           
    f.close()

def gui():
    root=tk.Tk()
    label=tk.Label(root,text="Hangman ",font=("Arial",12))
    label.pack()
    textbox=tk.Text(root,height="5",font=("Arial",13))
    textbox.pack()
    # check_box=tk.IntVar()
    # check=tk.Checkbutton(root,text="Do you want to play Hangman",font=("Arial",13),variable=check_box)
    # check.pack()
    buttton=tk.Button(root,text="Do you want to play Hangman",font=("Arial",13),command=lambda:main(textbox.get("1.0",tk.END)))
    buttton.pack()
    root.mainloop()
    


gui()
