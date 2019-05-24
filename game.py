# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 22:49:28 2019

@author: tarun b.tech(cse)
         gla university , mathura   
"""

import random
import time

def instruction_of_game():
    '''
        Function To Display Rules Of Game
    '''
    print('You Have To Guess Movie Name Within 5 Chances Word By Word')
    print('After 5 Chances You Have To Enter Name Of Movie')
    initial_time=time.time()
    while time.time()<=initial_time+5:pass

def check_index(ch,selected_movie):
    '''
        Function To Search For Index Of Particular Character in Movie Name
    '''
    
    return [i for i in range(len(selected_movie)) if ch==selected_movie[i] ]
        

def game_algo():
    '''
        Function For Full Game Algorithm
    '''
    score=0
    all_score=0
    movies=['ant man','avengers','kaabil','robot','terminator','transformers','raabta','guardians of the galaxy','captain america','captain marvel','infinity war','iron man','hulk','spiderman','thor','bat man','super man']
    user=True
    while user:
        selected_movie=random.choice(movies)
        movies.remove(selected_movie)
        ln=len(selected_movie)
        print('\nGuess')
        
        l=[' ' for i in range(ln)]
        choice=5
        while choice:
            print(l)
            ch=input('Enter :')
            index=check_index(ch,selected_movie)
            for i in range(len(index)):
                l[index[i]]=ch
            choice-=1
            print()
            print('Chances Left :',choice)
        print(l)    
        if selected_movie!=''.join(l):    
            movie_name=input('Enter Movie Name ')
            if movie_name==selected_movie:
                print('Congratulations!!! You Won The Round')
                score+=1
                all_score+=1
            else : 
                print('You Loose Appear In Next Round To Win : Movie Name Was',selected_movie)
                all_score+=1
        else:
            print('Congratulations!!! You Won The Round')
            score+=1
            all_score+=1
        user_input=input('\nPress y to continue else n to exit ')    
        user = True if user_input=='y' else False
    print('Your Score Is',score,'Out Of',all_score)
    return score

#----------------------------Main------------------------------------------

    instruction_of_game()
    a=game_algo()
    return (a*5)
