import random
import time
import os
import math
import sys


if True:

    def a4():
        msg = (a1()+a2()+a3())
        return msg

    def a3():
        return ("@@@@@      2018          @@@@@\n")

    def a1():
        return("@@@@@      TEXTCRAFT     @@@@@\n")

    def a2():
        return ("@@@@@      Skelouse      @@@@@\n")
# Bugs

    # future error, lol  burning enchanted wooden tools, won't be able to select which wood tool to burn

    # dying breaks achievement list

# Defines cls() to clear the screen of prints
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


#IMPORTING CURSES OR UNICURSES
if True:
    try:

        import curses
        #--------------------------------------
        def input_char(message,y):
            win = curses.initscr()
            win.clear()
            msg1 = None
            if y == 1:
                msg1 = ''
                for i in message:
                    msg1 += str(i)
                win.addstr(0, 0, msg1)
                while True: 
                    ch = win.getch()
                    if ch in range(32, 127): break
                    if ch == 10: break
                    time.sleep(0.05)
                curses.endwin()
                return chr(ch)
            elif y == 0:
                msg1 = message
                cls()
                msg1 += ("\n\n(press any key)\n")
                win.addstr(0, 0, msg1)
                while True: 
                    ch = win.getch()
                    if ch in range(32, 127): break
                    if ch == 10: break
                    time.sleep(0.05)
                curses.endwin()
                return chr(ch)

            else:
                x = 0
                iterations = y[0]# number of iterations
                z = y[1]
                
                msg1 = message

                msg1 += '.'
                win.addstr(0, 0, msg1)
                try:
                    time.sleep(y[2])
                except:
                    pass
                    
                curses.endwin()
                iterations -= 1
                if iterations != -1:
                    input(msg1, [iterations, z, z])
                else:
                    pass

                        
                    

    except:
        import unicurses
        #--------------------------------------
        def input_char(message,y):
            #try:
            msg1 = None
            if y == 1:
                stdscr = unicurses.initscr()
                unicurses.clear()
                msg1 = ''
                for i in message:
                    msg1 += str(i)
                unicurses.addstr(msg1, 0)
                while True: 
                    ch = unicurses.getch()
                    if ch in range(32, 127): break
                    if ch == 10: break
                    time.sleep(0.05)
                unicurses.endwin()
                return chr(ch)
            elif y == 0:
                stdscr = unicurses.initscr()
                unicurses.clear()
                msg1 = message
                msg1 += ("\n\n(press any key)\n")
                unicurses.addstr(msg1, 0)
                while True: 
                    ch = unicurses.getch()
                    if ch in range(32, 127): break
                    if ch == 10: break
                    time.sleep(0.05)
                unicurses.endwin()
                return chr(ch)
            else:
                stdscr = unicurses.initscr()        
                unicurses.clear()
                x = 0
                iterations = y[0]# number of iterations
                z = y[1]# sleep time
                
                msg1 = message

                unicurses.addstr(msg1, 0)
                while True:
                    unicurses.refresh()
                    time.sleep(z)
                    break
                unicurses.endwin()
                
                while iterations != 0:
                    msg1 += '.'
                    stdscr = unicurses.initscr()        
                    
                    iterations -= 1
                    
                    unicurses.addstr(msg1, 0)
                    while True:
                        unicurses.refresh()
                        time.sleep(z)
                        break
                    unicurses.endwin()
                    
                    
                


        #--------------------------------------


# Redefined input function to send into curses
def input(x,y):
    # y/0 pause to show a message
    # y/1 return the character pressed
    # y[msg, [iterations, sleep time]] adds '.' iterations times, after sleep time
    c = input_char(x,y)
    try:
        return int(c)
    except:
        return c


# Checks if testing or not, prints on start screen
test = False
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


