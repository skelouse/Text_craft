import random
import time
import os
import math

test = False

night = False
furnace_have = False
health = 100
height = 64
damage = 1
clock = 0
money = 0



def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()
# for 1 material [item to craft, material, quantity of material, quantity received]
# for 2 material [item to creaft, material, quantity of material, material2, quantity of material2, quantity received]
crafting = [
    ['furnace', 'cobblestone', 8, 1],
    ['bed', 'wool', 3, 'wood_plank', 3, 1],
    ['wood_plank', 'log', 1, 4],
    ['stick', 'wood_plank', 2, 4],
    ['fishing_rod', 'stick', 3, 'string', 2, 1],
    ['bucket', 'iron', 3, 1],
    ['torch', 'coal', 1,'stick', 1, 4],
    ['crafting_table', 'wood_plank', 4, 1],
    ['gold_pickaxe', 'stick', 2, 'gold', 3, 1],
    ['wooden_pickaxe', 'stick', 2, 'wood_plank', 3, 1],
    ['stone_pickaxe', 'stick', 2, 'cobblestone', 3, 1],
    ['iron_pickaxe', 'stick', 2, 'iron', 3, 1],
    ['diamond_pickaxe', 'stick', 2, 'diamond', 3, 1],
    
]


cook_output = [
    ['iron_ore', 'iron'], ['raw_porkchop', 'cooked_porkchop'], ['raw_beef', 'cooked_beef'],
    ['gold_ore', 'gold'], ['cobblestone', 'stone'], ['log', 'coal'], ['raw_fish', 'cooked_fish'],
    ['raw_lambchop', 'cooked_lambchop'], ['raw_chicken', 'cooked_chicken']
]

inventory = [
    ['torch', 1]
]

# type, current durability
equipment = []

current_pickaxe = ['fist', -1, 0, -1, 1]

#type, current durability, power, total durability
tools = [
    ['gold_pickaxe', 32, 2, 32, 4], ['wooden_pickaxe', 59, 1, 59, 1], ['stone_pickaxe', 131, 2, 131, 2]
        , ['iron_pickaxe', 250, 3, 250, 3], ['diamond_pickaxe', 1561, 4, 1561, 4]
]

picks = ['gold_pickaxe', 'wooden_pickaxe', 'stone_pickaxe', 'iron_pickaxe', 'diamond_pickaxe']

fuel = [
    ['coal', 8], ['log', 4], ['wood_plank', 2], ['stick', 1]
]

edible = [
    ['raw_porkchop', 5], ['raw_beef', 5], ['cooked_porkchop', 20], ['cooked_beef', 20],
    ['apple', 8], ['rotten_flesh', -5], ['raw_fish', 5], ['cooked_fish', 15], ['cooked_chicken', 20],
    ['cooked_lambchop', 20], ['raw_chicken', 5], ['raw_lambchop', 5]
]
semi_edible = [
    'raw_porkchop', 'raw_beef', 'raw_fish', 'raw_chicken',
    'raw_lambchop', 'rotten_flesh'
]

animal = ['wolf', 'chicken', 'chicken', 'chicken', 'pig', 'pig', 'pig', 'cow',
    'cow', 'cow', 'sheep', 'sheep', 'sheep']

animal_night = [
    'wolf', 'chicken', 'pig', 'cow','sheep',
    'zombie', 'zombie', 'skeleton', 'skeleton',
    'witch', 'slime', 'creeper', 'spider'
]

friend = ['chicken', 'pig', 'cow', 'sheep']
foe = ['zombie', 'skeleton', 'witch', 'spider', 'slime', 'creeper']


#['', ##, (0 for none, 1 for wood pick, 2 for stone pick, 3 for iron pick, 4 for unbreakable)]
ores = [
    ['bedrock', 5, 5], ['diamond', 14, 3], ['redstone', 14, 3],
    ['gold_ore', 30, 3], ['lapis', 30, 3], ['lava', 30], ['iron_ore', 61, 2], ['coal', 61, 1], ['gravel', 61, 0],
    ['cobblestone', 61, 1], ['dirt', 0, 0], ['obsidian', 0, 4]
]

cave_ores = [
    ['diamond', 14, 3], ['redstone', 14, 3],
    ['gold_ore', 30, 3], ['lapis', 30, 3], ['iron_ore', 61, 2], ['coal', 61, 1]
]

# To set an achievement up to something achievements_list[list number][0] += 1 
# [variable ,Don't have have 0 or 1 ,goal , "achievement",reason for achievement]
achievements_list = [
# 0
[0, 0, 'Dirt Miner',100 , 'mining 100 dirt'],
# 1
[0, 0, 'Dirty Diamonds',2 , 'mining 2 diamonds'],
# 2
[0, 0, 'Tree Hugger(not)',50 , 'killing 50 trees'],
# 3
[0, 0, 'Cover Me Feet',1 , 'pouring water on lava (not dying)'],
# 4
[0, 0, 'Sorry, Mom',1 , 'killing a cow'],
# 5
[0, 0, 'Jill' ,20 , 'filling your bucket 20 times'],
# 6
[0, 0, 'Good morning, ladies',10 , 'catching 10 fish'],
# 7
[0, 0, 'Bitch Tamer',5 , 'taming 5 wolves'],
# 8
[0, 0, 'Dar3 D3vil',10 , 'killing 10 creepers'],
# 9
[0, 0, 'Worrisome',100 , 'opening inventory 100 times'],
# 10
[0, 0, 'Oink, Oink',100 , 'eat 100 items']
]
achieved = []

# START FARMING LISTS
# START FARMING LISTS

farm_types = [
    ['wheat', 1, 500],
    ['skeleton', 1 ,10000000]
]
all_farms = [# my farms   ADDD MOREEEEEEEEEEEEE
['wheat', 0, 500, 'dirt'],
['skeleton', 0 ,10000000, 'dirt']
]

farm_materials = [
    ['log', 5],
    ['stone', 2],
    ['iron_block', .5],
    ['diamond_block', .02],
    ['obsidian', .001],
    ['bedrock', .0001]
]

