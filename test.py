import random
import time
import os
import math
import curses

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
# 11 millionaire
]

try:
    import textcraft123
except ModuleNotFoundError:
    with open('textcraft123.py', 'w') as file:
        file.write("inventory = []\n")
        file.write("all_farms = []\n")
        file.write("base = [0, 0, 100, 1, 0, 0, ['fist', -1, 0, -1, 1], 'user_id']\n")
        file.write("achieved = []\n")
        file.write("equipment = []\n")
        file.write("achievements_list =  ")
        file.write(str(achievements_list))
        print("Please hold...")
        time.sleep(2)

import textcraft123

inventory = textcraft123.inventory
all_farms = textcraft123.all_farms
base = textcraft123.base
achieved = textcraft123.achieved
equipment = textcraft123.equipment
achievements_list = textcraft123.achievements_list

test = False
night = base[0]
furnace_have = base[1]
health = base[2]
damage = base[3]
clock = base[4]
money = base[5]
current_pickaxe = base[6]
user_id = base[7]

height = 64
current_time = math.floor(time.time())



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
    ['bread', 'wheat', 3, 1],
    ['paper', 'sugar_cane', 3, 1],
    ['book', 'leather', 1, 'paper', 3],
    ['book_shelf', 'wood_plank', 6, 'book', 3]
    
]


cook_output = [
    ['iron_ore', 'iron'], ['raw_porkchop', 'cooked_porkchop'], ['raw_beef', 'cooked_beef'],
    ['gold_ore', 'gold'], ['cobblestone', 'stone'], ['log', 'coal'], ['raw_fish', 'cooked_fish'],
    ['raw_lambchop', 'cooked_lambchop'], ['raw_chicken', 'cooked_chicken']
]



# type, current durability




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
    ['apple', 8], ['rotten_flesh', 3], ['raw_fish', 5], ['cooked_fish', 15], ['cooked_chicken', 20],
    ['cooked_lambchop', 20], ['raw_chicken', 5], ['raw_lambchop', 5], ['bread', 20]
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
# 11 millionaire
]


# START FARMING LISTS
# START FARMING LISTS



farm_materials = [
    ['log', 50000],
    ['stone', 20000],
    ['iron_block', 5000],
    ['diamond_block', 2000],
    ['obsidian', 10],
    ['bedrock', 3]
]

# END FARMING LISTS
# END FARMING LISTS

prices = [
    ['log', 1], ['cobble', 2], ['gravel', 2], ['diamond', 20], ['apple', 10],
    ['iron', 5], ['leather', 5], ['redstone', 5], ['obsidian', 20], ['stone', 3],
    ['bedrock', 340]
]
#--------------------------------------
def input_char(message,y):
    #try:
    win = curses.initscr()
    win.clear()
    msg1 = None
    if y == 1:
        msg1 = ''
        for i in message:
            msg1 += str(i)
    else:
        msg1 = message
    win.addstr(0, 0, msg1)
    while True: 
        ch = win.getch()
        if ch in range(32, 127): break
        if ch == 10: break
        time.sleep(0.05)
    #except: raise
    #finally:
    curses.endwin()
    return chr(ch)

#--------------------------------------
def input(x,y):
    c = input_char(x,y)
    try:
        return int(c)
    except:
        return c

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

    
    # need to water? 0 or 1/ , need to rebuild 0 or 1, 
    #               return [water, rebuild]

    while select != 'q':
        cls()
        need_msg = ''
        x = 1
        try:

            if have_farm == True:   
                #if farm_selected:
                #    EventFarm(0, selected_farm)  # 1 is check for things that need to be done 
                #else:
                #    pass

                if selected_farm:
                    need_msg = (f"   level-{selected_farm[8]} {selected_farm[0]}|{selected_farm[10]} farm is selected!\n")
                    need_msg += (EventFarm(1, selected_farm))  
                msg = need_msg + ("""What would you like to do?
    (s)elect a farm
    (w)ater
    (h)arvest
    (l)evel up
    (n)otifications
    (b)uild new farm
    (d)estroy
    (q)uit\n""")# add are you sure on destroy

                select = input(msg)
                try:
                    if select == 'n': # Notifications
                        cls()
                        msg = ''
                        msg += EventFarm(0, all_farms)
                        msg += ("(press any key)\n")
                        input(msg, 0)

                    elif select == 's': # Select a farm
                        msg = ''
                        for i in current_farms:
                            msg += (f"#{x} level-{i[8]} {i[0]}|{i[10]}\n")
                            x += 1
                        try:
                            select = int(input(msg), 1)
                            if select:
                                selected_farm = current_farms[(select-1)]
                                farm_selected == True

                        except (ValueError, IndexError, TypeError):
                            msg = ''
                            msg += ("Invalid selection\n")
                            input(msg, 0)


                    elif select == 'w' and selected_farm != 0: # Water selected
                        EventFarm(2, selected_farm)

                    elif select == 'h' and selected_farm != 0: # Harvest selected
                        EventFarm(3, selected_farm)

                    elif select == 'l' and selected_farm != 0: # level selected
                        EventFarm(5, selected_farm)

                    elif select == 'd' and selected_farm != 0: # Destroy
                        msg = ''
                        msg += ("Are you sure you want to destroy this farm? (y/n)\n")
                        select = input(msg)
                        if select == 'y':
                            EventFarm(6, selected_farm)
                    
                    elif select == 'b':# build farm
                        build_farm()
                        select = 'q'

                    elif select == 'q': # Quit
                        pass

                    elif selected_farm == 0:
                        msg = ''
                        msg += ("No farm selected\n")
                        input(msg, 0)

                    else:
                        msg = ''
                        msg += ("Not an option\n")
                        input(msg, 0)
                except IndexError:
                    msg = ''
                    msg += ("Invalid\n")
                    input(msg, 0)
                
            
            else:
                msg = ''
                msg += ("You don't have any farms")
                msg += ("Build one? (y/n)\n")
                select = input(str(msg), 1)

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
    # 0 is notification
    # 1 is check for things that need to be done on y farm
    # 2 is water
    # 3 is harvest
    # 4 is build
    # 5 is level up
    # 6 is destroy
    select = 0
    have_farm = False
    something_happend = False
    for i in all_farms:
        if i[1] > 0:
            have_farm = True
    if x == 1:
        msg = ''
        if y[3] == 0:
            msg += ("   Needs to be watered.\n")
        elif y[4] == 1:
            msg += ("   Needs to be harvested.\n")
        return msg

    elif x == 2:
        water_farm(y)
    elif x == 3:
        harvest_farm(y)
    elif x == 4:
        all_farms.append(y)
    elif x == 5:
        level_farm(y)
    elif x == 6:
        msg = (f"Are you sure you want to destroy {y[0]} farm? (y/n)\n")
        select = input(str(msg), 1)
        if select == 'y':
            all_farms.remove(y)
        else:
            pass

    # 0type, 1is built, 2cost, 3has_water, 4ready to be harvested,5time_passed,6time_waterd
    #  7time needs water , 8level ,9[material ,chance of storm breaking]
        #['wheat', 1, 500, 0, 0, 0, 0, 3600, 1, [dirt, 50000]
    #['bedrock', .0001]
    else:# 0
        global current_time
        time_passed = 0
        time_passed = (math.floor(time.time())) - current_time + time_passed #seconds
        current_time = math.floor(time.time())
        time_passed_storm = time_passed

        for i in all_farms:
            if i[1] == 1:
                i[5] += time_passed
        storm = False
        need_water = False
        need_harvest = False
        what_happend = 0
        affected_farms1 = []
        affected_farms2 = []
        affected_farms3 = []
        #Storm 1
        #Crops dried up 2
        #Crops ready to harvest 3

        #STORM checks for every hour passed
        while time_passed_storm > 1800:
            #%10 chance of a storm passing each farm every hour
            for i in all_farms:
                if i[1] == 1:
                    if random.randint(0,100) < 20:
                        if random.randint(0,1000000) < i[9][1]:
                            storm = True
                            what_happend = True
                            affected_farms1.append(i)
                            all_farms.remove(i)

            time_passed_storm -= 1800

    # 0type, 1is built, 2cost, 3has_water, 4ready to be harvested,5time_passed,6time_waterd
    #  7time needs water , 8level ,9[material ,chance of storm breaking]
        #['wheat', 1, 500, 0, 0, 0, 0, 3600, 1, 50000]
    #['bedrock', .0001]
        for i in all_farms:
            if i[5] >= 1800:
                i[3] = 0
                i[6] += 1800

        for i in all_farms:
            if i[1] == 1 and i[3] == 0:
                if i[6] >= i[7]:
                    i[6] = 0
                    i[4] = 1
                else:
                    affected_farms2.append(i)
                    need_water = True
                    what_happend = True
        
        for i in all_farms:
            if i[4] == 1:
                affected_farms3.append(i)
                need_harvest = True
                what_happend = True


        if have_farm and what_happend:
            msg = ''
            if storm:
                msg += ("    A storm came by\n")
                for i in affected_farms1:
                    msg += (f"    level-{i[8]} {i[0]}|{i[10]} farm has been destroyed...\n")


            if need_water:
                msg += ("    Farm needs water\n")
                for i in affected_farms2:
                    msg += (f"    level-{i[8]} {i[0]}|{i[10]}\n")


            if need_harvest:
                msg += ("    Farm is ready to be harvested\n")
                for i in affected_farms3:
                    msg += (f"    level-{i[8]} {i[0]}|{i[10]}\n")
                    msg += ("(press any key)\n")
            return msg



        else:
            return ''

