import random
import sys

# Define the rarity percentages and corresponding skins
RARITY_PERCENTAGES = {
    'Common': 50.0,
    'Uncommon': 25.0,
    'Rare': 12.5,
    'Epic': 6.25,
    'Legendary': 3.125,
    'Mythic': 1.5625,
    'Contraband': 0.78125,
    'Unobtainable': 0.390625
}

# Skins grouped by rarity
SKINS_BY_RARITY = {
    'Common': ['Default Jonesy', 'Bullseye', 'Renegade Raider'],
    'Uncommon': ['Recon Scout', 'Scarlet Defender', 'Tracker'],
    'Rare': ['Skull Trooper', 'Ghoul Trooper', 'Red Knight'],
    'Epic': ['Dark Bomber', 'Raven', 'The Visitor'],
    'Legendary': ['Black Knight', 'Omega', 'Lynx'],
    'Mythic': ['Meowscles', 'Midas', 'Jules'],
    'Contraband': ['Shadow Ops', 'Galaxy', 'Wonder'],
    'Unobtainable': ['Aerial Assault Trooper', 'Renegade']
}

# Function to simulate opening a lootbox
def open_lootbox():
    # Determine rarity based on percentages
    rand_num = random.uniform(0, 100)
    cumulative_percentage = 0.0
    
    for rarity, percentage in RARITY_PERCENTAGES.items():
        cumulative_percentage += percentage
        if rand_num <= cumulative_percentage:
            selected_rarity = rarity
            break
    
    # Select a random skin from the chosen rarity
    selected_skin = random.choice(SKINS_BY_RARITY[selected_rarity])
    
    return selected_rarity, selected_skin

# Main loop to handle user input
inventory = []

while True:
    user_input = input("\nPress Enter to open a lootbox, or 'q' to view inventory: ").strip().lower()
    
    if user_input == '':
        rarity, skin = open_lootbox()
        inventory.append((rarity, skin))
        print(f"\nYou received a {rarity} skin: {skin}")
    
    elif user_input == 'q':
        if not inventory:
            print("\nYour inventory is empty.")
        else:
            print("\nCurrent Inventory:")
            for item in inventory:
                print(f"{item[0]}: {item[1]}")
        # Ask for confirmation to quit
        confirm_quit = input("\nPress 'q' again to quit or press Enter to continue: ").strip().lower()
        if confirm_quit == 'q':
            print("Exiting...")
            sys.exit(0)
    
    else:
        print("Invalid input. Press Enter to open a lootbox or 'q' to view inventory.")