# Importing save file 'textcraft123'
if True:
    try:
        import textcraft123
    except ModuleNotFoundError:
        achievements_list = [
        # [variable ,Don't have have 0 or 1 ,goal , "achievement",reason for achievement]
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


        with open('textcraft123.py', 'w') as file:
            file.write("inventory = []\n")
            file.write("all_farms = []\n")
            file.write("base = [0, 0, 100, 0, 0, 0, ['fist', -1, 0, -1, .5], 'user_id']\n")
            file.write("equipment = []\n")
            file.write("achievements_list =  ")
            file.write(str(achievements_list))
            print("Please hold...")
            time.sleep(2)

    import textcraft123
    global inventory
    global all_farms
    global base
    global equipment

    inventory = textcraft123.inventory
    all_farms = textcraft123.all_farms
    base = textcraft123.base
    equipment = textcraft123.equipment
    achievements_list = textcraft123.achievements_list

    test = False

    night = base[0]
    furnace_have = base[1]
    health = base[2]
    wolves = base[3]
    clock = base[4]
    money = base[5]
    current_pickaxe = base[6]
    user_id = base[7]


    try:
        current_shovel = base[8]
    except IndexError:
        current_shovel = ['fist', -1, 0, -1, .5]

    try:
        current_axe = base[9]
    except IndexError:
        current_axe = ['fist', -1, 0, -1, .5]

    try:
        current_helmet = base[10]
    except IndexError:
        current_helmet = ['skin', -1, 0, -1, 1]

    try:
        current_chestplate = base[11]
    except IndexError:
        current_chestplate = ['skin', -1, 0, -1, 1]

    try:
        current_leggings = base[12]
    except IndexError:
        current_leggings = ['skin', -1, 0, -1, 1]

    try:
        current_boots = base[13]
    except IndexError:
        current_boots = ['skin', -1, 0, -1, 1]

    try:
        current_sword = base[14]
    except IndexError:
        current_sword = ['fist', -1, 0, -1, .5]

    height = 64
    try:
        current_time = base[15]
    except IndexError:
        current_time = math.floor(time.time())

    try:
        furnace_level = base[16]
    except IndexError:
        furnace_level = 1


# TOOLS LISTS
if True:
    #type, current durability, power, total durability
    # type, current durability, defense, total durability
    tools = [
        ['gold_pickaxe', 32, 2, 32, 4], ['wooden_pickaxe', 59, 1, 59, 1], ['stone_pickaxe', 131, 2, 131, 2],
        ['iron_pickaxe', 250, 3, 250, 3], ['diamond_pickaxe', 1561, 4, 1561, 4],
        ['gold_axe', 32, 2, 32, 4], ['wooden_axe', 59, 1, 59, 1], ['stone_axe', 131, 2, 131, 2],
        ['iron_axe', 250, 3, 250, 3], ['diamond_axe', 1561, 4, 1561, 4],
        ['gold_shovel', 32, 2, 32, 4], ['wooden_shovel', 59, 1, 59, 1], ['stone_shovel', 131, 2, 131, 2],
        ['iron_shovel', 250, 3, 250, 3], ['diamond_shovel', 1561, 4, 1561, 4],
        ['gold_sword', 32, 2, 32, 3], ['wooden_sword', 59, 1, 59, 1], ['stone_sword', 131, 2, 131, 2],
        ['iron_sword', 250, 3, 250, 3], ['diamond_sword', 1561, 4, 1561, 4],
        ['log_helmet', 56, 2, 56, 2], ['log_chestplate', 81, 1, 81, 2],
        ['log_leggings', 76, 2, 76, 2],['log_boots', 66, 4, 66, 2],
        ['iron_helmet', 166, 2, 166, 3], ['iron_chestplate', 241, 1, 241, 3],
        ['iron_leggings', 226, 2, 226, 3],['iron_boots', 196, 4, 196, 3],
        ['gold_helmet', 78, 2, 78, 3], ['gold_chestplate', 113, 1, 113, 3],
        ['gold_leggings', 106, 2, 106, 3],['gold_boots', 92, 4, 92, 3],
        ['diamond_helmet', 364, 2, 364, 4], ['diamond_chestplate', 529, 1, 529, 4],
        ['diamond_leggings', 496, 2, 496, 4],['diamond_boots', 430, 4, 430, 4],
        ['bedrock_helmet', 921, 2, 921, 5], ['bedrock_chestplate', 1338, 1, 1338, 5],
        ['bedrock_leggings', 1254, 2, 1254, 5],['bedrock_boots', 1087, 4, 1087, 5],
        ['lapis_helmet', 56, 2, 56, 1], ['lapis_chestplate', 81, 1, 81, 1],
        ['lapis_leggings', 76, 2, 76, 1],['lapis_boots', 66, 4, 66, 1]
    ]

    picks = ['gold_pickaxe', 'wooden_pickaxe', 'stone_pickaxe', 'iron_pickaxe', 'diamond_pickaxe']

    shovels = ['gold_shovel', 'wooden_shovel', 'stone_shovel', 'iron_shovel', 'diamond_shovel']

    axes = ['gold_axe', 'wooden_axe', 'stone_axe', 'iron_axe', 'diamond_axe']

    swords = ['gold_sword', 'wooden_sword', 'stone_sword', 'iron_sword', 'diamond_sword']

    helmets = ['log_helmet', 'iron_helmet', 'gold_helmet', 'diamond_helmet',
    'bedrock_helmet', 'lapis_helmet']

    chestplates = ['log_chestplate', 'iron_chestplate', 'gold_chestplate', 'diamond_chestplate',
    'bedrock_chestplate', 'lapis_chestplate']

    leggings = ['log_leggings', 'iron_leggings', 'gold_leggings', 'diamond_leggings',
    'bedrock_leggings', 'lapis_leggings']

    boots = ['log_boots', 'iron_boots', 'gold_boots', 'diamond_boots',
    'bedrock_boots', 'lapis_boots']


# ADVENTURE LISTS
if True:
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
        'witch', 'slime', 'creeper', 'spider',
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


    prices = [
        ['log', 1], ['cobble', 2], ['gravel', 2], ['diamond', 20], ['apple', 10],
        ['iron', 5], ['leather', 5], ['redstone', 5], ['obsidian', 20], ['stone', 3],
        ['bedrock', 340]
    ]


class adventure():

    
    # Defines what you find on an adventure
    def adv():
        tick(1)
        search = ['tree','tree', 'tree', 'tree',
                'tree', 'tree', 'river', 'animal', 'animal', 'cave']
        if adventure.lapis_armor():
            if random.randint(0,100) < 80:
                search.append('villager')
        else:
            if random.randint(0,100) < 25:
                search.append('villager')

        end = search[random.randint(0, (len(search)-1))]

        if end == 'animal':
            cls()
            adventure.mob()

        elif end == 'tree':
            msg = ''
            msg += ("You find a tree\n")
            msg += ("Do you want to cut it down(y/n)\n")
            select = input(str(msg), 1)
            if select == 'y':
                cls()
                adventure.break_tree()
            elif select == 'n':
                cls()
                adventure.adv()
            else:
                pass

        elif end == 'river':
            cls()
            adventure.river()

        elif end == 'cave':
            cls()
            adventure.cave()

        elif end == 'villager':
            cls()
            adventure.villager()
        
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
            if i[0] == 'bucket' and i[1] > 0:
                if i[0] != 'water_bucket':
                    bucket = True

        if bucket == True and rod == True:
            msg += ("Would you like to fish or fill your bucket with water?(f/b)\n")
            select = input(str(msg), 1)
            if select == 'f':
                cls()
                adventure.fish()
            elif select == 'b':
                cls()
                adventure.fill_bucket()
            else:
                pass

        elif bucket == True:
            msg += ("would you like to fill a bucket with water?(y/n)\n")
            select = input(str(msg), 1)
            if select == 'y':
                cls()
                adventure.fill_bucket()

        elif rod == True:
            msg += ("would you like to fish?(y/n)\n")
            select = input(str(msg), 1)
            if select == 'y':
                cls()
                adventure.fish()

        else:
            msg += ("Sorry there's nothing for you here.\n")
            msg += ("Keep adventuring?(y/n)\n")
            select = input(str(msg), 1)
            if select == 'y':
                cls()
                adventure.adv()
            else:
                pass


    def fill_bucket():

        tick(1)
        bucket = True

        while bucket == True:
            z = 0
            cls()
            input("Your bucket fills up", [2, .5])
            achievements_list[5][0] += 1
            
            
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
            adventure.fish()
        else:
            pass


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


    def cave():
        global current_pickaxe
        tick(1)
        global height
        z = 0
        search = ['ore', 'monster']
        search_mob = ['zombie', 'creeper', 'skeleton']
        msg = ''
        msg += health_bar()
        msg += ("You peer into the entrance of a cave.\n")
        msg += ("Will you dare enter? (y/n)\n")
        select = input(str(msg), 1)

        if select == 'y':
            height -= 10
            find = search[random.randint(0,1)]

            if find == 'ore':
                block = adventure.cave_ore(height)
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
                adventure.deep_cave()
            else:
                cls()
                adventure.fight_mob(search_mob[random.randint(0,2)])
                adventure.deep_cave()

        elif select == 'n':
            cls()
            adventure.adv()

        else:
            cls()
            start()


    def deep_cave():

        global height
        global health
        global current_pickaxe
        cls()
        health_bar()
        tick(1)
        z = 0
        have_torch = False
        search = ['ore', 'monster']
        search_mob = ['zombie', 'creeper', 'skeleton']
        msg = ''
        msg += health_bar()
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
                block = adventure.cave_ore(height)
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
                adventure.deep_cave()
            else:
                cls()
                adventure.fight_mob(search_mob[random.randint(0,2)])
                adventure.deep_cave()

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
            adventure.deep_cave()


    def break_tree():
        global current_axe
        msg = ''
        z = 0
        amount = 0 # logs
        amount2 = 0 # apples
        amount3 = 0
        achievements_list[2][0] += 1

        amount = random.randint(4, 10)
        amount2 = random.randint(1, 4)
        if random.randint(0,100) > 90 and current_axe[0] != 'fist':
            msg += '    BIG TREE!!!!\n'
            amount = random.randint(12, 24)
            amount2 = random.randint(2, 9)
        amount3 = amount
        while amount3 > 0:
            msg += ("breaking log")
            input(msg, [3, float(.5/current_axe[4])])
            amount3 -= 1
            msg = ''

            if current_axe[1] > 0 and current_axe[0] != 'fist':
                current_axe[1] -= 1

            if current_axe[1] == 0:
                input("Your axe has broken...\n", 0)
                current_axe = ['fist', -1, 0, -1, .5]

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
        adventure.fight_mob(mob)


    def villager():
    
        global prices
        buying_selling = True
        
        item_for_sale = 0
        item_for_buy = 0
        quantity_buy = 0
        quantity_sell = 0
        select = 0
        z = 5
        sell_list = [['log', 1], ['cobblestone', 2], ['gravel', 2], ['diamond', 20], ['apple', 10]]
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
                msg += (f"How many {item_for_sale[0]} ${item_for_sale[1]} would you like to sell?\n")

                select = two_digit_select(msg, quantity_sell)
                try:
                    if 1 <= select <= quantity_sell:
                        msg = ''
                        msg += (f"Selling {select} {item_for_sale[0]} to Villager\n")

                        store((item_for_sale[0]), -(select))
                        money_added = item_for_sale[1] * select
                        msg += (f"You get ${money_added}\n")
                        money_add(money_added)
                        input(msg, 0)
                except TypeError:
                    pass


            elif select == 'b' and have_item_buy:
                msg = ''
                msg += (f"How many {item_for_buy[0]} would you like to buy?\n")

                try:
                    select = two_digit_select(msg, quantity_buy)
                    if 1 <= select <= quantity_buy:
                        msg = ''
                        msg += str(f"Buying {select} {item_for_buy[0]} from Villager for ${(item_for_buy[1] * (select))}\n")   
                        store((item_for_buy[0]), select)
                        money_added = item_for_buy[1] * -(select)
                        msg += (f"You get {select} {item_for_buy[0]}!\n")
                        money_add(money_added)
                        input(msg, 0)

                except TypeError:
                    pass

            elif select == 's':
                input(f"You dont have any {item_for_sale[0]}.\n", 0)

            elif select == 'b':
                input(f"You don't have enough money to buy {item_for_buy[0]}.\n", 0)

            elif select == 'q':
                buying_selling = False


    def fight_mob(mob):

        global health
        global friend
        global foe
        cls()
        
        select = 0
        wolf = ['wolf']
        msg = ''

        msg += (f"You run into a {mob}\n")

        if (mob) in friend:
            msg += (f"Would you like to kill the {mob} (y/n)\n")
            select = input(str(msg), 1)
            if select == 'y':
                adventure.kill(mob)
            elif select == 'n':
                cls()
                adventure.adv()
            else:
                pass

        elif (mob) in wolf:
            msg += ("You find a wolf!  Would you like to tame it?(y/n)\n")
            select = input(str(msg), 1)
            if select == 'y':
                cls()
                adventure.tame()

            elif select == 'n':
                cls()
                adventure.adv()

            else:
                pass

        else:
            msg = ''
            msg += health_bar()
            msg += (f"Fight the {mob} or run (f/r)\n")
            select = input(str(msg), 1)
            if select == 'f':
                cls()
                adventure.fight(mob)
            else:
                if mob == 'creeper':
                    cls()
                    input("Somehow you get away\n", 0)
                else:
                    cls()
                    health -= 5
                    msg = ''
                    msg += health_bar()
                    msg += str(f"You run away and the {mob} hits you for 5 hp\n")
                    input(msg, 0)
                    # DEATH                    
                    if health <= 0:
                        adventure.dead()

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

    # function for fighting ['zombie', 'skeleton','spider', 'witch', 'slime', 'creeper']
    def fight(mob):

        global health
        msg = ''
        msg += health_bar()
        
        #    print("What weapon")

        if mob == 'zombie':
            mob_health = 20

            while mob_health > 0:
                cls()
                health_bar()
                
                if random.randint(0,100) < 25:
                    hurt = random.randint(3,10)
                    hurt = defense(hurt)
                    health -= hurt
                    msg = ''
                    msg += health_bar()
                    msg += str(f"The zombie bites you!\n")

                else:
                    
                    if random.randint(0,100) < 90:
                        damage2 = damage()
                        mob_health -= damage2
                        msg += (f"You hit the {mob} for {damage2} hp\n")
                        msg += str("Attack mob!\n")
                        input(msg, 0)
                        msg = ''
                        msg += health_bar()
                    else:
                        msg += ("You miss\n")
                        msg += str("Attack mob!\n")
                        input(msg, 0)
                        msg = ''
                        msg += health_bar()
                # DEATH                    
                if health <= 0:
                    adventure.dead()
            
            if mob_health <= 0:
                cls()
                msg = ''
                msg += health_bar()
                msg += str(f"The {mob} has fallen by your fist\n")##### {weapon}
                amount = random.randint(0,3)
                msg += (f"You get {amount} rotten flesh!\n")
                store('rotten_flesh', amount)
                input(str(msg), 0)

    
        elif mob == 'skeleton':
            mob_health = 20

            while mob_health > 0:

                if random.randint(0,100) < 25:
                    hurt = random.randint(3,10)
                    hurt = defense(hurt)
                    health -= hurt
                    msg = ''
                    msg += health_bar()
                    msg += (f"The skeleton shoots you!\n")

                else:
                    if random.randint(0,100) < 90:
                        damage2 = damage()
                        mob_health -= damage2
                        msg += (f"You hit the {mob} for {damage2} hp\n")
                        msg += str("Attack mob!\n")
                        input(msg, 0)
                        msg = ''
                        msg += health_bar()
                    else:
                        msg += ("You miss\n")
                        msg += str("Attack mob!\n")
                        input(msg, 0)
                        msg = ''
                        msg += health_bar()
                # DEATH                    
                if health <= 0:
                    adventure.dead()
            
            if mob_health <= 0:
                cls()
                msg = ''
                msg += health_bar()
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
                    msg = ''
                    msg += health_bar()
                    msg += (f"The witch throws a damage potion at you!\n")


                elif random.randint(0,100) < 10:
                    msg += ("The witch heals itself with a potion")
                    mob_health += 10
                    if mob_health > 26:
                        mob_health = 26

                else:
                    if random.randint(0,100) < 90:
                        damage2 = damage()
                        mob_health -= damage2
                        msg += (f"You hit the {mob} for {damage2} hp\n")
                        msg += str("Attack mob!\n")
                        input(msg, 0)
                        msg = ''
                        msg += health_bar()
                    else:
                        msg += ("You miss\n")
                        msg += str("Attack mob!\n")
                        input(msg, 0)
                        msg = ''
                        msg += health_bar()
                # DEATH                    
                if health <= 0:
                    adventure.dead()
            
            if mob_health <= 0:
                cls()
                msg = ''
                msg += health_bar()
                msg += (f"The {mob} has fallen by your fist\n")##### {weapon}
                amount = random.randint(0,3)
                msg += (f"You get {amount} glass bottle!\n")
                store('glass_bottle', amount)
                input(str(msg), 0)


        elif mob == 'slime':
            mob_health = 16

            while mob_health > 0:

                if random.randint(0,100) < 25:
                    hurt = random.randint(3,10)
                    hurt = defense(hurt)
                    health -= hurt
                    msg = ''
                    msg += health_bar()
                    msg += (f"The slime stomps on you!\n")

                else:
                    if random.randint(0,100) < 90:
                        damage2 = damage()
                        mob_health -= damage2
                        msg += (f"You hit the {mob} for {damage2} hp\n")
                        msg += str("Attack mob!\n")
                        input(msg, 0)
                        msg = ''
                        msg += health_bar()
                    else:
                        msg += ("You miss\n")
                        msg += str("Attack mob!\n")
                        input(msg, 0)
                        msg = ''
                        msg += health_bar()
                # DEATH                    
                if health <= 0:
                    adventure.dead()
            
            if mob_health <= 0:
                cls()
                msg = ''
                msg += health_bar()
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
                    hurt = random.randint(60,90)
                    hurt = defense(hurt)
                    health -= hurt
                    msg = ''
                    msg += health_bar()
                    msg += (f"The creeper blows up!\n")
                    input(msg, 0)
                    mob_health = 0
                    blow_up = True
                else:

                    if random.randint(0,100) < 90:
                        damage2 = damage()
                        mob_health -= damage2
                        msg += (f"You hit the {mob} for {damage2} hp\n")
                        msg += str("Attack mob!\n")
                        input(msg, 0)
                        msg = ''
                        msg += health_bar()
                    else:
                        msg += ("You miss\n")
                        msg += str("Attack mob!\n")
                        input(msg, 0)
                        msg = ''
                        msg += health_bar()
                # DEATH                    
                if health <= 0:
                    adventure.dead()
            
            if mob_health <= 0 and blow_up == False:
                cls()
                msg = ''
                msg += health_bar()
                msg += (f"The {mob} has fallen by your fist\n")##### {weapon}
                amount = random.randint(0,3)
                msg += (f"You get {amount} gunpowder!\n")
                store('gunpowder', amount)
                input(str(msg), 0)


        if mob == 'spider':
            mob_health = 16

            while mob_health > 0:

                if random.randint(0,100) < 25:
                    hurt = random.randint(3,10)
                    hurt = defense(hurt)
                    health -= hurt
                    msg = ''
                    msg += health_bar()
                    msg += (f"The spider bites you!\n")

                else:
                    if random.randint(0,100) < 90:
                        damage2 = damage()
                        mob_health -= damage2
                        msg += (f"You hit the {mob} for {damage2} hp\n")
                        msg += str("Attack mob!\n")
                        input(msg, 0)
                        msg = ''
                        msg += health_bar()
                    else:
                        msg += ("You miss\n")
                        msg += str("Attack mob!\n")
                        input(msg, 0)
                        msg = ''
                        msg += health_bar()
              
                if health <= 0:
                    adventure.dead()
            
            if mob_health <= 0:
                cls()
                msg = ''
                msg += health_bar()
                msg += (f"The {mob} has fallen by your fist\n")##### {weapon}
                amount = random.randint(0,3)
                msg += (f"You get {amount} string!\n")
                store('string', amount)
                input(str(msg), 0)  


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
                    wolves += 1
                else:
                    input("Tame unsuccessful\n", 0)
                    adventure.tame()
            else:
                pass

        else:
            input("Sorry you don't have anymore bones\n", 0)


    def dead():
        select = 0
        deaths = 1
        msg = ''
        msg += ("You die, game over.\n")#  Total fatal incidents = {deaths}")

        with open('textcraft123.py', 'w') as file:
            file.write("inventory = []\n")
            file.write("all_farms = []\n")
            file.write("base = [0, 0, 100, 1, 0, 0, ['fist', -1, 0, -1, .5], 'user_id']\n")
            file.write("equipment = []\n")
            file.write("achievements_list = []\n")
            

        input(msg, 0)
        sys.exit()


    def lapis_armor():
        
        global current_helmet
        global current_chestplate
        global current_leggings
        global current_boots

        if ('lapis' in current_helmet[0] and 'lapis' in current_chestplate[0]
            and 'lapis' in current_leggings[0] and 'lapis' in current_boots[0]):
            return True


# FARM LISTS
if True:
    farm_materials = [
    ['log', 50000],
    ['stone', 20000],
    ['iron_block', 5000],
    ['gold_block', 3500],
    ['diamond_block', 2000],
    ['obsidian', 10],
    ['bedrock', 3]
    ]


class farm():
    
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

                if have_farm:   
                    #if farm_selected:
                    #    farm.EventFarm(0, selected_farm)  # 1 is check for things that need to be done 
                    #else:
                    #    pass

                    if selected_farm:
                        need_msg = (f"   level-{selected_farm[8]} {selected_farm[0]}|{selected_farm[10]} farm is selected!\n")
                        need_msg += (farm.EventFarm(1, selected_farm))  
                    msg = need_msg + ("""What would you like to do?
        (s)elect a farm
        (w)ater
        (h)arvest
        (l)evel up
        (n)otifications
        (b)uild new farm
        (d)estroy
        (q)uit\n""")# add are you sure on destroy

                    select = input(msg, 1)
                    try:
                        if select == 'n': # Notifications
                            cls()
                            msg = ''
                            msg += farm.EventFarm(0, all_farms)
                            input(msg, 0)

                        elif select == 's': # Select a farm
                            msg = ''
                            for i in current_farms:
                                msg += (f"#{x} level-{i[8]} {i[0]}|{i[10]}\n")
                                x += 1
                            try:
                                select = int(input(msg, 1))
                                if select:
                                    selected_farm = current_farms[(select-1)]
                                    farm_selected == True

                            except (ValueError, IndexError, TypeError):
                                msg = ''
                                msg += ("Invalid selection\n")
                                input(msg, 0)


                        elif select == 'w' and selected_farm != 0: # Water selected
                            farm.EventFarm(2, selected_farm)

                        elif select == 'h' and selected_farm != 0: # Harvest selected
                            farm.EventFarm(3, selected_farm)

                        elif select == 'l' and selected_farm != 0: # level selected
                            farm.EventFarm(5, selected_farm)

                        elif select == 'd' and selected_farm != 0: # Destroy
                            msg = ''
                            msg += ("Are you sure you want to destroy this farm? (y/n)\n")
                            select = input(msg, 1)
                            if select == 'y':
                                farm.EventFarm(6, selected_farm)
                                select = 'q'
                        
                        elif select == 'b':# build farm
                            farm.build_farm()
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
                    msg += ("You don't have any farms\n")
                    msg += ("Build one? (y/n)\n")
                    msg += "> "
                    select = input(str(msg), 1)

                    if select == 'y':
                        farm.build_farm()
                        select = 'q'
                    else:
                        select = 'q'

            except ZeroDivisionError:
                print("Lol")

    #DONE
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
                msg += ("       Needs to be watered.\n")
            elif y[4] == 1:
                msg += ("       Needs to be harvested.\n")
            return msg

        elif x == 2:
            farm.water_farm(y)
        elif x == 3:
            farm.harvest_farm(y)
        elif x == 4:
            farm.all_farms.append(y)
        elif x == 5:
            farm.level_farm(y)
        elif x == 6:
            msg = (f"Are you sure you want to destroy your {y[0]} farm? (y/n)\n")
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
            time_passed = (math.floor(time.time())) - current_time#seconds
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
                if i[5] >= 1800 and i[3] == 1:
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
                    msg += ("  A storm came by\n")
                    for i in affected_farms1:
                        msg += (f"    -level-{i[8]} {i[0]}|{i[10]} farm has been destroyed...\n")


                if need_water:
                    msg += ("  Farm needs water\n")
                    for i in affected_farms2:
                        msg += (f"    -level-{i[8]} {i[0]}|{i[10]}\n")


                if need_harvest:
                    msg += ("  Farm is ready to be harvested\n")
                    for i in affected_farms3:
                        msg += (f"    -level-{i[8]} {i[0]}|{i[10]}\n")
                return msg



            else:
                return ''

    #DONE
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

    #DONE
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

    #DONE
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
        have_stone = False
        have_dirt = False
        have_money = False
        level_farm = False
        cls()
        msg = ''
        msg += (f"Leveling up your farm costs\n")
        msg += (f"  {level_cost[0]} - {x[9][0]}\n")
        msg += (f"  {level_cost[1]} - stone\n")
        msg += (f"  {level_cost[2]} - dirt\n")
        msg += (f"  {level_cost[3]}$\n")
        msg += ("Be sure you harvest before leveling!\n")
        msg += ("Continue with level up? (y/n)\n")
        select = input(str(msg), 1)

        if select == 'y':
            for i in inventory:
                if i[0] == (x[9][0]) and i[1] >= level_cost[0]:
                    have_material = True
                if i[0] == 'stone' and i[1] >= level_cost[1]:
                    have_stone = True
                if i[0] == ('dirt') and i[1] >= level_cost[2]:
                    have_dirt = True
            if money > level_cost[3]:
                have_money = True

            if have_material and have_stone and have_dirt and have_money:
                for i in all_farms:
                    if x == i:
                        level_farm = True
                        i[8] += 1
                        i[3] = 0
                        i[6] = 0
                        i[4] = 0
                        
                        store((x[9][0]), -(level_cost[0]))
                        store('stone', -(level_cost[1]))
                        store('dirt', -(level_cost[2]))
                        money_add(-(level_cost[3]))
        # 0type, 1is built, 2cost, 3has_water, 4ready to be harvested,5time_passed,6time_waterd
        #  7time needs water , 8level ,9[0material ,1chance of storm breaking]
                    
            else:
                cls()
                msg = ''
                msg += ("You don't have enough materials...\n")
                if have_material == False:
                    material_quantity = 0
                    for i in inventory:
                        if i[0] == (x[9][0]):
                            material_quantity = i[1]
                    msg += str(f"You have {material_quantity}/{level_cost[0]} stone needed...\n")
                if have_stone == False:
                    stone_quantity = 0
                    for i in inventory:
                        if i[0] == 'stone':#x
                            stone_quantity = i[1]
                    msg += str(f"You have {stone_quantity}/{level_cost[1]} stone needed...\n")
                if have_dirt == False:
                    dirt_quantity = 0
                    for i in inventory:
                        if i[0] == 'dirt':#x
                            dirt_quantity = i[1]
                    msg += str(f"You have {dirt_quantity}/{level_cost[2]} dirt needed...\n")
                if have_money == False:
                    msg += str(f"You have ${money}/${level_cost[3]} money needed...\n")
                
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

    #DONE
    def build_farm():
        # $, material, stone, dirt, money
        # base_farm_cost = [100, 100, 40, 100]
        select = 0
        farm_selected = False
        have_enough_materials = False
        have_enough_stone = False
        have_enough_dirt = False
        have_enough_materials_to_build = False
        farm_types = [
        # 0type, 1is built, 2cost, 3has_water, 4ready to be harvested,5time_passed,6time_waterd
        #  7time needs water , 8level ,9[material ,chance of storm breaking]
            #['wheat', 1, 500, 0, 0, 0, 0, 3600, 1, [dirt, 50000]]
        #['bedrock', .0001]
        ['wheat', 1, 500, 0, 0, 0, 0, 3600, 1],
        ['log', 1, 1000, 0, 0, 0, 0, 5000, 1],
        ['sugar_cane', 1, 1000, 0, 0, 0, 0, 4000, 1],
        ['bone', 1 ,10000000, 0, 0, 0, 0, 28800, 1]
        ]

        for i in inventory:
            if i[0] == 'stone' and i[1] >= 100:
                have_enough_stone = True
            if i[0] == 'dirt' and i[1] >= 40:
                have_enough_dirt = True

        if have_enough_dirt and have_enough_stone:
            have_enough_materials_to_build = True

        while select != 'q':
            cls()
            z = 0
            x = 1
            k = 0
            msg = ''
            msg += ("What would you like to build it out of?\n")
            msg += number_list(farm_materials, 0)

            msg += ("Press (q) to quit\n")
            msg += "> #"
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
                                msg += (f"#{x} {i[0]} ${i[2]}, 100 wood_plank, and 40 dirt\n")
                                x += 1
                            msg += "> #"
                            select = input(msg , 1)
                            select = int(select)
                            select = farm_types[(select-1)]
                            if have_enough_materials_to_build and money >= select[2]:
                                select.append(choice_material)
                                select.append(len(all_farms) + 1)
                                input(f"Building {select[0]} farm!\n", 0)

                                while z != 4:
                                    if z == 0:
                                        cls()
                                        print("adding fence posts")
                                        while k != 6:
                                            print(".")
                                            time.sleep(.5)
                                            k += 1
                                        input((("")), 0)
                                        k = 0
                                    elif z == 1:
                                        cls()
                                        print(f"building the {choice_material[0]} supports")
                                        while k != 6:
                                            print(".")
                                            time.sleep(.5)
                                            k += 1
                                        input((("")), 0)
                                        k = 0
                                    elif z == 2:
                                        cls()
                                        print("dumping the dirt")
                                        while k != 6:
                                            print(".")
                                            time.sleep(.5)
                                            k += 1
                                        input("",0)
                                        k = 0
                                    elif z == 3:
                                        cls()
                                        print("decorating")
                                        while k != 6:
                                            print(".")
                                            time.sleep(.5)
                                            k += 1
                                        

                                    z += 1
                                    # $, material, stone, dirt, money
                                    # base_farm_cost = [100, 100, 40, 100]
                                cls()
                                input(f"{select[0]} farm is complete!\n", 0)
                                farm.EventFarm(4, select)
                                store(choice_material[0], -100)
                                store('stone', -100)
                                store('dirt', -40)
                                money_add(-(select[2]))
                                select = 'q'
                                farming()                                               

                            elif have_enough_materials_to_build:
                                input(f"You have {money}$/{select[2]}$ cash needed ...\n", 0)
                                select = 'q'

                            else:
                                msg = ''
                                msg +=("You don't have enough materials.\n")
                                if have_enough_stone == False:
                                    stone_quantity = 0
                                    for i in inventory:
                                        if i[0] == 'stone':#100
                                            stone_quantity = i[1]
                                    msg += str(f"You have {stone_quantity}/100 stone needed...\n")
                                if have_enough_dirt == False:
                                    dirt_quantity = 0
                                    for i in inventory:
                                        if i[0] == 'dirt':#40
                                            dirt_quantity = i[1]
                                    msg += str(f"You have {dirt_quantity}/40 dirt needed...\n")
                                input(msg, 0)
                                select = 'q'
                        else:
                            x_quantity = 0
                            for i in inventory:
                                if i[0] == choice_material[0]:
                                    x_quantity = i[1]
                            input(f"You have {x_quantity}/100 {choice_material[0]} needed...\n", 0)

                except (ValueError, IndexError, TypeError):
                    input("Not Valid\n", 0)

            else:
                pass


# Adds money, duhhh
def money_add(x):

    global money
    money = money + x


# Calculates the health taken vs current armor
def defense(x):
    # x/0 is for calculating and taking armor durability
    # x/1 is for printing the armor bar
    
    global current_helmet
    global current_chestplate
    global current_leggings
    global current_boots
    numbers = [current_helmet[4], current_chestplate[4], current_leggings[4], current_boots[4]]
    defense_average = sum(numbers) / len(numbers)

    if x > 0:
        if current_helmet[0] != 'skin':
            current_helmet[1] -= 1
            if current_helmet[1] == 0:
                input("Your helmet has broken", 0)
                current_helmet = ['skin', -1, 0, -1, 1]

        if current_chestplate[0] != 'skin':
            current_chestplate[1] -= 1
            if current_chestplate[1] == 0:
                input("Your chestplate has broken", 0)
                current_chestplate = ['skin', -1, 0, -1, 1]

        if current_leggings[0] != 'skin':
            current_leggings[1] -= 1
            if current_leggings[1] == 0:
                input("Your leggings have broken", 0)
                current_leggings = ['skin', -1, 0, -1, 1]

        if current_boots[0] != 'skin':
            current_boots[1] -= 1
            if current_boots[1] == 0:
                input("Your boots have broken", 0)
                current_boots = ['skin', -1, 0, -1, 1]

        return (math.ceil(x / defense_average))
    else:
        if defense_average > 1:
            return round((defense_average)*3)
        else:
            return 0
 

# Calculates damage of sword + wolves
def damage():

    global current_sword
    global wolves
    

    pain = 1
    if wolves > 0:
        pain = random.randint(1,3) * current_sword[4]
        pain += wolves

        if current_sword[0] != 'fist':
            current_sword[1] -= 1
            if current_sword[1] == 0:
                input("Your sword has broken", 0)
                current_sword = ['fist', -1, 0, -1, .5]

        return pain
    else:
        pain = random.randint(1,3) * current_sword[4]
        if current_sword[0] != 'fist':
            current_sword[1] -= 1
            if current_sword[1] == 0:
                input("Your sword has broken", 0)
                current_sword = ['fist', -1, 0, -1, .5]
        return pain


# Show achievements or notify of an achievement gained
def achievements(x):

    # x is whether to show all achievements or check for gained and notify(0 or 1)
    has = False
    msg = ''
    if x == 0:
        
        try:
            for i in achievements_list:
                if i[1] == 1:
                    msg += i[2]
                    msg += '\n'
        except:
            return"You don't have any, lol.\n"
            return msg
        else:
            return msg

    else:
        for i in achievements_list:
            if i[1] == 0 and i[0] >= i[3]:
                i[1] = 1
                msg += ("=========================\n")
                msg += ("=========================\n")
                msg += (f"You got {i[2]} achievement for {i[4]}!\n")
                msg += ("=========================\n")
                msg += ("=========================\n")
        return msg


# Selection menu
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
        input(achievements(0), 0)
    elif select == 'f': # farm
        farm.farming()
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
                file.write("\n")
                file.write("achievements_list = ")
                file.write(str(achievements_list))
                file.write("\n")
                global night
                global furnace_have
                global health
                global wolves
                global clock
                global money
                global current_pickaxe
                global user_id
                base = []
                base.append(night)
                base.append(furnace_have)
                base.append(health)
                base.append(wolves)
                base.append(clock)
                base.append(money)
                base.append(current_pickaxe)
                base.append(user_id)
                base.append(current_shovel)
                base.append(current_axe)
                base.append(current_helmet)
                base.append(current_chestplate)
                base.append(current_leggings)
                base.append(current_boots)
                base.append(current_sword)
                base.append(current_time)
                base.append(furnace_level)
                file.write("base = ")
                file.write(str(base))
            input("BYEEEE\n", 0)
            sys.exit()
    else:
        start()


# Crafting, duhhh
def craft():

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
    ['book_shelf', 'wood_plank', 6, 'book', 3],
    ['log_helmet', 'log', 5, 1],
    ['log_chestplate', 'log', 8, 1],
    ['log_leggings', 'log', 7, 1],
    ['log_boots', 'log', 4, 1],
    ['iron_helmet', 'iron', 5, 1],
    ['iron_chestplate', 'iron', 8, 1],
    ['iron_leggings', 'iron', 7, 1],
    ['iron_boots', 'iron', 4, 1],
    ['gold_helmet', 'gold', 5, 1],
    ['gold_chestplate', 'gold', 8, 1],
    ['gold_leggings', 'gold', 7, 1],
    ['gold_boots', 'gold', 4, 1],
    ['diamond_helmet', 'diamond', 5, 1],
    ['diamond_chestplate', 'diamond', 8, 1],
    ['diamond_leggings', 'diamond', 7, 1],
    ['diamond_boots', 'diamond', 4, 1],
    ['bedrock_helmet', 'bedrock', 5, 1],
    ['bedrock_chestplate', 'bedrock', 8, 1],
    ['bedrock_leggings', 'bedrock', 7, 1],
    ['bedrock_boots', 'bedrock', 4, 1],
    ['lapis_helmet', 'lapis', 5, 1],
    ['lapis_chestplate', 'lapis', 8, 1],
    ['lapis_leggings', 'lapis', 7, 1],
    ['lapis_boots', 'lapis', 4, 1],
    ['gold_axe', 'stick', 2, 'gold', 3, 1],
    ['wooden_axe', 'stick', 2, 'wood_plank', 3, 1],
    ['stone_axe', 'stick', 2, 'cobblestone', 3, 1],
    ['iron_axe', 'stick', 2, 'iron', 3, 1],
    ['diamond_axe', 'stick', 2, 'diamond', 3, 1],
    ['gold_shovel', 'stick', 2, 'gold', 1, 1],
    ['wooden_shovel', 'stick', 2, 'wood_plank', 1, 1],
    ['stone_shovel', 'stick', 2, 'cobblestone', 1, 1],
    ['iron_shovel', 'stick', 2, 'iron', 1, 1],
    ['diamond_shovel', 'stick', 2, 'diamond', 1, 1],
    ['gold_sword', 'stick', 1, 'gold', 2, 1],
    ['wooden_sword', 'stick', 1, 'wood_plank', 2, 1],
    ['stone_sword', 'stick', 1, 'cobblestone', 2, 1],
    ['iron_sword', 'stick', 1, 'iron', 2, 1],
    ['diamond_sword', 'stick', 1, 'diamond', 2, 1],
    ['coal_block', 'coal', 9, 1],
    ['iron_block', 'iron', 9, 1],
    ['gold_block', 'gold', 9, 1],
    ['diamond_block', 'diamond', 9, 1],
    ['redstone_block', 'redstone', 9, 1],
    ['coal', 'coal_block', 1, 9],
    ['iron', 'iron_block', 1, 9],
    ['gold', 'gold_block', 1, 9],
    ['diamond', 'diamond_block', 1, 9],
    ['redstone', 'redstone_block', 1, 9],
    ['bedrock', 'diamond_block', 1, 'obsidian', 8, 1]


    ]
    crafting.sort()
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
    msg = ''

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
                        for z in inventory:
                            if i[3] == z[0] and i[4] <= z[1]:
                                available.append(i)
            else:
                pass
    
    try:
        select = select_list(available, "What would you like to craft?\n")[0]
        k = 2
    except:
        pass

    if k == 2:
        z = 0
        
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


                msg = ''
                msg += (f"Make {select} how many times?\n")
                select2 = two_digit_select(msg, possible)
                try:
                    quantity2 = int(select2)
                    done = True
                except (TypeError, ValueError):
                    done2 = True



                # Where the crafting actually happens
                
        if done2 == False:
            msg2 = ''
            for e in crafting:
                if e[0] == select:

                    if len(e) == 6:
                        store(e[0], (e[5] * quantity2))
                        store(e[1], (-e[2] * quantity2))
                        store(e[3], (-e[4] * quantity2))
                        msg2 = (f"You gained {quantity2 * e[5]} {select}")
                        

                    else:
                        store(e[0], (e[3] * quantity2))
                        store(e[1], (-e[2] * quantity2))
                        msg2 = (f"You gained {quantity2 * e[3]} {select}")

            msg = str(f"Crafting {select}")
            tick(1)
            input(msg, [3, .5])
            input(msg2, 0)