def water_farm(x):

    enough_buckets = False
    # x is the selected farm
    # 0type, 1is built, 2cost, 3has_water, 4ready to be harvested,5time_passed,6time_waterd
    #  7time needs water , 8level ,9[material ,chance of storm breaking]
        #['wheat', 1, 500, 0, 0, 0, 0, 3600, 1, [dirt, 50000]
    for i in inventory:
        if i[0] == 'water_bucket' and i[1] >= 20 + ((x[8]-1)*3):
            enough_buckets = True

    if enough_buckets == True and x[3] == 0:
        cls()
        msg = ''
        msg += (f"{x[0]} farm has been watered!\n")
        for i in all_farms:
            if x == i:
                i[3] = 1
        store('bucket', (20+ ((x[8]-1)*3)))
        store('water_bucket', (-20+ ((x[8]-1)*3)))
        input(msg, 0)

    elif enough_buckets == True and x[3] == 1:
        cls()
        msg = ''
        msg += ("This farm is already watered!\n")
        input(msg, 0)

    elif x[3] == 1:
        cls()
        msg = ''
        msg += ("This farm is already watered!\n")
        input(msg, 0)

    else:
        cls()
        msg = ''
        msg += ("You don't have enough water!\n")
        msg += (f"You need {(20+ ((x[8]-1)*3))} buckets of water\n")
        input(msg, 0)

def harvest_farm(x):

    # 0type, 1is built, 2cost, 3has_water, 4ready to be harvested,5time_passed,6time_waterd
    #  7time needs water , 8level ,9[material ,chance of storm breaking]
        #['wheat', 1, 500, 0, 0, 0, 0, 3600, 1, [dirt, 50000]
    amount_received = 0

    if x[4] == 1:
        for i in all_farms:
            if x == i:
                i[3] = 0
                i[4] = 0
                amount_received = (i[8] * 10 * i[8])
                store((i[0]), amount_received)
                cls()
                msg = ''
                msg += (f"Farm harvested you get {amount_received} {i[0]}\n")
                input(msg, 0)
    else:
        cls()
        msg = ''
        msg += ("Not ready to be harvested\n")
        input(msg, 0)

def level_farm(x):

   # 0type, 1is built, 2cost, 3has_water, 4ready to be harvested,5time_passed,6time_waterd
    #  7time needs water , 8level ,9[0material ,1chance of storm breaking]
        #['wheat', 1, 500, 0, 0, 0, 0, 3600, 1, [dirt, 50000]

    global money
    select = 0
    z = 0
    k = 0
    base_level_cost = [10, 10, 4, 10]
    level_cost = [i * 2 * x[8] for i in base_level_cost]
    have_material = False
    have_plank = False
    have_dirt = False
    have_money = False
    level_farm = False
    cls()
    msg = ''
    msg += (f"""Leveling up your farm costs
    {level_cost[0]} - {x[9][0]}
    {level_cost[1]} - wood_plank
    {level_cost[2]} - dirt
    {level_cost[3]}$\n""")
    msg += ("Be sure you harvest before leveling!\n")
    msg += ("Continue with level up? (y/n)\n")
    select = input(str(msg), 1)

    if select == 'y':
        for i in inventory:
            if i[0] == (x[9][0]) and i[1] >= level_cost[0]:
                have_material = True
            if i[0] == 'wood_plank' and i[1] >= level_cost[1]:
                have_plank = True
            if i[0] == ('dirt') and i[1] >= level_cost[2]:
                have_dirt = True
        if money > level_cost[3]:
            have_money = True

        if have_material and have_plank and have_dirt and have_money:
            for i in all_farms:
                if x == i:
                    level_farm = True
                    i[8] += 1
                    i[3] = 0
                    i[6] = 0
                    i[4] = 0
                    
                    store((x[9][0]), -(level_cost[0]))
                    store('wood_plank', -(level_cost[1]))
                    store('dirt', -(level_cost[2]))
                    money_add(-(level_cost[3]))
    # 0type, 1is built, 2cost, 3has_water, 4ready to be harvested,5time_passed,6time_waterd
    #  7time needs water , 8level ,9[0material ,1chance of storm breaking]
                
        else:
            cls()
            msg = ''
            msg += ("You don't have enough materials...\n")
            input(msg, 0)

        if level_farm:
                    
            while z != 4:
                if z == 0:
                    cls()
                    print("Leveling up farm!\n")
                    while k != 2:
                        print(".\n")
                        time.sleep(.5)
                        k += 1
                    msg = '(press any key)\n'
                    input(msg, 0)
                    k = 0
                elif z == 1:
                    cls()
                    print(f"building more {x[9][0]} supports")
                    while k != 2:
                        print(".\n")
                        time.sleep(.5)
                        k += 1
                    msg = '(press any key)\n'
                    input(msg, 0)
                    k = 0
                elif z == 2:
                    cls()
                    print("dumping more dirt")
                    while k != 2:
                        print(".\n")
                        time.sleep(.5)
                        k += 1
                    input("add more decoration?\n", 0)
                    k = 0
                elif z == 3:
                    cls()
                    print("decorating")
                    while k != 2:
                        print(".\n")
                        time.sleep(.5)
                        k += 1
                    

                z += 1
            input("Farm leveled up!\n", 0)

    else:
        pass