# END FARMING LISTS
# END FARMING LISTS

def money_add(x):
    global money
    money = money + x


def farming():

    global money

    q = 0
    z = 0
    select = 0
    selected_farm = 0
    have_farm = False
    farm_selected = False
    choice_material = 0
    current_farms = []   

    for i in all_farms:
        if i[1] > 0:
            current_farms.append(i)
            have_farm = True

            # Base cost of a farm
        # $, material, wood_plank, dirt, money
    base_farm_cost = [100, 100, 40, 100]# level up is less

    EventFarm(0, all_farms)
    # need to water? 0 or 1/ , need to rebuild 0 or 1, 
    #               return [water, rebuild]

    while select != 'q':

        x = 1
        try:

            if have_farm == True:   
                if farm_selected:
                    EventFarm(1, selected_farm)  # 1 is check for things that need to be done 
                else:
                    pass  
                print("""What would you like to do?
    (s)elect a farm
    (w)ater
    (h)arvest
    (l)evel up
    (b)uild farm
    (d)estroy
    (q)uit
    """)# add are you sure on destroy

                select = input("> ")

                if select == 's': # Select a farm
                    for i in current_farms:
                        print(f"#{x} {i[0]}")
                    try:
                        select = int(input("> "))
                        if select:
                            selected_farm = current_farms[(select-1)]
                            farm_selected == True

                    except (ValueError, IndexError):
                        print("Invalid selection")
                        print("")

                elif select == 'w' and selected_farm != 0: # Water selected
                    EventFarm(2, selected_farm)

                elif select == 'h' and selected_farm != 0: # Harvest selected
                    EventFarm(3, selected_farm)

                elif select == 'l' and selected_farm != 0: # level selected
                    EventFarm(5, selected_farm)

                elif select == 'd' and selected_farm != 0: # Destroy
                    print("Are you sure you want to destroy this farm? (y/n)")
                    select = input("> ")
                    if select == 'y':
                        EventFarm(6, selected_farm)
                
                elif select == 'b':# build farm
                    build_farm()
                    select = 'q'

                elif select == 'q': # Quit
                    pass

                elif selected_farm == 0:
                    print("No farm selected")
                    print("")

                else:
                    print("Not an option")
                

            elif current_farms:# current_farms returns true or false
                print("Which farm would you like to go to")
                input("> ")
            
            else:
                print("You don't have any farms")
                print("Build one? (y/n)")
                select = input("> ")

                if select == 'y':
                    build_farm()
                    select = 'q'
                else:
                    select = 'q'
            


        except ZeroDivisionError:
            print("Lol")


def EventFarm(x,y):
    # x is what to do
    # y is which farm ('all_farms')
    #x
    # 1 is check for things that need to be done on y farm
    # 2 is water
    # 3 is harvest
    # 4 is build
    # 5 is level up
    # 6 is destroy

    have_farm = False
    for i in all_farms:
        if i[1] > 0:
            have_farm = True

    if x == 1 and len(y) == 2:
        print("Checking what needs to be done")
        input("> ")

    elif x == 2:
        print("watering",y)
    elif x == 3:
        print("harvesting",y)
    elif x == 4:
        all_farms.append(y)
    elif x == 5:
        print("leveling up",y)
    elif x == 6:
        print("Destroying")


    else:# 0

        if have_farm:
            print("This happened while you were gone")
            input("> ")
        else:
            pass



# $, material, wood_plank, dirt, money
# base_farm_cost = [100, 100, 40, 100]
def build_farm():

    select = 0
    farm_selected = False
    have_enough_materials = False
    have_enough_wood_plank = False
    have_enough_dirt = False
    have_enough_materials_to_build = False

    for i in inventory:
        if i[0] == 'wood_plank' and i[1] >= 100:
            have_enough_wood_plank = True
        if i[0] == 'dirt' and i[1] >= 40:
            have_enough_dirt = True

    if have_enough_dirt and have_enough_wood_plank:
        have_enough_materials_to_build = True

    while select != 'q':
        z = 0
        x = 1
        k = 0
        print("What would you like to build it out of?")
        number_list(farm_materials, 0)

        print("(q)uit")
        select = input("> ")
        if select != 'q':
            try:
                select = int(select)
                if select:
                    choice_material = farm_materials[(select-1)]# material chosen

                    for i in inventory:
                        if i[0] == choice_material[0] and i[1] >= 100:
                            have_enough_materials = True

                    if have_enough_materials:
                        print("What kind of farm do you want?")
                        x = 1
                        for i in farm_types:
                            print(f"#{x} {i[0]} ${i[2]}, 100 wood_plank, and 40 dirt")
                            x += 1
                        select = input()
                        select = int(select)
                        select = farm_types[(select-1)]
                        if have_enough_materials_to_build and money > select[2]:
                            select.append(choice_material[0])
                            print(f"Building {select[0]} farm!")

                            while z != 4:
                                if z == 0:
                                    print("adding fence posts")
                                    while k != 6:
                                        print(".")
                                        time.sleep(.5)
                                        k += 1
                                    input("(Enter)")
                                    k = 0
                                elif z == 1:
                                    print(f"building the {choice_material[0]} supports")
                                    while k != 6:
                                        print(".")
                                        time.sleep(.5)
                                        k += 1
                                    input("(Enter)")
                                    k = 0
                                elif z == 2:
                                    print("dumping the dirt")
                                    while k != 6:
                                        print(".")
                                        time.sleep(.5)
                                        k += 1
                                    input("decorate?")
                                    k = 0
                                elif z == 3:
                                    print("decorating")
                                    while k != 6:
                                        print(".")
                                        time.sleep(.5)
                                        k += 1
                                    

                                z += 1
                            input(f"{select[0]} farm is complete!")
                            EventFarm(4, select)
                            select = 'q'
                            farming()                                               

                        elif have_enough_materials_to_build:
                            input("You don't have enough cash.")
                            select = 'q'

                        else:
                            input("You don't have enough materials.")
                            select = 'q'
                    else:
                        print(f"You don't have 100 {choice_material[0]}")

            except (ValueError, IndexError):
                print("Not Valid")
                print("")
        else:
            pass