# Eating, duhhh
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
            
            health_added = 0
            food_selected = 0
            y = 0
            food_list = []
            for i in inventory:
                for x in edible:
                    if x[0] == i[0] and i[1] >= 1:
                        food_list.append(x[0])
            food_list.sort()
            while query != 'q':
                msg = ''
                msg += health_bar()
                try:
                    x = 1
                    msg += ("What are you hungry for?\n")
                    
                    msg += number_list(food_list, -1)
                    msg += ("\n")
                    select = int(input(str(msg), 1))
                    select = food_list[(select - 1)]
                    query = 'q'
                    
                except (ValueError, TypeError, IndexError):
                    have_food = False
                    query = 'q'
            while have_food:
                health_added = 0
                select2 = 0
                msg = ''
                msg += health_bar()
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
                                msg += ("Yuck...\n")
                                msg += (f"The {food_selected} poisons you, taking {health_added} hp!\n")
                                input(msg, 0)
                                achievements_list[10][0] += 1
                                if health <= 0:
                                    adventure.dead()


                    have_food = False
                    quantity = 0
                    for i in inventory:
                        if i[0] == food_selected:
                            quantity = i[1]
                            if quantity >= 1:
                                have_food = True
                    if quantity and have_food:
                        msg = ''
                        msg += health_bar()
                        msg += (f"{quantity} left, eat another? (y/n)\n")
                        select2 = input(str(msg), 1)

                        if select2 == 'y':
                            pass
                        else:
                            have_food = False
                    else:
                        msg += health_bar()
                        msg += ("No more food!\n")
                        input(msg, 0)
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


