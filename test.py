import random
import time
import os

night = False
health = 100
height = 64
damage = 1
clock = 0



def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# for 1 material [item to craft, material, quantity of material, quantity received]
# for 2 material [item to creaft, material, quantity of material, material2, quantity of material2, quantity received]
crafting = [['furnace', 'cobblestone', 8, 1], 
['bed', 'wool', 3, 'wood_plank', 3, 1],
['wood_plank', 'log', 1, 4], 
['stick', 'wood_plank', 2, 4],
['fishing_rod', 'stick', 3, 'string', 2, 1],
['bucket', 'iron', 3, 1],
['torch', 'coal', 1,'stick', 1, 2]]



cook_output = [['iron_ore', 'iron'], ['raw_porkchop', 'cooked_porkchop'], ['raw_beef', 'cooked_beef'],
['gold_ore', 'gold'], ['cobblestone', 'stone'], ['log', 'coal'], ['raw_fish', 'cooked_fish'],
['raw_lambchop', 'cooked_lambchop'], ['raw_chicken', 'cooked_chicken']]

inventory = [['torch', 1]]

fuel = [['coal', 8], ['log', 4], ['wood_plank', 2], ['stick', 1]]

edible = [['raw_porkchop', 5], ['raw_beef', 5], ['cooked_porkchop', 20], ['cooked_beef', 20],
['apple', 10], ['rotten_flesh', -5], ['raw_fish', 5], ['cooked_fish', 15], ['cooked_chicken', 20],
['cooked_lambchop', 20], ['raw_chicken', 5], ['raw_lambchop', 5]]


def craft():
    global crafting
    global inventory
    available = []
    item1 = False
    x = 1
    z = 0
    y = 0
    for i in crafting:

        if len(i) == 4:
            for x in inventory:
                if i[1] == x[0] and i[2] <= x[1]:
                    available.append(i[0])
        
        if len(i) == 6:
            for x in inventory:
                if i[1] == x[0] and i[2] <= x[1]:
                    item1 = True

            for x in inventory:
                if item1 == True and i[3] == x[0] and i[4] <= x[1]:
                    available.append(i[0])

    print("Items you can craft")
    for i in available:
        if i != None:
            print(i, end = "   ")
            z += 1
            if z == 4:
                print("")
                z = 0
            y += 1
    print("")
    print("What would you like to craft? #")
    select = input("> ")

    for i in available:
        if select == i:
            print(f"Crafting {i}")
            while z != 3:
                print(".")
                time.sleep(.5)
                z += 1 

            for e in crafting:
                if e[0] == select:

                    if len(e) == 6:
                        store(e[0], e[5])
                        store(e[1], -e[2])
                        store(e[3], -e[4])
                        print(f"You gained {e[5]} {select}")
                        input("> ")
                    else:
                        store(e[0], e[3])
                        store(e[1], -e[2])
                        print(f"You gained {e[3]} {select}")
                        input("> ")
    
        
    
def a2():
    print("@@@@@      Skelouse      @@@@@")

def eat():
    global health
    health_added = 0
    food_selected = 0
    y = 0
    food_list = []
    for i in inventory:
        for x in edible:
            if x[0] == i[0] and i[1] >= 1:
                food_list.append(x[0])

    print("What are you hungry for?")
    for i in food_list:
                print(i, end ="   ")
                y += 1
                if y == 4:
                    print("")
                    y = 0
    print("")
    select = input("> ")
    if select in food_list:
        print("Yummy")
        for x in edible:
            if x[0] == select:
                health_added = x[1]
                food_selected = x[0]
        
        store(food_selected, -1)
        health += health_added
        print(f"You eat {food_selected} for {health_added} hp")
        if health >= 100:
            print("Your health is full!")
            health = 100
        input("> ")
        

        
    else:
        print("Not valid")
        input("> ")



# ['stick', 'wood_plank', 2, 4]
# ['fishing_rod', 'stick', 3, 'string', 2, 1]]
# x is the item to add
# y is the quanity
# This is how all items are stored into the inventory
def store(x,y):
    added = False
    for i in inventory:
        if i[0] == x:
            i[1] = i[1] + y
            added = True

    if added != True:
        inventory.append([x, y])

# Takes current height and returns the available ores
def ore(height):

    ores = [['bedrock', 5], ['diamond', 14], ['redstone', 14],
    ['gold_ore', 30], ['lapis', 30], ['lava', 30], ['iron_ore', 61], ['coal', 61], ['gravel', 61],
    ['cobblestone', 61]]
    mineable = []
    for i in ores:
        if i[1] >= height:
            mineable.append(i[0])
    if height < 61:
        return mineable[random.randint(0, (len(mineable)-1))]
    else:
        return 'dirt'