# x is whether to show all achievements or check for gained and notify(0 or 1)
def achievements(x):
    has = False
    if x == 0:
        for i in achievements_list:
            if i[1] == 1:
                print(i[2],'*')
                print("")
                has = True

        if has == False:
            print("You don't have any, lol.")   

    else:
        for i in achievements_list:
            if i[1] == 0 and i[0] >= i[3]:
                achieved.append(i[2])
                i[1] = 1
                print("=========================")
                print("=========================")
                print(f"You got {i[2]} achievement for {i[4]}!")
                print("=========================")
                print("=========================")


def menu():

    print("""    (f)arm
    (e)quipment
    (i)nventory
    (a)chievements
    (q)uit""")
    select = input("> ")

    if select == 'a':
        achievements(0)
        input("> ")
    elif select == 'f': # farm
        farming()
    elif select == 'i': # inventory
        view_inventory()
    
    elif select == 'e': # equipment
        view_equipment()

    elif select == 'q':
        choice = input("Are you sure you want to quit and lose your progress? (y/n)")
        if choice == 'y':
            print("BYEEEE")
            time.sleep(3)
            exit(0)
    else:
        start()


def craft():
    global crafting
    global inventory
    available = []
    item1 = False
    table = False
    done = False
    done2 = False
    msg = 0
    x = 1
    k = 1
    z = 0
    y = 0
    p = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    possible = 0
    quantity = 1
    quantity2 = 0
    quantity3 = 0

    for i in inventory:
        if i[0] == 'crafting_table' and i[1] >= 1:
            table = True


    for i in crafting:

        if len(i) == 4:
            for x in inventory:
                if i[1] == x[0] and i[2] <= x[1]:
                    available.append(i)
        
        if len(i) == 6:
            if table == True:
                for x in inventory:
                    if i[1] == x[0] and i[2] <= x[1]:
                        item1 = True

                for x in inventory:
                    if item1 == True and i[3] == x[0] and i[4] <= x[1]:
                        available.append(i)
            else:
                pass

    print("Items you can craft")
    while k == 1:
        try:
            number_list(available, 0)

            print("")
            print("What would you like to craft? (0 to cancel)")
            select = int(input("> "))
            select = available[(select -1)][0]
            k = 2
        except(TypeError, ValueError):
            print("Invalid selection")

    if k == 2:
        
        for i in available:
            if select == i[0]:
                

                
                # finding the possible quantities
                for e in crafting:
                    # e is  ['bed', 'wool', 3, 'wood_plank', 3, 1],
                    # for 2 material recipies
                    if len(e) == 6 and select == e[0]:
                        for x in inventory:
                            if e[1] == x[0]:
                                # (Quantity I have on hand / Quantity needed for recipie) rounded down *
                                # total amount given at end [Total amount of item craftable]
                                var1 = math.floor(x[1] / e[2])

                        for x in inventory:
                            if e[3] == x[0]:
                                var2 = math.floor(x[1] / e[4])

                        if var1 > var2:
                            possible = var2
                        else:

                            possible = var1

                    # ['wood_plank', 'log', 1, 4], 
                    # for 1 material recipies
                    elif select == e[0]:
                        for x in inventory:
                            if e[1] == x[0]:
                                # Total amount of item craftable
                                var1 = math.floor(x[1] / e[2])
                                possible = var1


                while done == False:
                    
                    print(f"Make {select} how many times? 0-{possible}(enter 0 to cancel)")

                    try:
                        select2 = int(input("> "))
                        quantity2 = select2

                        if quantity2 < 0:
                            print("Must be greater than zero")

                        elif quantity2 == 0:
                            done = True
                            done2 = True

                        elif quantity2 <= possible:
                            done = True

                        else:
                            print("You don't have that many!")

                    except (TypeError, ValueError) as e:
                        print("Numbers only please")


                # Where the crafting actually happens
                
                if done2 == False:
                    for e in crafting:
                        if e[0] == select:

                            if len(e) == 6:
                                store(e[0], (e[5] * quantity2))
                                store(e[1], (-e[2] * quantity2))
                                store(e[3], (-e[4] * quantity2))
                                msg = (f"You gained {quantity2 * e[5]} {select}")
                                select2 = select2 * e[3]

                            else:
                                store(e[0], (e[3] * quantity2))
                                store(e[1], (-e[2] * quantity2))
                                msg = (f"You gained {quantity2 * e[3]} {select}")
                                select2 = select2 * e[3]

                    print(f"Crafting {select}")
                    tick(1)
                    while z != 3:
                        print(".")
                        time.sleep(.5)
                        z += 1
                    print(msg)
                    input("> ")
    
def a2():
    print("@@@@@      Skelouse      @@@@@")