# Stores x, y times
def store(x,y):

    # ['stick', 'wood_plank', 2, 4]
    # ['fishing_rod', 'stick', 3, 'string', 2, 1]]
    # x is the item to add
    # y is the quanity
    # This is how all items are stored into the inventory
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


# Calculates the ore found at x height
def ore(height):

    # Takes current height and returns the available ores
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


# Digging down at height
def dig_down(height):


    global health
    global current_pickaxe
    global current_shovel

    block = 0
    select = 0
    z = 0
    bucket = False
    
    block = ore(height)
    
    
    # if block == 'dirt' for shovel
    msg = ''
    x = 0
    for i in inventory: 
        if i[0] == 'water_bucket':
            x = i[1]
    msg += health_bar()
    msg += str(f"  {x}-water buckets\n")
    tick(1)
    msg += ("You mine the block below you")
    if block == 'dirt' or block == 'gravel':
        input(msg, [3, float(.5/current_shovel[4])])
        if current_shovel[1] > 0 and current_shovel[0] != 'fist':
                current_shovel[1] -= 1

        if current_shovel[1] == 0:
            input("Your shovel has broken...\n", 0)
            current_shovel = ['fist', -1, 0, -1, .5]

    else:
        input(msg, [3, float(.5/current_pickaxe[4])])
        if current_pickaxe[1] > 0 and current_pickaxe[0] != 'fist':
                current_pickaxe[1] -= 1

        if current_pickaxe[1] == 0:
            input("Your pickaxe has broken...\n", 0)
            current_pickaxe = ['fist', -1, 0, -1, .5]
    
    if block != 'bedrock' and block != 'lava':
        
        if pickaxe(block) == True:
            if block == 'diamond':
                    achievements_list[1][0] += 1
            msg = ''
            msg += health_bar()
            for i in inventory: 
                if i[0] == 'water_bucket':
                    x = i[1]
            msg += str(f"  {x}-water buckets\n")
            msg += (f"You get 1 {block}!")
            cls()
            store(block, 1)
        else:
            msg = ''
            x = 0
            msg += health_bar()
            for i in inventory: 
                if i[0] == 'water_bucket':
                    x = i[1]
            msg += str(f"  {x}-water buckets\n")
            msg += ("Try using a better pickaxe")
            cls()

        height -= 1
        health_bar()
        if height > 62:
            msg += ("\nClimb back up or keep digging(c/d)\n")
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
                health = 0
                msg += health_bar()
                for i in inventory: 
                    if i[0] == 'water_bucket':
                        x = i[1]
                msg += str(f"  {x}-water buckets\n")
                msg += ("OUCH LAVA BURNS!\n")
                msg += ("Bring a water bucket next time.\n")
                input(msg, 0)
                adventure.dead()
            else:
                achievements_list[3][0] += 1
                msg = ''
                health -= 10
                msg += health_bar()
                store('water_bucket', -1)
                for i in inventory: 
                    if i[0] == 'water_bucket':
                        x = i[1]
                msg += str(f"  {x}-water buckets\n")
                msg += ("You use your water bucket to turn the lava into obsidian\n")
                msg += ("You also lose 10 hp from well, lava\n")
                if health <= 0:
                    adventure.dead()
                block = 'obsidian'
                
                store('bucket', 1)

                if pickaxe(block) == True:
                    msg += (f"You get 1 {block}!\n")
                    store(block, 1)
                else:
                    msg += ("Try using a better pickaxe")

                height -= 1
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