def build_farm():
    # $, material, wood_plank, dirt, money
    # base_farm_cost = [100, 100, 40, 100]
    select = 0
    farm_selected = False
    have_enough_materials = False
    have_enough_wood_plank = False
    have_enough_dirt = False
    have_enough_materials_to_build = False
    farm_types = [
    # 0type, 1is built, 2cost, 3has_water, 4ready to be harvested,5time_passed,6time_waterd
    #  7time needs water , 8level ,9[material ,chance of storm breaking]
        #['wheat', 1, 500, 0, 0, 0, 0, 3600, 1, [dirt, 50000]
    #['bedrock', .0001]
    ['wheat', 1, 500, 0, 0, 0, 0, 3600, 1],
    ['log', 1, 1000, 0, 0, 0, 0, 5000, 1],
    ['sugar_cane', 1, 1000, 0, 0, 0, 0, 4000, 1],
    ['bone', 1 ,10000000, 0, 0, 0, 0, 28800, 1]
    ]

    for i in inventory:
        if i[0] == 'wood_plank' and i[1] >= 100:
            have_enough_wood_plank = True
        if i[0] == 'dirt' and i[1] >= 40:
            have_enough_dirt = True

    if have_enough_dirt and have_enough_wood_plank:
        have_enough_materials_to_build = True

    while select != 'q':
        cls()
        z = 0
        x = 1
        k = 0
        msg = ''
        msg += ("What would you like to build it out of?\n")
        number_list(farm_materials, 0)

        msg += ("(q)uit")
        select = input(str(msg), 1)
        if select != 'q':
            try:
                select = int(select)
                if select:
                    choice_material = farm_materials[(select-1)]# material chosen

                    for i in inventory:
                        if i[0] == choice_material[0] and i[1] >= 100:
                            have_enough_materials = True

                    if have_enough_materials:
                        msg = ("What kind of farm do you want?\n")
                        x = 1
                        for i in farm_types:
                            msg += (f"#{x} {i[0]} ${i[2]}, 100 wood_plank, and 40 dirt")
                            x += 1
                        select = input(msg , 1)
                        select = int(select)
                        select = farm_types[(select-1)]
                        if have_enough_materials_to_build and money > select[2]:
                            select.append(choice_material)
                            select.append(len(all_farms) + 1)
                            input(f"Building {select[0]} farm!\n", 0)

                            while z != 4:
                                if z == 0:
                                    cls()
                                    print("adding fence posts")
                                    while k != 6:
                                        print(".\n")
                                        time.sleep(.5)
                                        k += 1
                                    input((("(press any key)\n")), 0)
                                    k = 0
                                elif z == 1:
                                    cls()
                                    print(f"building the {choice_material[0]} supports")
                                    while k != 6:
                                        print(".\n")
                                        time.sleep(.5)
                                        k += 1
                                    input((("(press any key)\n")), 0)
                                    k = 0
                                elif z == 2:
                                    cls()
                                    print("dumping the dirt")
                                    while k != 6:
                                        print(".\n")
                                        time.sleep(.5)
                                        k += 1
                                    input("decorate?\n",0)
                                    k = 0
                                elif z == 3:
                                    cls()
                                    print("decorating")
                                    while k != 6:
                                        print(".\n")
                                        time.sleep(.5)
                                        k += 1
                                    

                                z += 1
                            cls()
                            input(f"{select[0]} farm is complete!\n", 0)
                            EventFarm(4, select)
                            select = 'q'
                            farming()                                               

                        elif have_enough_materials_to_build:
                            input("You don't have enough cash.\n", 0)
                            select = 'q'

                        else:
                            input("You don't have enough materials.\n", 0)
                            select = 'q'
                    else:
                        input(f"You don't have 100 {choice_material[0]}\n", 0)

            except (ValueError, IndexError, TypeError):
                input("Not Valid\n", 0)

        else:
            pass


# x is whether to show all achievements or check for gained and notify(0 or 1)
def achievements(x):
    has = False
    msg = ''
    if x == 0:
        
        for i in achievements_list:
            if i[1] == 1:
                msg += (i[2])
                msg += ("\n")
                has = True

        if has == False:
            input("You don't have any, lol.\n", 0)
        else:
            return msg

    else:
        for i in achievements_list:
            if i[1] == 0 and i[0] >= i[3]:
                achieved.append(i[2])
                i[1] = 1
                msg += ("=========================\n")
                msg += ("=========================\n")
                msg += (f"You got {i[2]} achievement for {i[4]}!\n")
                msg += ("=========================\n")
                msg += ("=========================\n")
        return msg


def menu():
    msg = ''
    msg += ("What would you like to do?\n")
    msg += ("""    (f)arm
    (e)quipment
    (i)nventory
    (a)chievements
    (q)uit\n""")
    select = input(str(msg), 1)

    if select == 'a':
        achievements(0)
    elif select == 'f': # farm
        farming()
    elif select == 'i': # inventory
        view_inventory()
    
    elif select == 'e': # equipment
        view_equipment()

    elif select == 'q':
        choice = input("Would you like to save your game? (y/n)\n", 1)
        if choice == 'y':
            with open('textcraft123.py', 'w') as file:
                file.write("inventory = ")
                file.write(str(inventory))
                file.write("\n")
                file.write("all_farms = ")
                file.write(str(all_farms))
                file.write("\n")
                file.write("equipment = ")
                file.write(str(equipment))
                file.write("\n")
                file.write("achieved = ")
                file.write(str(achieved))
                file.write("\n")
                file.write("achievements_list = ")
                file.write(str(achievements_list))
                file.write("\n")
                global night
                global furnace_have
                global health
                global damage
                global clock
                global money
                global current_pickaxe
                global user_id
                base = []
                base.append(night)
                base.append(furnace_have)
                base.append(health)
                base.append(damage)
                base.append(clock)
                base.append(money)
                base.append(current_pickaxe)
                base.append(user_id)
                file.write("base = ")
                file.write(str(base))
            input("BYEEEE\n", 0)
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
    msg = ''
    msg += ("Items you can craft\n")
    while k == 1:
        try:
            msg += number_list(available, 0)

            msg += ("\n")
            msg += ("What would you like to craft?\n")
            select = int(input(str(msg), 1))
            select = available[(select -1)][0]
            k = 2
        except(TypeError, ValueError, IndexError):
            k = 3
            msg = ''
            msg += ("Invalid selection\n")
            input(msg, 0)


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
                    msg = ''
                    msg += (f"Make {select} how many times? 0-{possible}(enter 0 to cancel)\n")

                    try:
                        select2 = int(input(str(msg), 1))
                        quantity2 = select2

                        if quantity2 < 0:
                            input("Must be greater than zero\n", 0)

                        elif quantity2 == 0:
                            done = True
                            done2 = True

                        elif quantity2 <= possible:
                            done = True

                        else:
                            input("You don't have that many!\n", 0)

                    except (TypeError, ValueError) as e:
                        input("Numbers only please", 0)


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
                    input(msg, 0)

    