def cave_ore(height):

    ores = [['diamond', 14], ['redstone', 14],
    ['gold_ore', 30], ['lapis', 30], ['iron_ore', 61], ['coal', 61]]
    mineable = []
    for i in ores:
        if i[1] >= height:
            mineable.append(i[0])
    if height < 61:
        return mineable[random.randint(0, (len(mineable)-1))]
    else:
        return 'dirt'


def dig_down(height):
    global health
    block = 0
    z = 0
    bucket = False

    print("You mine the block below you")
    while z != 3:
        print(".")
        time.sleep(.5)
        z += 1
    block = ore(height)

    
    if block != 'bedrock' and block != 'lava':
        print(f"You get 1 {block}!")
        height -= 1
        print("Climb back up or keep digging(c/d)")
        store(block, 1)
        select = input("> ")
        if select == 'c':
            print("You climb back to the surface")
            input("> ")

        elif select == 'd':
            dig_down(height)
        
        else:
            print("Returning to surface because you can't type")
            input("> ")

    else:

        if block == 'lava':
            for i in inventory:
                if i[0] == 'water_bucket':
                    bucket = True
            
            if bucket == False:
                print("OUCH LAVA BURNS!")
                print("Bring a water bucket next time.")
                dead()
            
            else:
                print("You use your water bucket to turn the lava into obsidian")
                print("You also lose 10 hp from well, lava")
                health -= 10
                block = 'obsidian'
                store('water_bucket', -1)
                store('bucket', 1)
                print(f"You get 1 {block}!")
                store(block, 1)
                height -= 1
                print("Climb back up or keep digging(c/d)")
                select = input("> ")

                if select == 'c':
                    print("You climb back to the surface")
                    input("> ")

                elif select == 'd':
                    dig_down(height)
        
                else:
                    print("Returning to surface because you can't type")
                    input("> ")

        else:    
            print("You can't mine through bedrock silly!")
            print("Returning to surface")
            input("> ")

def a4():
    a1()
    a2()
    a3()   

# Defines what you find on an adventure
def adventure():
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
        else:
            adventure()

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
            river()

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
        input("> ")



def fill_bucket():
    z = 0
    print("Your bucket fills up")
    
    while z != 3:
        print(".")
        time.sleep(.5)
        z += 1
    
    for i in inventory:
        if i[0] == 'bucket' and i[1] >= 1:
            store('bucket', -1)
            store('water_bucket', 1)


cls()
  


def fish():
    print("You throw in your line")
    select = 0
    z = 0
    while z != 10:
        print(".")
        time.sleep(1)
        z += 1
    if random.randint(0,100) < 30:
        print("You caught a fish!")
        store('raw_fish', 1)
        print("Continue fishing? (y/n)")
        select = input("> ")

    else:
        print("No bite, keep fishing? (y/n)")
        select = input("> ")

    if select == 'n':
        print("The river waves goodbye")
        input(">")
    else:
        fish()

def cave():
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
                time.sleep(.5)
                z += 1
            store(block, 1)    
            deep_cave()
            
        else:
            fight_mob(search_mob[random.randint(0,2)])
            deep_cave()

    elif select == 'n':
        adventure()

    else:
        cave()
def a3():
    print("@@@@@      2018          @@@@@")
    input("> ")
def deep_cave():
    global height
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
                time.sleep(.5)
                z += 1
            store(block, 1)    
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
        input("> ")

    
    else:
        print("breaking big tree")
        while z != 6:
            print(".")
            time.sleep(4)
            z += 1
        amount = random.randint(10,18)
        store('log', amount)
        print(f"You got {amount} logs!")
        input("> ")


#Defines what mob you will find on an adventure
def mob():
    if night == False:
        animal = ['wolf', 'chicken', 'chicken', 'chicken', 'pig', 'pig', 'pig', 'cow',
    'cow', 'cow', 'sheep', 'sheep', 'sheep']

    else:
        animal = ['wolf', 'chicken', 'pig', 'cow'
    , 'sheep', 'zombie', 'zombie', 'skeleton', 'skeleton',
    'witch', 'slime', 'creeper', 'spider']

    mob = animal[random.randint(0, (len(animal)-1))]


    print(f"You run into a {mob}")
    fight_mob(mob)


def fight_mob(mob):
    global health
    select = 0
    wolf = ['wolf']
    friend = ['chicken', 'pig', 'cow', 'sheep']
    foe = ['zombie', 'skeleton', 'witch', 'spider', 'slime', 'creeper']

    if (mob) in friend:
        print(f"Would you like to kill the {mob} (y/n)")
        select = input("> ")
        if select == 'y':
            kill(mob)
        else:
            adventure()

    elif (mob) in wolf:
        print("You find a wolf!  Would you like to tame or kill it? (t/k)")
        select = input("")
        if select == 't':
            tame()

        else:
            print("You kill the wolf, giving you nothing")
            input("> ")

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