# Calculates if your current_pickaxe can break a block or not
def pickaxe(block):

    # current_pickaxe = ['wooden_pickaxe', 33, 1, 59]
    global current_pickaxe
    can_mine = False
    for i in ores:
        if i[0] == block and i[2] <= current_pickaxe[2]:
            can_mine = True

    if can_mine == False:
        return False
    else:
        return True


# duhh
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
    inventory.sort()
    for i in inventory:
        #MAX len 17
        text = (f" {i[1]}-{i[0]}")
        var1 = 17 - len(text)
        msg += str(text + ' ' * var1 + '|')
        
        k += 1
        m += 1
        if k == 3:
            msg += ("\n")
            k = 0
    msg += ("\n")
    msg += ("Equipment\n")

    msg += number_list(equipment, 0)


    msg += ("\nThrow out an item or equipment? (i/e)\n")
    select = input(str(msg), 1)

    if select == 'i':
        msg = ' '

        msg += ("Select an item to destroy\n")
        try:
            select = select_list(inventory, msg)
            msg = ''
            msg += str(f"Are you sure you want to destroy {select[0]}? (y/n)\n")
            is_sure = input(str(msg), 1)
            if is_sure:
                store(select[0], -(select[1]))


        except(ValueError, TypeError, IndexError):
            input("Invalid", 0)


    elif select == 'e':
        msg = ''

        msg += ("Select an item to destroy\n")
        try:
            select_item = (select_list(equipment, msg))[0]
            msg += ("Are you sure? (y/n)\n")
            is_sure = input(str(msg), 1)
            if is_sure:
                store(select_item, -1)

        except(ValueError, TypeError, IndexError):
            input("Invalid", 0)



    else:
        pass