def eat():
    global health
    health_added = 0
    food_selected = 0
    quantity = 0
    query = 0
    y = 0
    food_list = []
    have_food = True


    while have_food:
        have_food = False
        for i in inventory:
            for x in edible:
                if i[0] == x[0] and i[1] > 0:
                    have_food = True
        if have_food == False:
            input("You don't have anything to eat")
        else:
            health_added = 0
            food_selected = 0
            y = 0
            food_list = []
            for i in inventory:
                for x in edible:
                    if x[0] == i[0] and i[1] >= 1:
                        food_list.append(x[0])
            while query != 'q':
                try:
                    x = 1
                    print("What are you hungry for?")
                    number_list(food_list, -1)

                    print("")
                    select = int(input("> "))
                    select = food_list[(select - 1)]
                    query = 'q'
                    
                except (ValueError, TypeError):
                    have_food = False
                    query = 'q'
            while have_food:
                select2 = 0
                if select in semi_edible:
                    
                    if random.randint(0,100) < 70:
                        print("Ehh")
                        for x in edible:
                            if x[0] == select:
                                tick(1)
                                health_added = x[1]
                                food_selected = x[0]
                                store(food_selected, -1)
                                health += health_added
                                print(f"You eat {food_selected} for {health_added} hp.")
                                achievements_list[10][0] += 1
                                if health >= 100:
                                    print("Your health is full!")
                                    health = 100


                    else:
                        print("Yuck")
                        for x in edible:
                            if x[0] == select:
                                tick(1)
                                health_added = -(x[1])
                                food_selected = x[0]
                                store(food_selected, -1)
                                health += health_added
                                print(f"The {food_selected} poisons you, taking {health_added} hp!")
                                achievements_list[10][0] += 1
                                if health <= 0:
                                    dead()


                    have_food = False
                    quantity = 0
                    for i in inventory:
                        if i[0] == food_selected:
                            quantity = i[1]
                            if quantity >= 1:
                                have_food = True
                    if quantity and have_food:
                        print(f"{quantity} left, eat another? (y/n)")
                        select2 = input("> ")

                        if select2 == 'y':
                            pass
                        else:
                            have_food = False
                    else:
                        input("No more food!")
                        have_food = False



                elif select in food_list:
                    print("Yummy")
                    for x in edible:
                        if x[0] == select:
                            tick(1)
                            health_added = x[1]
                            food_selected = x[0]
                    
                    store(food_selected, -1)
                    health += health_added
                    print(f"You eat {food_selected} for {health_added} hp")
                    achievements_list[10][0] += 1
                    if health >= 100:
                        print("Your health is full!")
                        health = 100

                    have_food = False
                    quantity = 0
                    for i in inventory:
                        if i[0] == food_selected:
                            quantity = i[1]
                            if quantity >= 1:
                                have_food = True
                    if quantity and have_food:
                        print(f"{quantity} left, eat another? (y/n)")
                        select2 = input("> ")

                        if select2 == 'y':
                            pass
                        else:
                            have_food = False
                    else:
                        input("No more food!")
                        have_food = False



# ['stick', 'wood_plank', 2, 4]
    # ['fishing_rod', 'stick', 3, 'string', 2, 1]]
    # x is the item to add
    # y is the quanity
    # This is how all items are stored into the inventory
def store(x,y):

    added = False
    in_tools = False
    z = 0
    remove = 0


    for i in tools:
        if x == i[0]:
            if y > 0:
                while y > 0:
                    equipment.append(i)
                    in_tools = True
                    y -= 1

            else:
                for i in equipment:
                    if i[0] == x:

                        equipment.remove(i)
                        in_tools = True      


    if in_tools == False:
        for i in inventory:
            if i[0] == x:
                i[1] = i[1] + y
                added = True

        if added != True:
            inventory.append([x, y])


# Takes current height and returns the available ores
def ore(height):

    global ores
    mineable = []

    for i in ores:
        if i[1] >= height:
            mineable.append(i[0])

    if height < 61:
        return mineable[random.randint(0, (len(mineable)-1))]
    else:
        if achievements_list[0][1] == 0:
            achievements_list[0][0] += 1             
        return 'dirt'


def cave_ore(height):

    global cave_ores
    mineable = []

    for i in cave_ores:
        if i[1] >= height:
            mineable.append(i[0])

    if height < 61:
        return mineable[random.randint(0, (len(mineable)-1))]
    else:
        return 'dirt'



def dig_down(height):


    global health
    block = 0
    select = 0
    z = 0
    bucket = False
    tick(1)

    block = ore(height)
    
    # if block == 'dirt'
    print("You mine the block below you")
    while z != 3:
        print(".")
        time.sleep(.5 / current_pickaxe[4])
        z += 1
    


    
    if block != 'bedrock' and block != 'lava':
        
        if pickaxe(block) == True:
            if block == 'diamond':
                    achievements_list[1][0] += 1
            print(f"You get 1 {block}!")
            store(block, 1)
        else:
            print("Try using a better pickaxe")

        height -= 1
        print("Climb back up or keep digging(c/d)")
        select = input("> ")
        if select == 'c':
            print("You climb back to the surface")
            input("> ")
        elif select == 'd':
            dig_down(height)
        else:
            print("Returning to surface")
            input("> ")

    else:
        bucket = False
        if block == 'lava':
            for i in inventory:
                if i[0] == 'water_bucket' and i[1] > 0:
                    bucket = True
            
            if bucket == False:
                print("OUCH LAVA BURNS!")
                print("Bring a water bucket next time.")
                dead()
            else:
                achievements_list[3][0] += 1
                print("You use your water bucket to turn the lava into obsidian")
                print("You also lose 10 hp from well, lava")
                health -= 10
                if health <= 0:
                    dead()
                block = 'obsidian'
                store('water_bucket', -1)
                store('bucket', 1)

                if pickaxe(block) == True:
                    print(f"You get 1 {block}!")
                    store(block, 1)
                else:
                    print("Try using a better pickaxe")

                height -= 1
                print("Climb back up or keep digging(c/d)")
                select = input("> ")
                if select == 'c':
                    print("You climb back to the surface")
                    input("> ")
                elif select == 'd':
                    dig_down(height)
                else:
                    print("Returning to surface")
                    input("> ")

        else:    
            print("You can't mine through bedrock silly!")
            print("Returning to surface")
            input("> ")

# current_pickaxe = ['wooden_pickaxe', 33, 1, 59]
def pickaxe(block):
    global current_pickaxe
    can_mine = False
    for i in ores:
        if i[0] == block and i[2] <= current_pickaxe[2]:
            broken = True
            if current_pickaxe[1] > 0:
                current_pickaxe[1] -= 1

            if current_pickaxe[1] == 0:
                print("Your pickaxe has broken...")
                current_pickaxe = ['fist', -1, 0, -1, 1]

            return True
    if can_mine == False:
        return False


def a4():
    a1()
    a2()
    a3()   