#['chicken', 'pig', 'cow', 'sheep]
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
        print(f"You kill the {mob}!")
        amount = random.randint(0,3)
        amount2 = random.randint(0,3)
        store('raw_beef', amount)
        store('leather', amount2)
        print(f"You get {amount} raw beef, and {amount2} leather")
        input("> ")
    

def a1():
    print("@@@@@      TEXTCRAFT     @@@@@")
#['zombie', 'skeleton','spider', 'witch', 'slime', 'creeper']
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
                print(f"The blows up hurting you {hurt} hp")
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

            if health <= 0:
                dead()
        
        if mob_health <= 0 and blow_up == False:
            print(f"The {mob} has fallen by your fist")##### {weapon}
            amount = random.randint(0,3)
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

            if health <= 0:
                dead()
        
        if mob_health <= 0:
            print(f"The {mob} has fallen by your fist")##### {weapon}
            amount = random.randint(0,3)
            print(f"You get {amount} string!")
            store('string', amount)
            input("> ")  
        

def dead():
    print("You die, game over")
    exit(0)


def view_inventory():
    x = 1
    z = 0
    for i in inventory:
        if i != None and i[1] != 0:
            print(f"#{x}", i[0], " - " ,i[1], end = " ")
            z += 1
            if z == 4:
                print("")
                z = 0
            x += 1
    input("> ")


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

# cook_output
def furnace():
    z = 0
    y = 0
    p = 0
    ape = 0
    quantity_unit = 0
    quantity_fuel = 0
    select_unit = 0
    select_fuel = 0
    can_cook = False
    have_fuel = False
    cook_list = []
    fuel_list = []
    for i in cook_output:
        cook_list.append(i[0])

    for i in inventory:
        if i[0] in cook_list and i[1] >= 1:
            can_cook = True
    for i in inventory:
        for x in fuel:
            if x[0] == i[0] and i[1] >= 1:
                have_fuel = True
                fuel_list.append(x[0])

    if can_cook == True and have_fuel == True:
        cookable = []
        print("What would you like to cook?")
        for i in inventory:
            if i[0] in cook_list:
                print(i[0], end = "   ")
                z += 1
                if z == 4:
                    print("")
                    z = 0
        print("")
        select_unit = input("> ")
        if select_unit in cook_list:
            print("What fuel would you like to use?")
            for i in fuel_list:
                print(i, end ="   ")
                y += 1
                if y == 4:
                    print("")
                    y = 0
            print("")
            select_fuel = input("> ")

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
                        if int(select) <= quantity_unit:
                            quantity_unit = int(select)
                            ape = 'q'

                        elif int(select) > quantity_unit:
                            print("You don't have that many dummy!")

                        elif int(select) > quantity_fuel:
                            print("Your fuel won't last that long")
                    
                        else:
                            furnace()
                            print("Learn to type a number!")

                    except ValueError:
                        print("Learn to type a number!")

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
                

                

            else:
                print("Not valid")
                

        else:
            print("Not valid")


        print("")
        input("> ")

    else:
        print("Cooks you can't")
        if can_cook == True:
            print("No fuel!")
        input("> ")



a4()
select = 0
while select != 'q':
    
    question = ("""What would you like to do?
(a)dventure
(c)raft
(d)ig down
(e)at
(i)nventory""")


    cls()

    clock += 1
    if clock == 40:
        night = True
        print("")
        print("The sun has fallen")
        print("")
    if clock == 80:
        night = False
        print("")
        print("The sun has risen")
        print("")
        clock = 0





    print('health ('+ (int(health/10)*2)*'@'+ ((-(int(health/10)-10))*2)*'-' + ')')

    print(question)
    for i in inventory:
        if i[0] == 'furnace':
            print("(f)urnace")
    print("(q)uit")

    select = input("> ")
    
    if select == 'i': # inventory
        view_inventory()
    
    elif select == 'a':# adventure()
        adventure()

    elif select == 'd':# dig_down()
        dig_down(height)

    elif select == 'c':# craft
        craft()
    
    elif select == 'f':# furnace
        furnace()
    
    elif select == 'e':# eat
        eat()

    elif select == 'q':
        choice = input("Are you sure you want to quit and lose your progress? (y/n)")
        if choice == 'y':
            print("BYEEEE")
        else:
            select = ''

    
    else:
        print("Try again")