def a2():
    return ("@@@@@      Skelouse      @@@@@\n")
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
            input("You don't have anything to eat", 0)
        else:
            cls()
            health_bar()
            health_added = 0
            food_selected = 0
            y = 0
            food_list = []
            for i in inventory:
                for x in edible:
                    if x[0] == i[0] and i[1] >= 1:
                        food_list.append(x[0])
            while query != 'q':
                msg = ''
                try:
                    x = 1
                    msg += ("What are you hungry for?\n")
                    number_list(food_list, -1)
                    select = int(input(str(msg), 1))
                    select = food_list[(select - 1)]
                    query = 'q'
                    
                except (ValueError, TypeError, IndexError):
                    have_food = False
                    query = 'q'
            while have_food:
                health_added = 0
                select2 = 0
                if select in semi_edible:
                    
                    if random.randint(0,100) < 70:
                        
                        for x in edible:
                            if x[0] == select:
                                tick(1)
                                health_added = x[1]
                                food_selected = x[0]
                                store(food_selected, -1)
                                health += health_added
                                cls()
                                health_bar()
                                msg = ''
                                msg += ("Ehh...\n")
                                msg += (f"You eat {food_selected} for {health_added} hp.\n")
                                achievements_list[10][0] += 1
                                if health >= 100:
                                    msg += ("Your health is full!\n")
                                    input(msg, 0)
                                    health = 100
                                else:
                                    input(msg, 0)


                    else:
                        for x in edible:
                            if x[0] == select:
                                tick(1)
                                health_added = -(x[1])
                                food_selected = x[0]
                                store(food_selected, -1)
                                health += health_added
                                cls()
                                health_bar()
                                msg = ''
                                msg += ("Yuck...\n")
                                msg += (f"The {food_selected} poisons you, taking {health_added} hp!\n")
                                input(msg, 0)
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
                        msg = ''
                        msg += (f"{quantity} left, eat another? (y/n)\n")
                        select2 = input(str(msg), 1)

                        if select2 == 'y':
                            pass
                        else:
                            have_food = False
                    else:
                        input("No more food!\n", 0)
                        have_food = False



                elif select in food_list:
                    
                    for x in edible:
                        if x[0] == select:
                            tick(1)
                            health_added = x[1]
                            food_selected = x[0]
                    
                    store(food_selected, -1)
                    health += health_added
                    cls()
                    health_bar()
                    msg = ''
                    msg += ("Yummy...\n")
                    msg += (f"You eat {food_selected} for {health_added} hp\n")
                    achievements_list[10][0] += 1
                    if health >= 100:
                        msg += ("Your health is full!\n")
                        input(msg, 0)
                        health = 100
                    else:
                        input(msg, 0)

                    have_food = False
                    quantity = 0
                    for i in inventory:
                        if i[0] == food_selected:
                            quantity = i[1]
                            if quantity >= 1:
                                have_food = True
                    if quantity and have_food:
                        msg = (f"{quantity} left, eat another? (y/n)\n")
                        select2 = input(str(msg), 1)

                        if select2 == 'y':
                            pass
                        else:
                            have_food = False
                    else:
                        input("No more food!\n", 0)
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
        print(".\n")
        time.sleep(.5 / current_pickaxe[4])
        z += 1
    


    
    if block != 'bedrock' and block != 'lava':
        
        if pickaxe(block) == True:
            if block == 'diamond':
                    achievements_list[1][0] += 1
            msg = ''
            msg += (f"You get 1 {block}!\n")
            input(msg, 0)
            cls()
            store(block, 1)
        else:
            msg = ''
            msg += ("Try using a better pickaxe\n")
            input(msg, 0)
            cls()

        height -= 1
        health_bar()
        msg = ''
        msg += ("Climb back up or keep digging(c/d)\n")
        select = input(str(msg), 1)
        if select == 'c':
            input("You climb back to the surface\n", 0)

        elif select == 'd':
            dig_down(height)
        else:
            input("Returning to surface\n", 0)

    else:
        bucket = False
        if block == 'lava':
            for i in inventory:
                if i[0] == 'water_bucket' and i[1] > 0:
                    bucket = True
            
            if bucket == False:
                msg = ''
                msg += ("OUCH LAVA BURNS!\n")
                msg += ("Bring a water bucket next time.\n")
                input(msg, 0)
                dead()
            else:
                achievements_list[3][0] += 1
                msg = ''
                msg += ("You use your water bucket to turn the lava into obsidian\n")
                msg += ("You also lose 10 hp from well, lava\n")
                health -= 10
                if health <= 0:
                    dead()
                block = 'obsidian'
                store('water_bucket', -1)
                store('bucket', 1)

                if pickaxe(block) == True:
                    msg += (f"You get 1 {block}!\n")
                    input(msg, 0)
                    cls()
                    store(block, 1)
                else:
                    msg += ("Try using a better pickaxe")
                    input(msg, 0)

                height -= 1
                health_bar()
                msg = ''
                msg = ("Climb back up or keep digging(c/d)\n")
                select = input(str(msg), 1)

                if select == 'c':
                    input("You climb back to the surface", 0)

                elif select == 'd':
                    cls()
                    dig_down(height)
                else:
                    input("Returning to surface", 0)

        else:
            msg = ''   
            msg += ("You can't mine through bedrock silly!\n")
            msg += ("Returning to surface")
            input(msg, 0)

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
                input("Your pickaxe has broken...\n", 0)
                current_pickaxe = ['fist', -1, 0, -1, 1]

            return True
    if can_mine == False:
        return False


def a4():
    msg = (a1()+a2()+a3())
    return msg

# Defines what you find on an adventure
def adventure():

    tick(1)
    search = ['tree','tree', 'tree', 'tree',
 'tree', 'tree', 'river', 'animal', 'animal', 'cave']

    if random.randint(0,100) < 20:
        search.append('villager')

    end = search[random.randint(0, (len(search)-1))]

    if end == 'animal':
        cls()
        mob()

    elif end == 'tree':
        msg = ''
        msg += ("You find a tree\n")
        msg += ("Do you want to cut it down(y/n)\n")
        select = input(str(msg), 1)
        if select == 'y':
            cls()
            break_tree()
        elif select == 'n':
            cls()
            adventure()
        else:
            pass

    elif end == 'river':
        cls()
        river()

    elif end == 'cave':
        cls()
        cave()

    elif end == 'villager':
        cls()
        villager()
    
    else:
        input("ERROR in def adventure\n", 0)