# Defines what you find on an adventure
def adventure():

    tick(1)
    search = ['tree','tree', 'tree', 'tree',
 'tree', 'tree', 'river', 'animal', 'animal', 'cave']


    end = search[random.randint(0, (len(search)-1))]

    if end == 'animal':
        mob()

    elif end == 'tree':
        print("You find a tree")
        select = input("Do you want to cut it down(y/n)")
        if select == 'y':
            break_tree()
        elif select == 'n':
            adventure()
        else:
            pass

    elif end == 'river':
        river()

    elif end == 'cave':
        cave()
    
    else:
        print("ERROR in def adventure")


def river():

    rod = False
    bucket = False
    print("You see a river!")
    for i in inventory:
        if i[0] == 'fishing_rod':
            rod = True

    for i in inventory:
        if i[0] == 'bucket':
            bucket = True

    if bucket == True and rod == True:
        print("Would you like to fish or fill your bucket with water?(f/b)")
        select = input("> ")
        if select == 'f':
            fish()
        elif select == 'b':
            fill_bucket()
        else:
            pass

    elif bucket == True:
        print("would you like to fill a bucket with water?(y/n)")
        select = input("> ")
        if select == 'y':
            fill_bucket()

    elif rod == True:
        print("would you like to fish?(y/n) ")
        select = input("> ")
        if select == 'y':
            fish()

    else:
        print("Sorry there's nothing for you here.")
        print("Keep adventuring?(y/n)")
        select = input("> ")
        if select == 'y':
            adventure()
        else:
            start()


def fill_bucket():

    tick(1)
    bucket = True

    while bucket == True:
        z = 0
        print("Your bucket fills up")
        achievements_list[5][0] += 1
        
        while z != 3:
            print(".")
            time.sleep(.5)
            z += 1
        
        for i in inventory:
            if i[0] == 'bucket' and i[1] >= 1:
                store('bucket', -1)
                store('water_bucket', 1)

        bucket = False
        for i in inventory:
            if i[0] == 'bucket' and i[1] > 0:
                bucket = True

        if bucket == True:
            print("Fill another? (y/n)")
            select = input("> ")

            if select == 'y':
                pass
            else:
                bucket = False


  
def fish():

    print("You throw in your line")
    tick(1)
    select = 0
    z = 0
    while z != 10:
        print(".")
        time.sleep(1)
        z += 1

    if random.randint(0,100) < 30:
        print("You caught a fish!")
        achievements_list[6][0] += 1
        store('raw_fish', 1)
        print("Continue fishing? (y/n)")
        select = input("> ")

    else:
        print("No bite, keep fishing? (y/n)")
        select = input("> ")

    if select == 'n':
        print("The river waves goodbye")
        input(">")
    elif select == 'y':
        fish()
    else:
        pass


def cave():

    tick(1)
    global height
    z = 0
    search = ['ore', 'monster']
    search_mob = ['zombie', 'creeper', 'skeleton']

    print("You peer into the entrance of a cave.")
    print("Will you dare enter? (y/n)")
    select = input("> ")

    if select == 'y':
        height -= 10
        find = search[random.randint(0,1)]

        if find == 'ore':
            block = cave_ore(height)
            print(f"You mine one {block}")
            while z != 3:
                print(".")
                time.sleep(.5 / current_pickaxe[4])
                z += 1
            if pickaxe(block) == True:
                if block == 'diamond':
                    achievements_list[1][0] += 1
                print(f"You get 1 {block}!")
                store(block, 1)
            else:
                print("Try using a better pickaxe")   
            deep_cave()
        else:
            fight_mob(search_mob[random.randint(0,2)])
            deep_cave()

    elif select == 'n':
        adventure()

    else:
        start()


def a3():
    print("@@@@@      2018          @@@@@")


def deep_cave():

    global height
    tick(1)
    z = 0
    have_torch = False
    search = ['ore', 'monster']
    search_mob = ['zombie', 'creeper', 'skeleton']

    print("Would you like to use a torch and go deeper? (y/n)")
    select = input("> ")

    for i in inventory:
        if i[0] == 'torch' and i[1] > 0:
            have_torch = True

    if select == 'y' and have_torch == True:
        store('torch', -1)
        height -= 10
        find = search[random.randint(0,1)]

        if find == 'ore':
            block = cave_ore(height)
            print(f"You mine one {block}")
            while z != 3:
                print(".")
                time.sleep(.5 / current_pickaxe[4])
                z += 1
            if pickaxe(block) == True:
                if block == 'diamond':
                    achievements_list[1][0] += 1
                print(f"You get 1 {block}!")
                store(block, 1)
            else:
                print("Try using a better pickaxe")   
            deep_cave()
        else:
            fight_mob(search_mob[random.randint(0,2)])
            deep_cave()

    elif select == 'y' and have_torch == False:
        print("You're out of torches, returning to surface")
        input("> ")
        height = 64

    elif select == 'n':
        print("Returning to surface")
        input("> ")
        height = 64

    else:
        print("Learn to type")
        deep_cave()


def break_tree():

    z = 0
    amount = 0
    amount2 = 0
    achievements_list[2][0] += 1

    if random.randint(0,100) < 10:
        x = 1
    else:
        x = 0

    if x == 0:
        print("breaking tree")
        while z != 3:
            print(".")
            time.sleep(2)
            z += 1
        amount = random.randint(4,8)
        store('log', amount)
        print(f"You got {amount} logs!")

        if random.randint(0,100) < 10:
            amount2 = random.randint(1,4)
            print(f"You got {amount2} apples!")
            store('apple', amount2)
        else:
            print("Guess you're going to the doctor today!")
        input("> ")

    
    else:
        print("breaking big tree")
        while z != 6:
            print(".")
            time.sleep(2)
            z += 1
        amount = random.randint(10,18)
        store('log', amount)
        print(f"You got {amount} logs!")
        if random.randint(0,100) < 10:
            amount2 = random.randint(1,9)
            print(f"You got {amount2} apples!")
            store('apple', amount2)
        else:
            print("Guess you're going to the doctor today!")
        input("> ")

#Defines what mob you will find on an adventure
def mob():

    global animal
    global animal_night
    global night
    tick(1)
    mob_type = 0

    if night == False:
        mob_type = animal

    else:
        mob_type = animal_night

    mob = mob_type[random.randint(0, (len(animal)-1))]
    print(f"You run into a {mob}")
    fight_mob(mob)


