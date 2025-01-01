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
    """checks if the given letter is the answer and replace it if it exists"""
    guess=simpledialog.askstring("Input", "Enter the guess")
    while not(len(guess)==1 and guess.isalpha()) and all(isinstance(guess, int) for x in letter_guess_wrong) :
        label_1.config(text="guess format is wrong",font=("Arial", 14))
        guess=simpledialog.askstring("Input", "Enter the guess")
    guess=guess.lower()
    increment=0
    a=0
    while a<len(letter_list):
        if guess==letter_list[a]:
            letter_list[a]=0
            increment+=1
        a+=1
    if increment==0:
        i+=1
        letter_guess_wrong.append(guess)
        label_1.config(text=f"wrong guess {6-i} are left",font=("Arial", 14))
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

def hangman() ->str:
    """creates a new window and initiates the whole hangman game"""
    global grade
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
    while not(all(isinstance(x, int) for x in letter_list)) and i<6:
        i=checker(letter_list,i,letter_guess_wrong,letter_guess_correct,answer)
    if i==6:
        label = tk.Label(hangman_game, text=f"you fail the answer is {answer}", font=("Arial", 14))
        label.pack(padx=50,pady=50)
        grade=len(letter_guess_wrong)+6
    else:
        label = tk.Label(hangman_game, text="you got it right", font=("Arial", 14))
        label.pack(padx=50,pady=50)
        grade=len(letter_guess_wrong)+0
    hangman_game.after(1000, hangman_game.destroy) 
    return f"correct word '{answer}' wrong guess '{letter_guess_wrong}'"

def main():
    """write the output into a file"""
    global grade
    teammembers = simpledialog.askstring("Input", "How many teams are there")
    value=int(teammembers)
    score_card=[]
    while value>0:
        answer=hangman()
        score_card.append(grade)
        grade=0
        value-=1
    label_0.config(text=score_card,font=("Arial", 14))
    f.writelines(answer+"\n")    

def gui():
    """creates the basic screen for the game"""
    global root,f,label_0
    f=open("senteces used.txt","w")
    root=tk.Tk()
    root.geometry("300x300")
    label=tk.Label(root,text="Hangman ",font=("Arial",20))
    label.pack()
    buttton=tk.Button(root,text="Single",font=("Arial",13),command=lambda:main())
    buttton.pack()
    buttton=tk.Button(root,text="Team",font=("Arial",13),command=lambda:main())
    buttton.pack()
    label_0=tk.Label(root,text="score card",font=("Arial",14))
    label_0.pack()
    root.mainloop()
    f.close()
    
gui()

# same letter or mistake

# teams(multiple teams) 
#   with score based on hardness
# computer mode(1000 words guess)
#   Give definition or clues after 5 mistakes
#   increase in hardness of words for less than 5 mistake
#   multiple levels of hardness with score
# human 

