from ast import While
import random

game_options = ["R", "P", "S"]
computer_score = 0
player_score = 0
draw = 0
            
def play_game():
    global draw
    global player_score
    global computer_score
    player_choice = input("input your choice, rock(R), paper(P), scissors(S) or end(E): ")
    computer_choice = random.choice(game_options)
    
    
    
    if player_choice.upper() == computer_choice:
        print("You Both Chose The Same Thing! Try Again.")
        draw += 1
        play_game()
        
    else:
        if player_choice.upper() == 'R':
            if computer_choice == 'S':
                player_score += 1
                print('Computer Chose: '+ computer_choice +' ' + 'You Win! Rock Smashes Scissors.')
                play_game()
                
            else:
                computer_score += 1
                print('Computer Chose: '+ computer_choice +' ' + 'You Lose! Paper covers Rock.')
                play_game()
            
        elif player_choice.upper() == 'P':
            if computer_choice == 'R':
                player_score += 1
                print('Computer Chose: '+ computer_choice +' ' + 'You Win! Paper Covers Rock.')
                play_game()  
            else:
                computer_score += 1
                print('Computer Chose: '+ computer_choice +' ' + 'You Lose! Scissors Cuts Paper')
                play_game()
                
        elif player_choice.upper() == 'S':
            if computer_choice == 'P':
                player_score += 1
                print('Computer Chose: '+ computer_choice +' ' + 'You Win! Scissors Cuts Paper.')
                play_game()
            else:
                computer_score += 1
                print('Computer Chose: '+ computer_choice +' ' + 'You Lose! Rock Smashes Scissors.')
                play_game()
    
        elif player_choice.upper() == 'E':  
            def endgame():
                print('Game Ended.')         
                print('Computer Won ' + str(computer_score) + ' Times')
                print('You Won ' + str(player_score) + ' Times')
                print('Drew ' + str(draw) + ' Times') 
            endgame() 
        
        
        else:
            print('Invalid Input!') 
            play_game()
            
        # play_game()
        
play_game()
    