def river():

    rod = False
    bucket = False
    msg = ''
    msg += ("You see a river!\n")
    for i in inventory:
        if i[0] == 'fishing_rod':
            rod = True

    for i in inventory:
        if i[0] == 'bucket':
            bucket = True

    if bucket == True and rod == True:
        msg += ("Would you like to fish or fill your bucket with water?(f/b)\n")
        select = input(str(msg), 1)
        if select == 'f':
            cls()
            fish()
        elif select == 'b':
            cls()
            fill_bucket()
        else:
            pass

    elif bucket == True:
        msg += ("would you like to fill a bucket with water?(y/n)\n")
        select = input(str(msg), 1)
        if select == 'y':
            cls()
            fill_bucket()

    elif rod == True:
        msg += ("would you like to fish?(y/n)\n")
        select = input(str(msg), 1)
        if select == 'y':
            cls()
            fish()

    else:
        msg += ("Sorry there's nothing for you here.\n")
        msg += ("Keep adventuring?(y/n)\n")
        select = input(str(msg), 1)
        if select == 'y':
            cls()
            adventure()
        else:
            pass


def fill_bucket():

    tick(1)
    bucket = True

    while bucket == True:
        z = 0
        input("Your bucket fills up\n", 0)
        achievements_list[5][0] += 1
        
        while z != 3:
            print(".\n")
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
            msg = ''
            msg += ("Fill another bucket? (y/n)\n")
            select = input(str(msg), 1)

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
        print(".\n")
        time.sleep(1)
        z += 1

    if random.randint(0,100) < 30:
        msg = ''
        msg += ("You caught a fish!\n")
        achievements_list[6][0] += 1
        store('raw_fish', 1)
        msg += ("Continue fishing? (y/n)\n")
        select = input(str(msg), 1)
        msg = ''

    else:
        msg = ''
        msg += ("No bite, keep fishing? (y/n)\n")
        select = input(str(msg), 1)

    if select == 'n':
        input("The river waves goodbye", 0)
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
    msg = ''
    msg += ("You peer into the entrance of a cave.\n")
    msg += ("Will you dare enter? (y/n)\n")
    select = input(str(msg), 1)

    if select == 'y':
        height -= 10
        find = search[random.randint(0,1)]

        if find == 'ore':
            block = cave_ore(height)
            print(f"You mine one {block}")
            while z != 3:
                print(".\n")
                time.sleep(.5 / current_pickaxe[4])
                z += 1
            if pickaxe(block) == True:
                if block == 'diamond':
                    achievements_list[1][0] += 1
                input(f"You get 1 {block}!\n", 0)
                store(block, 1)
            else:
                input("Try using a better pickaxe", 0)  
            cls() 
            deep_cave()
        else:
            cls()
            fight_mob(search_mob[random.randint(0,2)])
            deep_cave()

    elif select == 'n':
        cls()
        adventure()

    else:
        cls()
        start()


def a3():
    return ("@@@@@      2018          @@@@@\n")


def deep_cave():

    global height
    global health
    cls()
    health_bar()
    tick(1)
    z = 0
    have_torch = False
    search = ['ore', 'monster']
    search_mob = ['zombie', 'creeper', 'skeleton']
    msg = ''
    msg += ("Would you like to use a torch and go deeper? (y/n)\n")
    select = input(str(msg), 1)


    for i in inventory:
        if i[0] == 'torch' and i[1] > 0:
            have_torch = True

    if select == 'y' and have_torch == True:
        store('torch', -1)
        height -= 10
        find = search[random.randint(0,1)]

        if find == 'ore':
            block = cave_ore(height)
            cls()
            print(f"You mine one {block}")
            while z != 3:
                print(".\n")
                time.sleep(.5 / current_pickaxe[4])
                z += 1
            if pickaxe(block) == True:
                if block == 'diamond':
                    achievements_list[1][0] += 1
                input(f"You get 1 {block}!\n", 0)
                
                store(block, 1)
            else:
                input("Try using a better pickaxe\n", 0)

            cls()   
            deep_cave()
        else:
            cls()
            fight_mob(search_mob[random.randint(0,2)])
            deep_cave()

    elif select == 'y' and have_torch == False:
        cls()
        input("You're out of torches, returning to surface\n", 0)
        height = 64

    elif select == 'n':
        cls()
        input("Returning to surface", 0)
        height = 64

    else:
        input("Learn to hit a key", 0)
        deep_cave()


def break_tree():

    z = 0
    amount = 0
    amount2 = 0
    achievements_list[2][0] += 1

    if random.randint(0,100) < 90:
        print("breaking tree")
        while z != 3:
            print(".")
            time.sleep(2)
            z += 1
        amount = random.randint(4,8)
        store('log', amount)
        msg = ''
        msg += (f"You got {amount} logs!\n")

        if random.randint(0,100) < 10:
            amount2 = random.randint(1,4)
            msg += (f"You got {amount2} apples!\n")
            store('apple', amount2)
        else:
            msg += ("Guess you're going to the doctor today!\n")
        input(msg, 0)

    
    else:
        print("breaking big tree")
        while z != 6:
            print(".")
            time.sleep(2)
            z += 1
        amount = random.randint(10,18)
        store('log', amount)
        msg = ''
        msg += (f"You got {amount} logs!\n")
        if random.randint(0,100) < 10:
            amount2 = random.randint(1,9)
            msg += (f"You got {amount2} apples!\n")
            store('apple', amount2)
        else:
            msg += ("Guess you're going to the doctor today!\n")
        input(msg, 0)

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
    input(f"You run into a {mob}\n", 0)
    fight_mob(mob)


def fight_mob(mob):

    global health
    global friend
    global foe
    cls()
    health_bar()
    select = 0
    wolf = ['wolf']
    

    if (mob) in friend:
        msg = ''
        msg += (f"Would you like to kill the {mob} (y/n)\n")
        select = input(str(msg), 1)
        if select == 'y':
            kill(mob)
        elif select == 'n':
            cls()
            adventure()
        else:
            pass

    elif (mob) in wolf:
        msg = ''
        msg += ("You find a wolf!  Would you like to tame it?(y/n)\n")
        select = input(str(msg), 1)
        if select == 'y':
            cls()
            tame()

        elif select == 'n':
            cls()
            adventure()

        else:
            pass

    else:
        msg = ''
        msg += (f"Fight the {mob} or run (f/r)\n")
        select = input(str(msg), 1)
        if select == 'f':
            cls()
            fight(mob)
        else:
            if mob == 'creeper':
                cls()
                input("Somehow you get away\n", 0)
            else:
                cls()
                health -= 5
                health_bar()
                input(f"You run away and the {mob} hits you for 5 hp\n", 0)
                cls()

