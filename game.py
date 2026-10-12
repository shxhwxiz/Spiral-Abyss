import random
import time
import pyfiglet
from playsound3 import playsound
import sys


player_info = {
    "hp": 20,
    "max_hp": 20,
    "gold": 0,
    "floor": 1,
    "player_inventory": []
}




def monster_encounter():
        monsters = ["Skeleton!", "Spider!", "Hillichurl!", "Zombie!"]
        enemy = random.choice(monsters)   
        enemy_damage = random.randint(1, 10)

        print(f"Oh no! A wild {enemy} appears!")
        playsound("sounds/undertale-battle-start.mp3")
        decision = input("Will you (f)ight or (r)un? (Type exit to leave)")
        if decision == "f":
            player_info["hp"] -= enemy_damage
            if check_death():
                return
            print(f"You attacked the {enemy} and lost {enemy_damage} health!")
            time.sleep(4)
            gold_earned = random.randint(1,20)
            player_info["gold"] += gold_earned
            print(f"You pocketed {gold_earned} gold from that fight! Wow, so rich! Currently, you have ", player_info["gold"], " gold. Keep on going!")
            time.sleep(4)
            print(f"The enemy put up a good fight, dealing {enemy_damage} damage leaving you with only ", player_info["hp"], " health!")
            time.sleep(4)
        if decision == "r":
            run_factor = random.randint(1,2)
            if run_factor == 1:
                l_gold = random.randint(2, 7)
                player_info["gold"] -= l_gold
                print(f"You succesfully ran away, but you lost {l_gold} while running!")
                time.sleep(2)
                print(f"That encounter left you with ", player_info["gold"], ", keep on going!")
                time.sleep(1.5)
        if decision == "exit":
            print("Alright! Hope to see you next time!")
            sys.exit()
        if run_factor == 2:
            player_info["hp"] -= enemy_damage
            if check_death():
                return
            print(f'''You slipped and fell while running, losing your balance! 
            The monster caught you, dealing {enemy_damage} damage to you!''')
            time.sleep(3)
            print(f"You have {player_info['hp']} health left, keep trying!")
            time.sleep(3)






def check_death():
    if player_info["hp"] <= (0):
        playsound("sounds/undertale-death.mp3")
        print("Oof, you died! Try again? (Starting again in 5 seconds)")
        time.sleep(5)
        player_info["hp"] = player_info["max_hp"]
        player_info["gold"] = 0
        player_info["floor"] = 1
        return True
    return False




def shop_time():
    print('''An old, unknown person approaches you. He speaks with a slightly weak tone:
    "Welcome, welcome young traveler. Would you like to come to the gold shop? I have all kinds of treasures...''')
    time.sleep(3)
    shop_decision = input("Enter the shop? (y/n)")
    if shop_decision == "n":
        print("Alrighty! Time to continue with the game!")
    if shop_decision == "y":
        shop_items = {
            "Revival Potion": 20,
            "Shield": 20
        }
        print('''Wise decision, youngster. This is the shop. We have all kinds of things
        to help you on your abyssal journey. Peruse the shop as you please.''')
        time.sleep(2)
        while True:
            print(f"Current Gold: {player_info['gold']}")
            print("Items for sale:")
            for item, price in shop_items.items():
                print(f"{item}: {price} gold.")
            item_buy = input("What would you like to buy, traveler? (Type leave to exit the shop)")
            if item_buy == "leave":
                print("Thanks for coming to the shop. Safe travels-- I'Il see you around.")
                break
            if item_buy in shop_items:
                cost = shop_items[item_buy]
                if player_info["gold"] >= cost:
                    player_info["gold"] -= cost
                    player_info["player_inventory"].append(item_buy)
                    print(f"Ah, what a fine choice! You got a {item_buy}!")
                else: 
                    print("Over here, nothing is free. You do not have any gold. Better try your luck in some other place." "")
            else:
                print("Hm, I have never heard of such a thing. I do not carry that here. Take another look.")















i_banner = pyfiglet.figlet_format("SPIRAL ABYSS!", font="larry3d")
print(i_banner)

yn = input("Welcome, welcome. Would you like to dive into the Spiral Abyss? (y/n)")

if yn == "y":
    print("Alright! Heading into the abyss...!")
    time.sleep(1.5)


    while True:
        monster_encounter()
        if random.randint(1, 3) == 1:
            shop_time()
        player_info["floor"] += 1
        time.sleep(4)
        print(f"Moving down deeper... Welcome to.. Floor {player_info['floor']}!!")
        time.sleep(2)

elif yn == "n":
    print("Alright! Buh bye for now!")
    sys.exit()
    time.sleep(1)