# duhh, also for equipping
def view_equipment():

    global picks
    global shovels
    global axes
    global swords
    global helmets
    global chestplates
    global leggings
    global boots
    global current_pickaxe
    global current_shovel
    global current_axe
    global current_sword
    global current_helmet
    global current_chestplate
    global current_leggings
    global current_boots
    global equipment
    equipment.sort()
    x = 0
    z = 0
    y = 1
    a = 0
    old_pick = 0
    percentage1 = 0
    msg = 'Equipped\n'
    
    if len(current_helmet) > 1 and current_helmet[0] != 'skin':
        percentage2 = math.ceil( 100* (current_helmet[1]) / current_helmet[3])
        msg += (f" {current_helmet[0]} {percentage2}%\n")

    if len(current_chestplate) > 1 and current_chestplate[0] != 'skin':
        percentage2 = math.ceil( 100* (current_chestplate[1]) / current_chestplate[3])
        msg += (f" {current_chestplate[0]} {percentage2}%\n")

    if len(current_leggings) > 1 and current_leggings[0] != 'skin':
        percentage2 = math.ceil( 100* (current_leggings[1]) / current_leggings[3])
        msg += (f" {current_leggings[0]} {percentage2}%\n")

    if len(current_boots) > 1 and current_boots[0] != 'skin':
        percentage2 = math.ceil( 100* (current_boots[1]) / current_boots[3])
        msg += (f" {current_boots[0]} {percentage2}%\n")

    if len(current_pickaxe) > 1 and current_pickaxe[0] != 'fist':
        percentage2 = math.ceil( 100* (current_pickaxe[1]) / current_pickaxe[3])
        msg += (f" {current_pickaxe[0]} {percentage2}%\n")
    
    if len(current_shovel) > 1 and current_shovel[0] != 'fist':
        percentage2 = math.ceil( 100* (current_shovel[1]) / current_shovel[3])
        msg += (f" {current_shovel[0]} {percentage2}%\n")

    if len(current_axe) > 1 and current_axe[0] != 'fist':
        percentage2 = math.ceil( 100* (current_axe[1]) / current_axe[3])
        msg += (f" {current_axe[0]} {percentage2}%\n")

    if len(current_sword) > 1 and current_sword[0] != 'fist':
        percentage2 = math.ceil( 100* (current_sword[1]) / current_sword[3])
        msg += (f" {current_sword[0]} {percentage2}%\n")
    

    
    #[['wooden_pickaxe', 4, 1, 59], []]

    if len(equipment) > 0:
        msg += '\nUnequipped\n'
        for i in equipment:
            if i != None and len(equipment[0]) > 0:
                if i[1] != 0:
                    percentage1 = math.ceil( 100* (i[1]) / i[3])
                    msg += str(f" |{i[0]} {percentage1}% ")
                    z += 1
                    if z == 2:
                        msg += ("\n")
                        z = 0
                    y += 1

        msg += ("\n")
        msg += ("Equip something? (e) or Equip best (b)\n")
        select = input(msg, 1)
        if select == 'e':
            try:

                msg = 'Equip a #\n'
                select = select_list(equipment, msg)

                if 'pickaxe' in select[0]:
                    store(select[0], -1)                    
                    old_equipment(current_pickaxe)                    
                    current_pickaxe = select
                    input(str(f"{select[0]} equipped!\n"), 0)

                elif 'axe' in select[0]:
                    store(select[0], -1)                    
                    old_equipment(current_axe)                    
                    current_axe = select
                    input(str(f"{select[0]} equipped!\n"), 0)

                elif 'shovel' in select[0]:
                    store(select[0], -1)                    
                    old_equipment(current_shovel)                    
                    current_shovel = select
                    input(str(f"{select[0]} equipped!\n"), 0)

                elif 'sword' in select[0]:
                    store(select[0], -1)                    
                    old_equipment(current_sword)                    
                    current_sword = select
                    input(str(f"{select[0]} equipped!\n"), 0)

                elif 'helmet' in select[0]:
                    store(select[0], -1)                    
                    old_equipment(current_helmet)                    
                    current_helmet = select
                    input(str(f"{select[0]} equipped!\n"), 0)

                elif 'chestplate' in select[0]:
                    store(select[0], -1)                    
                    old_equipment(current_chestplate)                    
                    current_chestplate = select
                    input(str(f"{select[0]} equipped!\n"), 0)

                elif 'leggings' in select[0]:
                    store(select[0], -1)                    
                    old_equipment(current_leggings)                    
                    current_leggings = select
                    input(str(f"{select[0]} equipped!\n"), 0)

                elif 'boots' in select[0]:
                    store(select[0], -1)                    
                    old_equipment(current_boots)                    
                    current_boots = select
                    input(str(f"{select[0]} equipped!\n"), 0)

            except (TypeError, ValueError, IndexError):
                input("", 0)

        elif select == 'b':
            x = 0
            while x != 200:
                x += 1
                for i in equipment:

                    if 'pickaxe' in i[0]:
                        if i[4] > current_pickaxe[4]:
                            store(i[0], -1)                    
                            old_equipment(current_pickaxe)                    
                            current_pickaxe = i

                    elif 'axe' in i[0]:
                        if i[4] > current_axe[4]:
                            store(i[0], -1)                    
                            old_equipment(current_axe)                    
                            current_axe = i

                    elif 'shovel' in i[0]:
                        if i[4] > current_shovel[4]:
                            store(i[0], -1)                    
                            old_equipment(current_shovel)                    
                            current_shovel = i

                    elif 'sword' in i[0]:
                        if i[4] > current_sword[4]:
                            store(i[0], -1)                    
                            old_equipment(current_sword)                    
                            current_sword = i

                    elif 'helmet' in i[0]:
                        if i[4] > current_helmet[4]:
                            store(i[0], -1)                    
                            old_equipment(current_helmet)                    
                            current_helmet = i

                    elif 'chestplate' in i[0]:
                        if i[4] > current_chestplate[4]:
                            store(i[0], -1)                    
                            old_equipment(current_chestplate)                    
                            current_chestplate = i

                    elif 'leggings' in select[0]:
                        if i[4] > current_leggings[4]:
                            store(i[0], -1)                    
                            old_equipment(current_leggings)                    
                            current_leggings = i

                    elif 'boots' in i[0]:
                        if i[4] > current_boots[4]:
                            store(i[0], -1)                    
                            old_equipment(current_boots)                    
                            current_boots = i

            input("Best equipment on!", 0)


        


    else:
        msg += ("You don't have any equipment\n")
        input(msg, 0)


