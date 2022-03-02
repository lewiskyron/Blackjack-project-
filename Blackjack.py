#Blackjack capstone project
import random

art_logo = """
__________.__                 __           __               __    
\______   \  | _____    ____ |  | __      |__|____    ____ |  | __
 |    |  _/  | \__  \ _/ ___\|  |/ /      |  \__  \ _/ ___\|  |/ /
 |    |   \  |__/ __ \\  \___|    <       |  |/ __ \\  \___|    <      
 |______  /____(____  /\___  >__|_ \  /\__|  (____  /\___  >__|_ \
        \/          \/     \/     \/  \______|    \/     \/     \/

"""
print(art_logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def draw():
    random_card = random.choice(cards)
    return random_card


functions ={"hit" : draw}
player_cards = []
dealers_cards = []
def game_draws(data, data_list):
    dealer_score = 0
    player_score = 0  
    for i in range(2):
        player_cards.append(draw())
        dealers_cards.append(draw())


#if elif statements are evaluated from top to bottom.
    print(f" the player cards are  {player_cards}")  
    player_score  += (player_cards[0] + player_cards[1])
    print(f"The current player score is  {player_score}")
    print(f" the dealers cards are  {dealers_cards[0]}")
    dealer_score += dealers_cards[0] + dealers_cards[1]
    



 
    if player_score == 21:
       print("Player wins!")
    while player_score < 21: 
        answer1 = input("Do you want to stand or hit "). lower()
        if answer1 == "hit":
                added_card = functions["hit"]
                new_card = added_card()
                player_cards.append(new_card)
                print(player_cards)
                player_score += new_card
                print(f" the player's score is {player_score}")
                print(f"The players cards are {player_cards}")
        else:
             print(player_score)
             print(f" the player's score is {player_score}")
             break

    while dealer_score < 17:
        nzulu = draw()
        dealers_cards.append(nzulu)
        dealer_score += nzulu
   
   
    print(f"The dealer's score is {dealer_score}")
    print(f"The dealers cards are{dealers_cards}")
            
    if player_score > 21:
         print("Dealer wins")
    elif player_score < dealer_score:
         print("The dealer wins!")
    elif player_score > dealer_score:
         print("Player wins")  
    elif dealer_score == player_score:
        print("Game is a draw")    
game_draws(2, player_cards)



# use function for parts of the game that are general for both players.
# this declutters the code structure.
# if we wanted to restart the game we would put the whole game into a function then clear the previous game.