# function for killing['chicken', 'pig', 'cow', 'sheep]
def kill(mob):
    msg = ''
    if mob == 'sheep':
        print(f"You kill the {mob}!\n")
        amount = random.randint(0,3)
        amount2 = random.randint(0,3)
        store('wool', amount)
        store('raw_lambchop', amount2)
        msg += (f"You get {amount} wool and {amount2} raw lambchop!\n")
        input(msg ,0)
    
    elif mob == 'chicken':
        print(f"You kill the {mob}!\n")
        amount = random.randint(0,3)
        amount2 = random.randint(0,3)
        store('feathers', amount)
        store('raw_chicken', amount2)
        msg += (f"You get {amount} feathers and {amount2} raw chicken!\n")
        input(msg ,0)
    
    elif mob == 'pig':
        print(f"You kill the {mob}!\n")
        amount = random.randint(0,3)
        store('raw_porkchop', amount)
        msg += (f"You get {amount} raw porkchop!\n")
        input(msg ,0)
    
    elif mob == 'cow':
        achievements_list[4][0] += 1
        print(f"You kill the {mob}!\n")
        amount = random.randint(0,3)
        amount2 = random.randint(0,3)
        store('raw_beef', amount)
        store('leather', amount2)
        msg += (f"You get {amount} raw beef, and {amount2} leather!\n")
        input(msg, 0)
    


def villager():
    

    global prices
    buying_selling = True
    
    item_for_sale = 0
    item_for_buy = 0
    quantity_buy = 0
    quantity_sell = 0
    select = 0
    z = 5
    sell_list = [['log', 1], ['cobble', 2], ['gravel', 2], ['diamond', 20], ['apple', 10]]
    buy_list = prices
    for i in inventory:
        for x in prices:
            if i[0] == x[0]:
                sell_list.append(x)
                if z != 0:
                    sell_list.remove(sell_list[(z - 1)])
                    z -= 1
    # ['leather', 5]
    item_for_sale = sell_list[random.randint(0,(len(sell_list)-1))]
    sell_list.remove(item_for_sale)
    item_for_buy = buy_list[random.randint(0,(len(buy_list)-1))]
    item_for_sale[1] = (item_for_sale[1]/2)

    
    while buying_selling == True:
        global money
        have_item_sell = False
        have_item_buy = False
        cls()
        msg = ''
        msg += ("Villager is...\n")
        msg += (f"Buying - {item_for_sale[0]} for ${item_for_sale[1]}\n")
        msg += (f"Selling - {item_for_buy[0]} for ${item_for_buy[1]}\n")


        
        for i in inventory:
            if i[0] == item_for_sale[0] and i[1] > 0:
                have_item_sell = True
                quantity_sell = i[1]
        if money >= item_for_buy[1]:
            have_item_buy = True
            quantity_buy = math.floor(money/(item_for_buy[1]))


    
        msg += (f"You have ${money}\n")
        msg += (f"Would you like to buy or sell? (b/s) (q to quit)\n")
        select = input(str(msg), 1)

        if select == 's' and have_item_sell:
            msg = ''
            msg += (f"How many {item_for_sale[0]} ${item_for_sale[1]} would you like to sell? (0-{quantity_sell})\n")
            try:
                select = int(input(str(msg), 1))
                if 1 <= select <= quantity_sell:
                    msg = ''
                    msg += (f"Selling {select} {item_for_sale[0]} to Villager\n")

                    store((item_for_sale[0]), -(select))
                    money_added = item_for_sale[1] * select
                    msg += (f"You get ${money_added}\n")
                    money_add(money_added)
                    input(msg, 0)

                elif select > quantity_sell:
                    input("You don't have that many!\n", 0)

                else:
                    input("Invalid", 0)
            except(ValueError, IndexError, TypeError):
                input("Invalid", 0)

        elif select == 'b' and have_item_buy:
            msg = ''
            msg += (f"How many {item_for_buy[0]} would you like to buy? (0-{quantity_buy})\n")
            try:
                select = int(input(str(msg), 1))
                if 1 <= select <= quantity_buy:
                    msg = ''
                    msg += (f"Buying {select} {item_for_buy[0]} to Villager\n")   
                    store((item_for_buy[0]), select)
                    money_added = item_for_buy[1] * -(select)
                    msg += (f"You get {select} {item_for_buy[0]}!\n")
                    money_add(money_added)
                    input(msg, 0)

                elif select > quantity_buy:
                    input("You don't have enough money!\n", 0)
                else:
                    input("Invalid", 0)
            except(ValueError, IndexError,TypeError):
                input("Invalid", 0)

        elif select == 's':
            input(f"You dont have any {item_for_sale[0]}.\n", 0)

        elif select == 'b':
            input(f"You don't have enough money to buy {item_for_buy[0]}.\n", 0)

        elif select == 'q':
            buying_selling = False



def a1():
    return("@@@@@      TEXTCRAFT     @@@@@\n")

