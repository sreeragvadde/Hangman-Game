import tkinter as tk
from tkinter import simpledialog
def input_split(letter_list:list) ->str:
    """ Takes the input of the answer and breaks it down into a list if letters """
    answer_1 = simpledialog.askstring("Input", "Enter the sentence")
    answer_1=answer_1.lower()
    answer_list=answer_1.split()
    for i in answer_list:
        for a in i:
            letter_list.append(a)
    return answer_1

def checker(letter_list:list,i:int,letter_guess_wrong:list,letter_guess_correct:list,answer:str) ->int:
    """checks if the given letter is the answer and removes it if it exists"""
    guess=simpledialog.askstring("Input", "Enter the guess")
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
        label_1.config(text=f"wrong guess {10-i} are left",font=("Arial", 14))
    else:
        label_1.config(text=f"correct guess",font=("Arial", 14))
    label.config(text=position(answer,guess,letter_guess_correct),font=("Arial", 14))
    if len(letter_guess_wrong)>=1:
        guesss_wrong = tk.Toplevel(hangman_game)
        wrong=tk.Label(guesss_wrong,text=f"wrong guesses till now {letter_guess_wrong}",font=("Arial","13"))
        wrong.pack(padx=30,pady=30)
        guesss_wrong.after(2000, guesss_wrong.destroy) 
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
    for i in range(len(answer)):
        if answer[i]==" ":
            letter_guess_correct.append(" ")
        else:
            letter_guess_correct.append("_")
    i=0
    global hangman_game,label_1,label
    hangman_game = tk.Toplevel(root)
    hangman_game.title("Lets play")
    label = tk.Label(hangman_game, text=letter_guess_correct, font=("Arial", 14))
    label.pack(padx=50,pady=50)
    label_1 = tk.Label(hangman_game, text="Will show correct or wrong here", font=("Arial", 14))
    label_1.pack(padx=50,pady=50)
    while letter_list!=[] and i<10:
        i=checker(letter_list,i,letter_guess_wrong,letter_guess_correct,answer)
    if i==10:
        label = tk.Label(hangman_game, text=f"you fail the answer is {answer}", font=("Arial", 14))
        label.pack(padx=50,pady=50)
    else:
        label = tk.Label(hangman_game, text="you got it right", font=("Arial", 14))
        label.pack(padx=50,pady=50)
    hangman_game.after(2000, hangman_game.destroy) 
    return answer

def main():
    f=open("senteces used.txt","a")
    answer=hangman()
    f.writelines(answer+"\n")           
    f.close()

def gui():
    global root
    root=tk.Tk()
    root.geometry("300x300")
    label=tk.Label(root,text="Hangman ",font=("Arial",12))
    label.pack()
    buttton=tk.Button(root,text="Play Hangman",font=("Arial",13),command=lambda:main())
    buttton.pack()
    root.mainloop()
    
gui()
