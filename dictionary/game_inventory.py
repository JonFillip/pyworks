
game_inventory = {
    'machine gun': 1,
    '30 caliber bullet': 190,
    'hand grenade': 50,
    'sniper gun': 1,
    'long range sniper': 1,
    'rpg': 1,
    'hand gun': 5,
    'sticker bomb': 12,
    'fuel can': 1,
    'lighter': 1
}

def display_inventory(inventory):
    """Displays and sums the amount of player inventory."""
    print("Available Inventory:")
    total_items = 0
    for name, quantity in inventory.items():
        print(f"- {name}: {quantity}")
        total_items += quantity
    return f"The total amount of inventory owned by the player is: {total_items}."

def add_to_inventory(inventory, added_items):
    """Adds more game items to the inventory dictionary and prints the 
    newly added items and the sum of the inventory"""
    game_inventory = {}
    for item in added_items:
        if item in game_inventory:
            game_inventory[item] += 1
        else:
            game_inventory[item] = 1
    print(display_inventory(game_inventory))

new_items = ['knife', 'cross-bow', 'knife', 'scope', 'long range sniper', 'hand gun', 'remote bomb', 'drone']
print(add_to_inventory(game_inventory, new_items))