def fight_mob(mob):

    global health
    global friend
    global foe

    select = 0
    wolf = ['wolf']
    

    if (mob) in friend:
        print(f"Would you like to kill the {mob} (y/n)")
        select = input("> ")
        if select == 'y':
            kill(mob)
        elif select == 'n':
            adventure()
        else:
            pass

    elif (mob) in wolf:
        print("You find a wolf!  Would you like to tame it?(y/n)")
        select = input("")
        if select == 'y':
            tame()

        elif select == 'n':
            adventure()

        else:
            pass

    else:
        print(f"Fight the {mob} or run (f/r)")
        select = input("> ")
        if select == 'f':
            fight(mob)
        else:
            if mob == 'creeper':
                print("Somehow you get away")
                input("> ")
            else:
                print(f"You run away and the {mob} hits you for 5 hp")
                health -= 5
                input("> ")

# function for killing['chicken', 'pig', 'cow', 'sheep]
def kill(mob):

    if mob == 'sheep':
        print(f"You kill the {mob}!")
        amount = random.randint(0,3)
        amount2 = random.randint(0,3)
        store('wool', amount)
        store('raw_lambchop', amount2)
        print(f"You get {amount} wool and {amount2} raw lambchop!")
        input(">")
    
    elif mob == 'chicken':
        print(f"You kill the {mob}!")
        amount = random.randint(0,3)
        amount2 = random.randint(0,3)
        store('feathers', amount)
        store('raw_chicken', amount2)
        print(f"You get {amount} feathers and {amount2} raw chicken!")
        input(">")
    
    elif mob == 'pig':
        print(f"You kill the {mob}!")
        amount = random.randint(0,3)
        store('raw_porkchop', amount)
        print(f"You get {amount} raw porkchop!")
        input(">")
    
    elif mob == 'cow':
        achievements_list[4][0] += 1
        print(f"You kill the {mob}!")
        amount = random.randint(0,3)
        amount2 = random.randint(0,3)
        store('raw_beef', amount)
        store('leather', amount2)
        print(f"You get {amount} raw beef, and {amount2} leather")
        input("> ")
    

def a1():
    print("@@@@@      TEXTCRAFT     @@@@@")

# function for fighting ['zombie', 'skeleton','spider', 'witch', 'slime', 'creeper']
def fight(mob):

    global health
    global damage
    
    #    print("What weapon")

    if mob == 'zombie':
        mob_health = 20

        while mob_health > 0:

            if random.randint(0,100) < 25:
                hurt = random.randint(3,10)
                health -= hurt
                print(f"The zombie bites you taking {hurt} hp")
            else:
                print("")
                input("Hit (enter) to attack!")
                if random.randint(0,100) < 90:
                    damage2 = damage * random.randint(1,3)
                    mob_health -= damage2
                    print(f"You hit the {mob} for {damage2} hp")
                else:
                    print("You miss")
            # DEATH                    
            if health <= 0:
                dead()
        
        if mob_health <= 0:
            print(f"The {mob} has fallen by your fist")##### {weapon}
            amount = random.randint(0,3)
            print(f"You get {amount} rotten flesh!")
            store('rotten_flesh', amount)
            input("> ")

   
    elif mob == 'skeleton':
        mob_health = 20

        while mob_health > 0:

            if random.randint(0,100) < 25:
                hurt = random.randint(3,10)
                health -= hurt
                print(f"The skeleton shoots you taking {hurt} hp")
            else:
                print("")
                input("Hit (enter) to attack!")
                if random.randint(0,100) < 90:
                    damage2 = damage * random.randint(1,3)
                    mob_health -= damage2
                    print(f"You hit the {mob} for {damage2} hp")
                else:
                    print("You miss")
            # DEATH
            if health <= 0:
                dead()
        
        if mob_health <= 0:
            print(f"The {mob} has fallen by your fist")##### {weapon}
            amount = random.randint(0,3)
            print(f"You get {amount} bone!")
            store('bone', amount)
            input("> ")


    elif mob == 'witch':
        mob_health = 26

        while mob_health > 0:

            if random.randint(0,100) < 25:
                hurt = random.randint(3,10)
                health -= hurt
                print(f"The witch throws a damage potion at you taking {hurt} hp")

            if random.randint(0,100) < 10:
                print("The witch heals itself with a potion")
                mob_health += 10
                if mob_health > 26:
                    mob_health = 26
            else:
                print("")
                input("Hit (enter) to attack!")
                if random.randint(0,100) < 90:
                    damage2 = damage * random.randint(1,3)
                    mob_health -= damage2
                    print(f"You hit the {mob} for {damage2} hp")
                else:
                    print("You miss")
            # DEATH
            if health <= 0:
                dead()
        
        if mob_health <= 0:
            print(f"The {mob} has fallen by your fist")##### {weapon}
            amount = random.randint(0,2)
            print(f"You get {amount} glass bottle")
            store('glass_bottle', amount)
            input("> ")


    elif mob == 'slime':
        mob_health = 16

        while mob_health > 0:

            if random.randint(0,100) < 25:
                hurt = random.randint(3,10)
                health -= hurt
                print(f"The slime stomps on you taking {hurt} hp")
            else:
                print("")
                input("Hit (enter) to attack!")
                if random.randint(0,100) < 90:
                    damage2 = damage * random.randint(1,3)
                    mob_health -= damage2
                    print(f"You hit the {mob} for {damage2} hp")
                else:
                    print("You miss")
            # DEATH
            if health <= 0:
                dead()
        
        if mob_health <= 0:
            print(f"The {mob} has fallen by your fist")##### {weapon}
            amount = random.randint(0,3)
            print(f"You get {amount} slimeball!")
            store('slimeball', amount)
            input("> ")


    elif mob == 'creeper':
        mob_health = 20
        blow_up = False

        while mob_health > 0:

            if random.randint(0,100) < 10:
                hurt = random.randint(40,61)
                health -= hurt
                print(f"The creeper blows up hurting you {hurt} hp")
                mob_health = 0
                blow_up = True
                input("> ")
            else:
                print("")
                input("Hit (enter) to attack!")
                if random.randint(0,100) < 90:
                    damage2 = damage * random.randint(1,3)
                    mob_health -= damage2
                    print(f"You hit the {mob} for {damage2} hp")

                else:
                    print("You miss")
            # DEATH
            if health <= 0:
                dead()
        
        if mob_health <= 0 and blow_up == False:
            print(f"The {mob} has fallen by your fist")##### {weapon}
            amount = random.randint(0,3)
            achievements_list[8][0] += 1
            print(f"You get {amount} gunpowder!")
            store('gunpowder', amount)
            input("> ")


    if mob == 'spider':
        mob_health = 16

        while mob_health > 0:

            if random.randint(0,100) < 25:
                hurt = random.randint(3,10)
                health -= hurt
                print(f"The spider bites you taking {hurt} hp")
            else:
                print("")
                input("Hit (enter) to attack!")
                if random.randint(0,100) < 90:
                    damage2 = damage * random.randint(1,3)
                    mob_health -= damage2
                    print(f"You hit the {mob} for {damage2} hp")

                else:
                    print("You miss")
            # DEATH
            if health <= 0:
                dead()
        
        if mob_health <= 0:
            print(f"The {mob} has fallen by your fist")##### {weapon}
            amount = random.randint(0,3)
            print(f"You get {amount} string!")
            store('string', amount)
            input("> ")  
        