# Returns health bar and armor bar(If you have any armor)
def health_bar():

    global health
    msg = ''
    msg += ('  Health('+ (int(health/10)*2)*'@'+ ((-(int(health/10)-10))*2)*'-' + ')\n')
    if defense(0) > 0:
        msg += str("  Armor (" + ("%" * int(defense(0))) + ')\n')
    return msg


# When unequipping something, if it's not a fist or skin, puts back in inventory
def old_equipment(x):
    if x[0] == 'fist' or x[0] == 'skin':
        pass
    else:
        equipment.append(x)


# duhh
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


# Function to level up the furnace
def upgrade_furnace():

    # costs 23 cobblestone * current_level
    # add furnace_level to same
    global furnace_level
    have_enough = False
    total_cobble = 0
    select = 0
    cost = (23 * furnace_level)
    for i in inventory:
        if i[0] == 'cobblestone':
            if i[1] > cost:
                total_cobble = i[1]
                have_enough = True

    if have_enough:
        msg = ''
        msg += str(f" Upgrading your lvl-{furnace_level}|furnace\n")
        msg += str(f" costs {cost} cobblestone, continue? (y/n)")
        select = input(msg, 1)
        if select == 'y':
            store('cobblestone', -(cost))
            furnace_level += 1
            msg = str(f" You upgrade your furnace to level {furnace_level}")
            input(msg, 0)
    else:
        msg = str(f"You have {total_cobble}/{cost} needed cobblestone")
        input(msg, 0)


# Gives the ability to add numbers pressed together to return a total that is two digits
# all while only being able to press 1 key at a time
def two_digit_select(message, x):

    # x is the available_material(max)
    done2 = False
    input_material_count = 0
    material_count = 0
    material = 0
    available_material = x
    msg = ''
    msg += "Press (q) to quit.\n"
    msg += message
    msg += str(f"(0 - {available_material})?\n")
    msg += "Simply press a number to add that many, press(d) when done -\n"
    
    while done2 == False:
        if input_material_count > 0:
            msg += str(input_material_count)
            msg += ' + '
        select = input(msg, 1)
        if select == 'd':
            if input_material_count > 0:
                material_count = input_material_count
            done2 = True

        elif select == 'q':
            done2 = True
            material_count = 'q'

        else:
            try:
                if int(select) <= available_material:
                    input_material_count += select
                    available_material -= select
                else:
                    input("You don't have that many!", 0)
            except:
                input('(Invalid)', 0)

    return material_count