# function for fighting ['zombie', 'skeleton','spider', 'witch', 'slime', 'creeper']
def fight(mob):

    global health
    global damage
    
    #    print("What weapon")

    if mob == 'zombie':
        mob_health = 20

        while mob_health > 0:
            cls()
            health_bar()

            if random.randint(0,100) < 25:
                hurt = random.randint(3,10)
                health -= hurt
                input(f"The zombie bites you taking {hurt} hp\n", 0)

            else:
                input("Hit (press any key) to attack!\n", 0)
                if random.randint(0,100) < 90:
                    damage2 = damage * random.randint(1,3)
                    mob_health -= damage2
                    input(f"You hit the {mob} for {damage2} hp\n", 0)
                else:
                    input("You miss", 0)
            # DEATH                    
            if health <= 0:
                dead()
        
        if mob_health <= 0:
            cls()
            msg = ''
            msg += (f"The {mob} has fallen by your fist\n")##### {weapon}
            amount = random.randint(0,3)
            msg += (f"You get {amount} rotten flesh!\n")
            store('rotten_flesh', amount)
            input(str(msg), 0)

   
    elif mob == 'skeleton':
        mob_health = 20

        while mob_health > 0:
            cls()
            health_bar()

            if random.randint(0,100) < 25:
                hurt = random.randint(3,10)
                health -= hurt
                input(f"The skeleton shoots you taking {hurt} hp\n", 0)

            else:
                input("Hit (press any key) to attack!\n", 0)
                if random.randint(0,100) < 90:
                    damage2 = damage * random.randint(1,3)
                    mob_health -= damage2
                    input(f"You hit the {mob} for {damage2} hp\n", 0)
                else:
                    input("You miss", 0)
            # DEATH                    
            if health <= 0:
                dead()
        
        if mob_health <= 0:
            cls()
            msg = ''
            msg += (f"The {mob} has fallen by your fist\n")##### {weapon}
            amount = random.randint(0,3)
            msg += (f"You get {amount} bone!\n")
            store('bone', amount)
            input(str(msg), 0)


    elif mob == 'witch':
        mob_health = 26

        while mob_health > 0:
            cls()
            health_bar()

            if random.randint(0,100) < 25:
                hurt = random.randint(3,10)
                health -= hurt
                input(f"The witch throws a damage potion at you taking {hurt} hp\n", 0)


            if random.randint(0,100) < 10:
                msg = ("The witch heals itself with a potion")
                input(msg, 0)
                mob_health += 10
                if mob_health > 26:
                    mob_health = 26
            else:
                input("Hit (press any key) to attack!\n", 0)
                if random.randint(0,100) < 90:
                    damage2 = damage * random.randint(1,3)
                    mob_health -= damage2
                    input(f"You hit the {mob} for {damage2} hp\n", 0)
                else:
                    input("You miss", 0)
            # DEATH                    
            if health <= 0:
                dead()
        
        if mob_health <= 0:
            cls()
            msg = ''
            msg += (f"The {mob} has fallen by your fist\n")##### {weapon}
            amount = random.randint(0,3)
            msg += (f"You get {amount} glass bottle!\n")
            store('glass_bottle', amount)
            input(str(msg), 0)


    elif mob == 'slime':
        mob_health = 16

        while mob_health > 0:
            cls()
            health_bar()

            if random.randint(0,100) < 25:
                hurt = random.randint(3,10)
                health -= hurt
                input(f"The slime stomps on you taking {hurt} hp\n", 0)

            else:
                input("Hit (press any key) to attack!\n", 0)
                if random.randint(0,100) < 90:
                    damage2 = damage * random.randint(1,3)
                    mob_health -= damage2
                    input(f"You hit the {mob} for {damage2} hp\n", 0)
                else:
                    input("You miss", 0)
            # DEATH                    
            if health <= 0:
                dead()
        
        if mob_health <= 0:
            cls()
            msg = ''
            msg += (f"The {mob} has fallen by your fist\n")##### {weapon}
            amount = random.randint(0,3)
            msg += (f"You get {amount} slimeball!\n")
            store('slimeball', amount)
            input(str(msg), 0)


    elif mob == 'creeper':
        mob_health = 20
        blow_up = False

        while mob_health > 0:
            cls()
            health_bar()

            if random.randint(0,100) < 20:
                hurt = random.randint(40,61)
                health -= hurt
                cls()
                health_bar()
                input(f"The creeper blows up hurting you {hurt} hp\n", 0)
                mob_health = 0
                blow_up = True
            else:
                input("Hit (press any key) to attack!\n", 0)
                if random.randint(0,100) < 90:
                    damage2 = damage * random.randint(1,3)
                    mob_health -= damage2
                    input(f"You hit the {mob} for {damage2} hp\n", 0)
                else:
                    input("You miss", 0)
            # DEATH                    
            if health <= 0:
                dead()
        
        if mob_health <= 0 and blow_up == False:
            cls()
            msg = ''
            msg += (f"The {mob} has fallen by your fist\n")##### {weapon}
            amount = random.randint(0,3)
            msg += (f"You get {amount} gunpowder!\n")
            store('gunpowder', amount)
            input(str(msg), 0)


    if mob == 'spider':
        mob_health = 16

        while mob_health > 0:
            cls()
            health_bar()

            if random.randint(0,100) < 25:
                hurt = random.randint(3,10)
                health -= hurt
                input(f"The spider bites you taking {hurt} hp\n", 0)

            else:
                input("Hit (press any key) to attack!\n", 0)
                if random.randint(0,100) < 90:
                    damage2 = damage * random.randint(1,3)
                    mob_health -= damage2
                    input(f"You hit the {mob} for {damage2} hp\n", 0)
                else:
                    input("You miss", 0)
            # DEATH test  test test                 
            if health <= 0:
                dead()
        
        if mob_health <= 0:
            cls()
            msg = ''
            msg += (f"The {mob} has fallen by your fist\n")##### {weapon}
            amount = random.randint(0,3)
            msg += (f"You get {amount} string!\n")
            store('string', amount)
            input(str(msg), 0)  
        

def dead():
    select = 0
    deaths = 1
    msg = ''
    msg += ("You die, game over.\n")#  Total fatal incidents = {deaths}")

    with open('textcraft123.py', 'w') as file:
        file.write("inventory = []\n")
        file.write("all_farms = []\n")
        file.write("base = [0, 0, 100, 1, 0, 0, ['fist', -1, 0, -1, 1], 'user_id']\n")
        file.write("achieved = []\n")
        file.write("equipment = []\n")
        file.write("achievements_list = []\n")
        

    msg += ("Play again (y/n)\n")
    
    while True:
        select = input(msg)
        if select == 'n':
            exit(0)
        elif select == 'y':
            deaths += 1
        else:
            pass
        


def view_inventory():

    k = 0
    m = 1
    select = 0
    is_sure = False
    selected_item = 0
    achievements_list[9][0] += 1
    msg = ''
    msg += ("Items\n")
    for i in inventory:
        if i[1] == 0:
            inventory.remove(i)
    
    for i in inventory:
        #MAX len 21
        text = (f"  {i[1]}-{i[0]}")
        var1 = 20 - len(text)
        msg += str(text + ' ' * var1)
        
        k += 1
        m += 1
        if k == 3:
            msg += ("\n")
            k = 0
    msg += ("\n")
    msg += ("Equipment\n")

    msg += number_list(equipment, 0)


    msg += ("Throw out an item or equipment? (i/e)\n")
    select = input(str(msg), 1)

    if select == 'i':
        msg += number_list(inventory, 0)

        msg += ("Select an item to destroy\n")
        try:
            select = int(input(str(msg), 1))
            msg += ("Are you sure? (y/n)\n")
            is_sure = input(str(msg), 1)
            if is_sure:
                store(inventory[(select-1)][0], -(inventory[(select-1)][1]))


        except(ValueError, TypeError, IndexError):
            input("Invalid", 0)


    elif select == 'e':
        msg += number_list(equipment, 0)

        msg += ("Select an item to destroy\n")
        try:
            select = int(input(str(msg), 1))
            select_item = equipment[(select-1)][0]
            msg += ("Are you sure? (y/n)\n")
            is_sure = input(str(msg), 1)
            if is_sure:
                store(select, -(inventory[(select-1)]))

        except(ValueError, TypeError, IndexError):
            input("Invalid", 0)



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
    msg = ''

    if len(current_pickaxe) > 1:
        percentage2 = math.ceil( 100* (current_pickaxe[1]) / current_pickaxe[3])
        msg += (f"Current - {current_pickaxe[0]} {percentage2}%\n")

    
    #[['wooden_pickaxe', 4, 1, 59], []]

    if len(equipment) > 0:
        
        for i in equipment:
            if i != None and len(equipment[0]) > 0:
                if i[1] != 0:
                    percentage1 = math.ceil( 100* (i[1]) / i[3])
                    msg += str(f"#{y} {i[0]} {percentage1}% ")
                    z += 1
                    if z == 2:
                        msg += ("\n")
                        z = 0
                    y += 1

        msg += ("\n")
        msg += ("Equip a #?\n")
        try:
            select = input(str(msg), 1)
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
                    input(f"{x[0]} equipped!\n", 0)

        except (TypeError, ValueError, IndexError):
            input("(Exit)\n", 0)

        


    else:
        msg += ("You don't have any equipment\n")
        input(msg, 0)


