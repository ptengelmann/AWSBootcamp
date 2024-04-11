"""
Your module description
"""

games_user_plays = {1 : "League of Legends", 
2 : "Zelda", 
3 : "Call of Duty"
}
print(games_user_plays)

print("What game would you like to play?")
for key, game_tile in games_user_plays.items() :
    print(f"{key} : {game_tile}")
    
userRep = input("Enter the number of your choice: ")

if userRep in ["1", "2", "3"]:
    selected_game = games_user_plays[int(userRep)] 
    print(f"Amazing! Have a good time playing {selected_game}!")
    
else:
    print("Invalid choice. Please try again.")