# Duhh
def furnace():

    global furnace_level

    fuel_quantity = [
    ['coal', 8], ['log', 4], ['wood_plank', 2], ['stick', 1], ['wooden_pickaxe', 3], ['wooden_shovel', 2],
    ['wooden_axe', 3], ['wooden_sword', 3], ['log_helmet', 10], ['log_chestplate', 16],
    ['log_leggings', 14], ['log_boots', 8], ['coal_block', 72]
    ]

    cook_output = [
    ['iron_ore', 'iron'], ['raw_porkchop', 'cooked_porkchop'], ['raw_beef', 'cooked_beef'],
    ['gold_ore', 'gold'], ['cobblestone', 'stone'], ['log', 'coal'], ['raw_fish', 'cooked_fish'],
    ['raw_lambchop', 'cooked_lambchop'], ['raw_chicken', 'cooked_chicken']
    ]

    gained = []
    in_gained = False
    used_fuel = []
    in_used_fuel = False
    #left_over_fuel = 0
    #left_over_material = 0

    can_cook = False
    have_fuel = False
    furnace_have = False
    done = False
    have_fuel = False
    fuel = ''
    material = ''
    fuel_value = 0
    select = 0
    double = 1
    

    for i in inventory:
        if i[0] == 'furnace':
            furnace_have = True

    for x in inventory:
        for i in cook_output:
            if x[0] == i[0] and x[1] > 0:
                can_cook = True

    for i in inventory:
        for x in fuel_quantity:
            if x[0] == i[0] and i[1] >= 1:
                have_fuel = True

    for i in equipment:
        for x in fuel_quantity:
            if x[0] == i[0] and i[1] >= 1:
                have_fuel = True

    if furnace_have == False:
        input("Try crafting a furnace first", 0)

    else:
        select = input("(u)pgrade your furnace?", 1)
        if select == 'u':
            upgrade_furnace()

        if can_cook == True and have_fuel == True:
            while done == False:

                
                input_material_count = 0
                selected_fuel = 0
                selected_material = 0
                available_material = 0
                cook_list = []
                fuel_list = []
                
                for x in inventory:
                    for i in cook_output:
                        if x[0] == i[0] and x[1] > 0:
                            cook_list.append(i[0])

                for i in inventory:
                    for x in fuel_quantity:
                        if x[0] == i[0] and i[1] >= 1:
                            fuel_list.append(x[0])

                for i in equipment:
                    for x in fuel_quantity:
                        if x[0] == i[0]:
                            fuel_list.append(x[0])

                cook_list.sort()
                fuel_list.sort()


                msg = ''

                msg += ("Add fuel or add material (f/m) press (q) to quit\n")
                select = input(msg, 1)

                if select == 'f':
                    fuel_count = 0
                    done2 = False
                    msg = 'What fuel would you like to add?\n'
                    selected_fuel = select_list(fuel_list, msg)
                    for i in inventory:
                        if selected_fuel == i[0] and i[1] > 0:
                            fuel_count = i[1]
                            have_fuel = True
                            
                    for i in equipment:
                        if selected_fuel == i[0]:
                            fuel_count = 1
                            have_fuel = True

                    fuel = selected_fuel
                    


                elif select == 'm':
                    material_count = 0
                    done2 = False
                    msg = 'what material would you like to add?\n'
                    selected_material = select_list(cook_list, msg)
                    if selected_material:
                        for i in inventory:
                            if selected_material == i[0] and i[1] > 0:
                                available_material = i[1]
                        msg += "Press (q) to quit cooking\n"
                        msg += str(f"How many would you like to add (0 - {available_material})?\n")
                        msg += "Simply press a number to add that many, press(d) when done -\n"
                        
                        while done2 == False:
                            if input_material_count > 0:
                                msg += str(input_material_count)
                                msg += ' + '
                            select = input(msg, 1)
                            if select == 'd':
                                if input_material_count > 0:
                                    material_count = input_material_count
                                    material = selected_material
                                done2 = True

                            elif select == 'q':
                                done2 = True
                                done = True
                                material_count = 0

                            else:
                                try:
                                    if int(select) <= available_material:
                                        input_material_count += select
                                        available_material -= select
                                    else:
                                        input("You don't have that many!", 0)
                                except:
                                    input('(Invalid)', 0)


                elif select == 'q':
                    done = True

                else:
                    input('(Invalid)', 0)

                
                try:
                    msg = ''
                    while have_fuel == True and material_count > 0:
                        cls()
                        
                        if fuel_value == 0 and fuel_count > 0:
                            for i in fuel_quantity:
                                if fuel == i[0]:
                                    fuel_value = i[1]
                                    msg = ''
                                    msg += str(f"{fuel} added to flame...\n")
                                    have_fuel = True
                                    store(fuel, -1)
                                    fuel_count -= 1
                                    for x in used_fuel:
                                        try:
                                            if fuel == x[0]:
                                                x[1] += 1
                                                in_used_fuel = True
                                                
                                        except TypeError:
                                            pass
                                    if in_used_fuel == False:
                                        used_fuel.append([fuel, 1])
                                            
                                            
                                        

                        elif fuel_value > 0:
                            material_count -= 1
                            fuel_value -= 1
                            if random.randint(0,100) < (furnace_level * 2):
                                double = 2
                                msg += ("--Double bonus--")
                            else:
                                double = 1
                            msg += str(f"Cooking {material} with {fuel}")
                            input(msg, [3, float(1/furnace_level)])# speed up with furnace level
                            msg = ''
                            tick(1)
                            in_gained = False
                            for i in cook_output:
                                if i[0] == material:
                                    for x in gained:
                                        try:
                                            if i[1] == x[0]:
                                                x[1] += double
                                                in_gained = True
                                        except TypeError:
                                            pass
                                    if in_gained == False:
                                        gained.append([i[1], double])
                                        
                                    store(i[1], double)# chance of doubling with furnace level
                                    store(material, -1)
                        else:
                            have_fuel = False
                except UnboundLocalError:
                    pass

            
            try:
                if gained[0][1] > 0:
                    msg = ''
                    msg += 'You gained...\n'
                    for i in gained:
                        msg += f" {i[1]} | {i[0]}\n"
                if used_fuel[0][1] > 0:
                    msg += 'Fuel used...\n'
                    for i in used_fuel:
                        msg += f" {i[1]} | {i[0]}\n"
                    input(msg, 0)
                
            except:
                pass



        else:
            msg = ''
            msg += ("Cooks you can't\n")
            if can_cook == True:
                msg += ("No fuel!\n")
                input(msg, 0)
            else:
                msg += ("You have nothing to cook!\n")
                input(msg, 0)


# Checking the clock or moving time forward
def tick(x):

    # tick(0) checks the clock
    # tick(x) checks clock and moves time forward by x

    global clock
    global night
    if x == 0:
        if clock < 100:
            night = False
            return ("  Birds are singing in the sunlight...\n")
        else:
            night = True
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


# Selecting a number from a list, being able to scroll through(for 1 number press)
def select_list(available, message):

    try:
        scroll = True
        check = True
        select = 0
        k = 1
        x = 1
        
        while k == 1:
            available2 = available
            while scroll:
                msg = ''
                
                var = len(available2)
                if len(available2) > 9 and check:
                    if select == 's':
                        x = 0
                        available2 = [x for x in available2 if x not in available]
                        var -= 8

                    x = 0
                    available = []
                    for i in available2:
                        available.append(available2[x])
                        x += 1
                        if x == 9: break

                if var > 9:
                    msg += ("Press (s) to scroll!\n")
                    msg += ("====================\n")
                msg += available
                msg += number_list(available, 0)
                msg += ("\n")
                msg += message
                msg += ("(q to quit)\n")
                select = input(msg, 1)
                if select == 's':
                    scroll = True
                    check = True
                elif select == 'q':
                    k = 3
                    scroll = False
                    
                else:
                    try:
                        select = int(select)
                        return available[(select - 1)]
                        scroll = False
                    except:
                        input("(Invalid)", 0)
                        check = False
    except:

        scroll = True
        check = True
        select = 0
        k = 1
        x = 1
        
        while k == 1:
            available2 = available
            
            while scroll:
                msg = ''
                var = len(available2)
                if len(available2) > 9 and check:
                    if select == 's':
                        x = 0
                        available2 = [x for x in available2 if x not in available]

                    x = 0
                    available = []
                    for i in available2:
                        available.append(available2)
                        x += 1
                        if x == 9: break

                if var > 9:
                    msg += ("Press (s) to scroll!\n")
                    msg += ("====================\n")
                
                msg += number_list(available, -1)
                msg += ("\n")
                msg += message
                msg += ("(q to quit)\n")
                select = input(msg, 1)
                if select == 's':
                    scroll = True
                    check = True
                elif select == 'q':
                    k = 3
                    scroll = False
                    
                else:
                    try:
                        select = int(select)
                        return available[(select - 1)]
                        scroll = False
                    except:
                        input("(Invalid)", 0)
                        check = False


# Returns a pretty list with each item numbered
def number_list(x,y):

    # x is the list to print. y is the list indice(-1 for no indice) diamond_pickaxe
    m = 1
    k = 0
    var1 = 0
    text = 0
    done = False
    msg = ' '
    if y != -1:
        for i in x:
            
            #MAX len 19 lol
            text = (f"|#{m}-{i[y]}")
            var1 = 19 - len(text)
            msg += (text + ' ' * var1)
            k += 1
            m += 1
            if k == 3:
                msg += ("\n ")
                k = 0
        return msg
    else:

        for i in x:
            
            #MAX len 16
            text = (f"|#{m}-{i}")
            var1 = 18 - len(text)
            msg += str(text + ' ' * var1)
            k += 1
            m += 1
            if k == 3:
                msg += ("\n ")
                k = 0
        return msg


# Start menu
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

    msg = ''
    msg += tick(0)
    msg += achievements(1)
    msg += health_bar()
    msg += str(f"  In the bank = ${money}\n")
    msg += farm.EventFarm(0, all_farms)
    msg += question
    select = input(msg, 1)

    #select = input(ms, 1g)
    msg = ''
    
    if select == 'a':# adventure()
        cls()
        adventure.adv()

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

    cls()
    select = 0

    


#version('test')
version('pre-alpha 3.0')

# App runs
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
                msg = (f"Welcome back, {user_id}")
                input(msg, 0)
                start()
        except Exception:
            input("This is broken lol Error### bleehgfajfasaofowaowo.   wkkd        .\n", 0)
# end