def dead():
    #    select = 0
    #    deaths = 1
    print("You die, game over.")#  Total fatal incidents = {deaths}")
    input("(Enter)")
    exit(0 )
    #    print("Play again (y/n)")
    #    select = input("> ")
    #    while True:
    #        if select == 'n':
    #            exit(0)
    #        elif select == 'y':
    #            deaths += 1
    #            clear_save()
    #        else:
    #            pass
        


def view_inventory():

    k = 0
    m = 1
    select = 0
    is_sure = False
    selected_item = 0
    achievements_list[9][0] += 1
    print("Items")
    for i in inventory:
        if i[1] == 0:
            inventory.remove(i)

    for i in inventory:
            #MAX len 21
            text = (f"  {i[1]}-{i[0]}")
            var1 = 20 - len(text)
            print(text,' ' * var1, end = "")
            k += 1
            m += 1
            if k == 3:
                print("")
                k = 0
    print("Equipment")

    number_list(equipment, 0)


    print("Throw out an item or equipment? (i/e)")
    select = input("> ")

    if select == 'i':
        number_list(inventory, 0)
        print("")
        print("Select an item to destroy")
        try:
            select = int(input("> "))
            print("Are you sure? (y/n)")
            is_sure = input("> ")
            if is_sure:
                store(inventory[(select-1)][0], -(inventory[(select-1)][1]))
                input("(Enter)")

        except(ValueError, TypeError, IndexError):
            print("Invalid")
            input("(Enter)")

    elif select == 'e':
        number_list(equipment, 0)
        print("")
        print("Select an item to destroy")
        try:
            select = int(input("> "))
            select_item = equipment[(select-1)][0]
            print("Are you sure? (y/n)")
            is_sure = input("> ")
            if is_sure:
                store(select, -(inventory[(select-1)]))

        except(ValueError, TypeError, IndexError):
            print("Invalid")
            input("(Enter)")


    else:
        pass
    



def view_equipment():

    global picks
    global current_pickaxe
    global equipment
    x = 0
    z = 0
    y = 1
    a = 0
    old_pick = 0
    percentage1 = 0
    ready = False

    if len(current_pickaxe) > 1:
        percentage2 = math.ceil( 100* (current_pickaxe[1]) / current_pickaxe[3])
        print(f"Current - {current_pickaxe[0]} {percentage2}%")

    
    #[['wooden_pickaxe', 4, 1, 59], []]

    if len(equipment) > 0:
        
        for i in equipment:
            if i != None and len(equipment[0]) > 0:
                if i[1] != 0:
                    percentage1 = math.ceil( 100* (i[1]) / i[3])
                    print(f"#{y} {i[0]} {percentage1}% ", end = " ")
                    z += 1
                    if z == 2:
                        print("")
                        z = 0
                    y += 1

        print("")
        print("Equip a #?")
        try:
            select = input("# ")
            a = int(select) - 1
            select = equipment[a]
            for x in equipment:
                if select[0] == x[0]:
                    ready = True

            for i in picks:
                if equipment[a][0] == i and ready == True:
                    store(equipment[a][0], -1)                    
                    old_equipment(current_pickaxe)                    
                    current_pickaxe = x
                    print(f"{x[0]} equipped!")

        except (TypeError, ValueError, IndexError):
            input("(Exit)")

        


    else:
        print("You don't have any equipment")
        input("Exit")


def old_equipment(x):
    if x[0] != 'fist':
        equipment.append(x)


def tame():

    select = 0
    bone = 0
    global damage

    for i in inventory:
        if i[0] == 'bone' and i[1] >= 1:
            bone = True

    if bone == True:
        print("Use bone? (y/n)")
        select = input("> ")
        if select == 'y':
            store('bone', -1)
            if random.randint(0,100) < 20:
                achievements_list[7][0] += 1
                print("Tame successful, your damage increases by 1")
                damage += 1
                input("> ")
            else:
                print("Tame unsuccessful")
                tame()
        else:
            print("OKAY")

    else:
        print("Sorry you don't have any more bones")
        input("> ")


def bed_sleep():

    global night
    have_bed = False

    for i in inventory:
        if i[0] == 'bed':
            have_bed = True

    if have_bed == False and night == False:
        print("You can't sleep on the ground, silly")
        input("> ")
    elif night == False:
        print("No naps allowed, sleep at night...")
        input("> ")

    else:
        tick(100)
    
        