def health_bar():

    global health
    return ('  Health('+ (int(health/10)*2)*'@'+ ((-(int(health/10)-10))*2)*'-' + ')\n')

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
        msg = ''
        msg += ("Use bone? (y/n)\n")
        select = input(str(msg), 1)

        if select == 'y':
            store('bone', -1)
            if random.randint(0,100) < 20:
                achievements_list[7][0] += 1
                input("Tame successful, your damage increases by 1\n", 0)
                damage += 1
            else:
                input("Tame unsuccessful\n", 0)
                tame()
        else:
            pass

    else:
        input("Sorry you don't have anymore bones\n", 0)



def bed_sleep():

    global night
    have_bed = False

    for i in inventory:
        if i[0] == 'bed':
            have_bed = True

    if have_bed == False and night == False:
        input("You can't sleep on the ground, silly\n", 0)

    elif night == False:
        input("No naps allowed, sleep at night...\n", 0)


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
        input("Try crafting a furnace first", 0)

    else:
        if can_cook == True and have_fuel == True:
            try:
                k = 1
                msg += ("What would you like to cook?\n")
                msg += number_list(cook_list, -1)

                msg += ("\n")
                select_unit = int(input(str(msg), 1))
                select_unit = cook_list[(select_unit - 1)]
            except(ValueError, IndexError, TypeError):
                pass
            if select_unit in cook_list:
                try:
                    k = 1
                    msg = ''
                    msg += (f"What fuel would you like to use to cook your {select_unit}?\n")
                    msg += number_list(fuel_list, -1)

                    msg += ("\n")
                    select_fuel = int(input(str(msg), 1))
                    select_fuel = fuel_list[(select_fuel - 1)]
                except(ValueError, IndexError, TypeError):
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
                        msg = ''
                        msg += (f"How many {select_unit} would you like to cook? You have {quantity_unit}\n")
                        msg += (f"and {select_fuel} only cooks {quantity_fuel}\n")
                        select = input(str(msg), 1)

                        try:
                            if int(select) <= quantity_fuel:
                                quantity_unit = int(select)####
                                if int(quantity_unit) > int(quantity_fuel):
                                    total_cooked = int(quantity_fuel)
                                else:
                                    total_cooked = int(quantity_unit)
                                print("Cooking")
                                while p != 3:
                                    print(".\n")
                                    time.sleep(1 * total_cooked)
                                    p += 1

                                for i in cook_output:
                                    if select_unit == i[0]:
                                        select_unit2 = i[1]
                                msg = ''
                                msg += (f"You cook {total_cooked} {select_unit} with your {select_fuel}\n")
                                msg += (f"Giving you {total_cooked} {select_unit2}\n")
                                store(select_unit2, total_cooked)
                                store(select_fuel, -1)
                                store(select_unit, -total_cooked)
                                input(msg, 0)


                                ape = 'q'

                            elif int(select) > quantity_unit:
                                input("You don't have that many dummy!\n", 0)

                            elif int(select) > quantity_fuel:
                                input("Your fuel won't last that long\n", 0)

                        
                            else:
                                ape = 'q'

                        except ValueError:
                            ape = 'q'



        else:
            msg = ''
            msg += ("Cooks you can't\n")
            if can_cook == True:
                msg += ("No fuel!\n")
                input(msg, 0)
            else:
                msg += ("You have nothing to cook!\n")
                input(msg, 0)


# tick(0) checks the clock
# tick(x) checks clock and moves time forward by x
def tick(x):

    global clock
    if x == 0:
        if clock < 100:
            return ("  Birds are singing in the sunlight...\n")
        else:
            return ("  Crickets are chirping in the moonlight...\n")

    # For sleeping
    elif x == 100:
        night = False
        msg = ''
        msg += ("=========================\n")
        msg += ("=========================\n")
        msg += ("The sun has RISEN!\n")
        msg += ("=========================\n")
        msg += ("=========================\n")
        input(msg, 0)
        clock = 0

    else:
        clock += x
        if clock == 100:
            night = True
            msg = ''
            msg += ("=========================\n")
            msg += ("=========================\n")
            msg += ("The sun has FALLEN!\n")
            msg += ("=========================\n")
            msg += ("=========================\n")
            return msg
        if clock == 200:
            night = False
            msg = ''
            msg += ("=========================\n")
            msg += ("=========================\n")
            msg += ("The sun has RISEN!\n")
            msg += ("=========================\n")
            msg += ("=========================\n")
            clock = 0
            return msg

# x is the list to print. y is the list indice(-1 for no indice) diamond_pickaxe
def number_list(x,y):
    m = 1
    k = 0
    var1 = 0
    text = 0
    done = False
    msg = ''
    if y != -1:

        for i in x:
            
            #MAX len 21
            text = (f"  #{m} {i[y]}")
            var1 = 21 - len(text)
            msg += (text + ' ' * var1)
            k += 1
            m += 1
            if k == 3:
                msg += ("\n")
                k = 0
        return msg
    else:

        for i in x:
            
            #MAX len 20
            text = (f" #{m} {i}")
            var1 = 20 - len(text)
            msg += str(text + ' ' * var1)
            k += 1
            m += 1
            if k == 3:
                msg += ("\n")
                k = 0
        return msg


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
    (m)enu\n""")

    
    cls()
    
    # Checking time
    tick(0)
    # Checking for new achievements
    achievements(1)
    health_bar()
    print(f"  In the bank = ${money}")
    # Checking for farm events

    
    select = input([tick(0), achievements(1), health_bar(),f"  In the bank = ${money}\n",
EventFarm(0, all_farms), question], 1)

    #select = input(ms, 1g)
    msg = ''
    
    if select == 'a':# adventure()
        cls()
        adventure()

    elif select == 'd':# dig_down()
        cls()
        dig_down(height)

    elif select == 'c':# craft
        cls()
        craft()
    
    elif select == 'f':# furnace
        cls()
        furnace()
    
    elif select == 'e':# eat
        cls()
        eat()
    
    elif select == 's':# sleep
        cls()
        bed_sleep()
    
    elif select == 'm':# menu
        cls()
        menu()
    
    else:
        cls()
        print("Try again")


def version(x):
    global test
    msg = ''
    msg += a4()
    msg += (f"     v.{x}\n")
    input(msg, 0)
    if x == 'test':
        test = True
    else:
        pass



version('test')
version('pre-alpha 3.0')

if user_id != 'user_id':
    msg = (f"Welcome back, {user_id}")
    input(msg, 0)
    start()

while True:
    if test:
        start()
    else:
        try:
            if user_id == 'user_id':

                select = 0
                id = ''
                msg = ("Pick a user id (Press (.)PERIOD when done)\n > ")
                while select != '.':
                    select = input(msg, 1)
                    id += select
                    msg += select
                for x in id:
                    x.replace(".", "")
                user_id = id
                msg = (f"Welcome {user_id}!")
                input(msg, 0)
                start()

            else:
                start()
        except Exception:
            input("This is broken lol Error### bleehgfajfasaofowaowo.   wkkd        .\n", 0)


    