# cook_output
def furnace():

    z = 0
    y = 0
    p = 0
    ape = 0
    query = 0
    quantity_unit = 0
    quantity_fuel = 0
    select_unit = 0
    select_fuel = 0
    can_cook = False
    have_fuel = False
    furnace_have = False
    cook_list = []
    fuel_list = []

    for i in inventory:
        if i[0] == 'furnace':
            furnace_have = True

    for x in inventory:
        for i in cook_output:
            if x[0] == i[0] and x[1] > 0:
                cook_list.append(i[0])
                can_cook = True

    for i in inventory:
        for x in fuel:
            if x[0] == i[0] and i[1] >= 1:
                have_fuel = True
                fuel_list.append(x[0])

    if furnace_have == False:
        print("Try crafting a furnace first")
        input("> ")
    else:
        if can_cook == True and have_fuel == True:
            try:
                k = 1
                print("What would you like to cook?")
                number_list(cook_list, -1)

                print("")
                select_unit = int(input("> "))
                select_unit = cook_list[(select_unit - 1)]
            except(ValueError, IndexError):
                pass
            if select_unit in cook_list:
                try:
                    k = 1
                    print("What fuel would you like to use?")
                    number_list(fuel_list, -1)

                    print("")
                    select_fuel = int(input("> "))
                    select_fuel = fuel_list[(select_fuel - 1)]
                except(ValueError, IndexError):
                    pass

                # This is where the actual cooking happens
                if select_fuel in fuel_list:
                    # discovering the quantities in inventory and how many the fuel can burn
                    for i in inventory:
                        if select_unit == i[0]:
                            quantity_unit = i[1]
                    for i in fuel:
                        if select_fuel == i[0]:
                            quantity_fuel = i[1]
                        
                    while ape != 'q':

                        print(f"How many would you like to cook? You have {quantity_unit}")
                        print(f"and {select_fuel} only cooks {quantity_fuel}")
                        select = input("> ")
                        try:
                            if int(select) <= quantity_fuel:
                                quantity_unit = int(select)####
                                if int(quantity_unit) > int(quantity_fuel):
                                    total_cooked = int(quantity_fuel)
                                else:
                                    total_cooked = int(quantity_unit)
                                print("Cooking")
                                while p != 3:
                                    print(".")
                                    time.sleep(1 * total_cooked)
                                    p += 1

                                for i in cook_output:
                                    if select_unit == i[0]:
                                        select_unit2 = i[1]

                                print(f"You cook {total_cooked} {select_unit} with your {select_fuel}")
                                print(f"Giving you {total_cooked} {select_unit2}")
                                store(select_unit2, total_cooked)
                                store(select_fuel, -1)
                                store(select_unit, -total_cooked)
                                input("> ")


                                ape = 'q'

                            elif int(select) > quantity_unit:
                                print("You don't have that many dummy!")
                                input("> ")
                            elif int(select) > quantity_fuel:
                                print("Your fuel won't last that long")
                                input("> ")
                        
                            else:
                                ape = 'q'

                        except ValueError:
                            ape = 'q'



        else:
            print("Cooks you can't")
            if can_cook == True:
                print("No fuel!")
            input("> ")


# tick(0) checks the clock
# tick(x) checks clock and moves time forward by x
def tick(x):

    global clock
    if x == 0:
        if clock < 100:
            print("  Birds are singing in the sunlight...")
        else:
            print("  Crickets are chirping in the moonlight...")

    # For sleeping
    elif x == 100:
        night = False
        print("=========================")
        print("=========================")
        print("The sun has RISEN!")
        print("=========================")
        print("=========================")
        clock = 0

    else:
        clock += x
        if clock == 100:
            night = True
            print("=========================")
            print("=========================")
            print("The sun has FALLEN!")
            print("=========================")
            print("=========================")
        if clock == 200:
            night = False
            print("=========================")
            print("=========================")
            print("The sun has RISEN!")
            print("=========================")
            print("=========================")
            clock = 0

# x is the list to print. y is the list indice(-1 for no indice) diamond_pickaxe
def number_list(x,y):
    m = 1
    k = 0
    var1 = 0
    text = 0
    done = False
    if y != -1:

        for i in x:
            
            #MAX len 21
            text = (f"  #{m} {i[y]}")
            var1 = 21 - len(text)
            print(text,' ' * var1, end = "")
            k += 1
            m += 1
            if k == 3:
                print("")
                k = 0
    else:

        for i in x:
            
            #MAX len 20
            text = (f" #{m} {i}")
            var1 = 20 - len(text)
            print(text,' ' * var1, end = "")
            k += 1
            m += 1
            if k == 3:
                print("")
                k = 0


select = 0
def start():

    # variables
    global night
    global health
    global height
    global damage
    global clock
    global select
    global furnace

    # lists
    global crafting
    global cook_output
    global inventory
    global fuel
    global edible
    
    

    question = ("""What would you like to do?
    (a)dventure
    (c)raft
    (d)ig down
    (e)at
    (f)urnace
    (s)leep
    (m)enu""")

    cls()
    # Checking time
    tick(0)
    # Checking for new achievements
    achievements(1)
    print('  Health('+ (int(health/10)*2)*'@'+ ((-(int(health/10)-10))*2)*'-' + ')')
    print(question)

    select = input("> ")
    
    if select == 'a':# adventure()
        adventure()

    elif select == 'd':# dig_down()
        dig_down(height)

    elif select == 'c':# craft
        craft()
    
    elif select == 'f':# furnace
        furnace()
    
    elif select == 'e':# eat
        eat()
    
    elif select == 's':# sleep
        bed_sleep()
    
    elif select == 'm':# menu
        menu()
    
    else:
        cls()
        print("Try again")
def version(x):
    global test
    print(f"     v.{x}", end = " ")
    if x == 'test':
        test = True
        print("")
    else:
        input("(Enter)")

a4()

#version('test')
version('pre-alpha')




while True:
    if test:
        start()
    else:
        try:
            start()
        except Exception:
            print("This is broken lol Error### bleehgfajfasaofowaowo.   wkkd        .")
            input("> ")


    








