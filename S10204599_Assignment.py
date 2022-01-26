#Ng Lynn Shaan P05 S10204599

#Ratventure

#import
import json
import random

#score list
score=[]
topscore={'score':0}

#display menu
print("""Welcome to Ratventure
------------------
1) New Game
2) Resume Game
3) Exit Game """)
display_choice=int(input("Enter choice: "))
print()

#town menu
town_menu="""1) View Character
2) View Map
3) Move
4) Rest
5) Save Game
6) Exit Game """

#outdoor menu
outdoor_menu="""1) View Character
2) View Map
3) Move
4) Sense Orb
5) Exit Game """

#combat menu
combatmenu="""1) Attack
2) Run"""

#map data
world_map = [['H/T', '   ', '   ', '   ', '   ', '   ', '   ', '   '],\
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],\
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],\
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],\
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],\
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],\
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],\
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', ' K ']]

#separator for printing
separator = '+---+---+---+---+---+---+---+---+\n'

#the orb will be displayed in the hidden map but not printed in the world map
hidden_map = [[' T ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],\
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],\
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],\
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],\
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],\
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],\
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],\
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', ' K ']]

#player statistics
found=False
player={"name":"The Hero", "damage": "2-4","defence":1,"hp":20,"location":[0,0],'day':1, 'orb':found, "mindamage":2,'maxdamage':4}

#rat statistics
rat={"name":'Rat', "damage": "1-3","defence":1,"hp":10,"mindamage":1,'maxdamage':3}

#rat king statistics
ratking={"name":'Rat King', "damage": "8-12","defence":5,"hp":25,'mindamage':6,'maxdamage':10}

#function to print the formatted map
def map():
    gridline=''
    gridline+=separator
    for i in range(8):
        gridline+='|'+'|'.join(world_map[i])+'|\n'
        gridline+=separator
    print(gridline)

#function for randomization of orb location
def orblocation():
    orbx=random.randint(4,7)
    orby=random.randint(4,7)
    #check if randomized location is empty
    if world_map[orbx][orby]=='   ':
        hidden_map[orbx][orby]=' O '
    #if randomized location occupied, coordinates randomized again 
    else:
        orblocation()

#function for randomization of town location
def randomization():
    #town count to ensure total of 4 towns
    towncount=0
    while towncount<4:
        rxcoord=random.randint(0,7)
        rycoord=random.randint(0,7)
        town=True
        for rx in range (-2,3):
            #to ensure list index in range
            begin=abs(rx)-2
            end=abs(begin)
            #to check whether the surrounding area is empty
            for ry in range (begin,end+1):
                if 7 >= (rxcoord+rx) >=0 and 7 >= (rycoord+ry) >=0 and world_map[rxcoord+rx][rycoord+ry] != "   ":
                    town=False
        if town==True:
            towncount+=1
            world_map[rxcoord][rycoord]=' T '
    orblocation()

#function to view character
def view_chara():
    print()
    print(player['name'])
    print("Damage:",player['damage'])
    print("Defence:",player['defence'])
    print("HP:",player['hp'])
    if player['orb']==True:
        print("You are holding the Orb of Power.")
    print()

#function to save game
def save_data():
    player_data={'map_data':world_map, 'player_stats':player, 'ratKingstats':ratking}
    savefile=open('savefile.json','w')
    savefile.write(json.dumps(player_data))
    savefile.close()

#function to load game
def load_data():
    #check if save file exists
    try:
        global world_map,player,ratking
        savefile=open('savefile.json','r')
        player_data=json.loads(savefile.read())
        world_map=player_data['map_data']
        player=player_data['player_stats']
        ratking=player_data['ratKingstats']

    except FileNotFoundError:
        print("File not found.")
        print("""
1) New Game
2) Resume Game
3) Exit Game """)
        display_choice=int(input("Enter choice: "))
        print()
        #validation
        while display_choice!=-1:
            #new game
            if display_choice==1:
                player['name']=input("Enter name: ")
                print()
                randomization()
                town_actions()
            #resume game
            if display_choice==2:
                load_data()
                town_actions()     
            #exit game 
            if display_choice==3:
                exitGame()
            #invalid choice
            if display_choice!=1 and display_choice!=2 and display_choice!=3:
                print("Invalid choice")
                display_choice=int(input("Enter choice: "))
                print()

#function to exit game
def exitGame():
    print("Exiting...")
    exit()

#player death function
def death():
    print("You died! Try again?")
    print("""1) Try again
2) Exit game """)
    dchoice=int(input("Enter choice: "))
    print()
    #validation
    while dchoice!=-1:
        #load from last save
        if dchoice==1:
            load_data()
            town_actions()
        #exit game
        if dchoice==2:
            exitGame()
        #invalid choice
        if dchoice!=1 and dchoice!=2:
            print("Invalid choice")
            print("""1) Try again
2) Exit game """)
            dchoice=int(input("Enter choice: "))
        print()

#function to save score
def recordScore():
    global topscore, score
    score=[player['name'],player['day']]
    topscore['score']=(score)
    winrecord=open('winrecord.json','w')
    winrecord.write(json.dumps(topscore))
    winrecord.close()
    exitGame()

#function to load score
def loadScores():
    global topscore,score
    winrecord=open('winrecord.json','r')
    topscore=json.loads(winrecord.read())
    score=topscore['score']
    winrecord.close()
    
#move function
def move():
    print("W = up; A = left; S = down; D = right")
    move=input("Your move: ")
    print()
    #validation
    while move!=-1:
        global x,y
        x=player['location'][0]
        y=player['location'][1]
        #removing old location
        if world_map[x][y]==' H ':
            world_map[x][y]='   '
        if world_map[x][y]=='H/T':
            world_map[x][y]=' T '
        if world_map[x][y]=='H/K':
            world_map[x][y]=' K '
        if move=='w' or move=='a' or move=='s' or move=='d':
            #update coordinates
            if move=='w':
                x=x-1
            if move=='a':
                y=y-1
            if move=='s':
                x+=1
            if move=='d':
                y+=1
            if x<0 or y<0 or x>7 or y>7:
                print("You cannot move out of the map")
                move=input("Your move: ")
                print()
            if 7>=x>=0 and 7>=y>=0:
                player['day'] +=1
                player['location'][0]=x
                player['location'][1]=y
                #outdoor combat
                if world_map[x][y]=='   ':
                    world_map[x][y]=' H '
                    print("Day",player['day'],": You are out in the open.")
                    ratcounter()  
                    #attack
                    if player['hp']==0:
                        death()
                    if rat['hp']==0:
                        print("The Rat is dead! You are victorious!")
                        print()
                        outdoor_actions()
                #in town
                if world_map[x][y]==' T ':
                    world_map[x][y]='H/T'
                    town_actions()
                #rat king
                if world_map[x][y]==' K ':
                    world_map[x][y]='H/K'
                    print("Day",player['day'],": You see the Rat King.")
                    rat_king()
                    if player['hp']==0:
                        death()
                break
        else:
            #invalid move
            print("Invalid move")
            move=input("Your move: ")
            print()

#orb function
def sense_orb():
    #check orb location
    for i in hidden_map:
        if " O " in i:
            global found
            #orb coordinates
            ox=hidden_map.index(i)
            oy=i.index(' O ')
            #found orb
            if ox==x and oy==y:
                print()
                print("""You found the orb of power
Your attack increases by 5!
Your defence increases by 5!""")
                player['defence']+=5
                player['damage']='7-9'
                player['mindamage']+=5
                player['maxdamage']+=5
                found=True
                player['orb']=found
            #orb direction
            else:
                if ox<x and oy==y:
                    direction="north"
                if ox<x and oy<y:
                    direction="north-west"
                if ox<x and oy>y:
                    direction="north-east"
                if ox>x and oy==y:
                    direction="south"
                if ox>x and oy<y:
                    direction="south-west"
                if ox>x and oy>y:
                    direction="south-east"
                if ox==x and oy<y:
                    direction="west"
                if ox==x and oy>y:
                    direction="east"
                print("You sense that the Orb of Power is to the {}.".format(direction))
                print()

#rat attack function
def attack():
    import random
    while rat['hp']!=0 and player['hp']!=0:
        #random damage
        damdealt=random.randint(player['mindamage'],player['maxdamage'])
        rdamdealt=random.randint(rat['mindamage'],rat['maxdamage'])
        #damage taken by plaver
        if player['defence']<rdamdealt:
            rdd=rdamdealt-player['defence']
            player['hp']=player['hp']-rdd
        #no damage
        if player['defence']>rdamdealt:
            rdd=0
        print("You deal",damdealt,"damage to the Rat.")
        #damage dealt to the rat
        rat['hp']=rat['hp']-(damdealt-rat['defence'])
        if damdealt>rat['hp']:
            damdealt=rat['hp']
        print("Ouch! The Rat hit you for",rdamdealt,"damage!")
        #player death
        if rdamdealt>player['hp']:
            rdamdealt=player['hp']
        if player['hp']<0:
            player['hp']=0
        print("You have",player['hp'] ,"HP left.")
        if rat['hp']<0:
            rat['hp']=0
        print("Encounter! - Rat")
        print("""Damage: 1-3
        Defence: 1
        HP=""",rat['hp'])
        #rat death
        if player['hp']==0:
            break
        #continue combat
        if rat['hp']!=0:
            print()
            print(combatmenu)
            combat_choice=int(input("Enter choice: "))
            print()
            #run
            if combat_choice==2:
                print(outdoor_menu)
                outdoor_choice=int(input("Enter choice: "))
                print()
                while outdoor_choice!=-1:
                    #get attacked again
                    if outdoor_choice==1 or outdoor_choice==2 or outdoor_choice==4:
                        ratcounter()
                    #move
                    if outdoor_choice==3:
                        map()
                        move()
                    #exit    
                    if outdoor_choice==5:
                        exitGame()
                    #invalid
                    if outdoor_choice!=1 and outdoor_choice!=2 and outdoor_choice!=3 and outdoor_choice!=4 and outdoor_choice!=5:
                        print("Invalid choice")
                        print(outdoor_menu)
                        outdoor_choice=int(input("Enter choice: "))
                        print()
        if rat['hp']==0:
            break

#rat encounter function
def ratcounter():
    rat['hp']=10
    print("Encounter! - Rat")
    print("""Damage: 1-3
    Defence: 1
    HP=""",rat['hp'])
    print()
    print(combatmenu)
    combat_choice=int(input("Enter choice: "))
    print()
    #validation
    while combat_choice!=-1:
        #attack
        if combat_choice==1:
            attack()   
            break
        #run
        if combat_choice==2:
            print(outdoor_menu)
            outdoor_choice=int(input("Enter choice: "))
            print()
            #if player does not move away player will get attacked again
            if outdoor_choice==1 or outdoor_choice==2 or outdoor_choice==4:
                ratcounter()
            #move
            if outdoor_choice==3:
                map()
                move()
            #exit    
            if outdoor_choice==5:
                exitGame()
            #invalid
            if outdoor_choice!=1 and outdoor_choice!=2 and outdoor_choice!=3 and outdoor_choice!=4 and outdoor_choice!=5:
                print("Invalid choice")
                print(outdoor_menu)
                outdoor_choice=int(input("Enter choice: "))
                print()
            break
        #invalid
        if combat_choice!=1 and combat_choice!=2:
            print("Invalid choice")
            print(combatmenu)
            combat_choice=int(input("Enter choice: "))
            print()

#rat king combat
def rat_king():
    import random
    print("""Encounter! - Rat King 
    Damage: 6-10
    Defence: 5
    HP: """,ratking['hp'])
    print()
    print(combatmenu)
    combat_choice=int(input("Enter choice: "))
    print()
    #validation
    while combat_choice!=-1:
        if combat_choice==1:
            while ratking['hp']!=0 and player['hp']!=0:
                #damage dealt by the rat king
                rkdamdealt=random.randint(ratking['mindamage'],ratking['maxdamage'])
                #if player does not have orb, no damage is inflicted
                if player['orb']==False:
                    print("You do not have the Orb of Power - The Rat King is immune!")
                    damdealt=0
                if player['orb']==True:
                    #damage dealt by the player
                    damdealt=random.randint(player['mindamage'],player['maxdamage'])
                    #damage taken by the rat king
                    if ratking['defence']<damdealt:
                        pdd=damdealt-ratking['defence']
                    #if damage done is lower than rat king defence, no damage is taken
                    if ratking['defence']>damdealt:
                        pdd=0
                print("You deal",damdealt,"damage to the Rat King.")
                #rat king hp after damage taken
                ratking['hp']=ratking['hp']-pdd
                #if damage taken more than rat king hp, rat king hp = 0
                if pdd>ratking['hp']:
                    pdd=ratking['hp']
                print("Ouch! The Rat King hit you for",rkdamdealt,"damage!")
                #damage taken by the player
                if player['defence']<rkdamdealt:
                    rkdd=rkdamdealt-player['defence']
                    #player hp if damaged
                    player['hp']=player['hp']-rkdd
                #if player defence higher than damage done by rat king, no damage is taken
                if player['defence']>rkdamdealt:
                    rkdd=0
                #if damage done by rat king is higher than player hp, player hp = 0
                if rkdamdealt>player['hp']:
                    rkdamdealt=player['hp']
                #player hp cannot be negative
                if player['hp']<0:
                    player['hp']=0
                print("You have",player['hp'] ,"HP left.")
                #rat king hp cannot be negative
                if ratking['hp']<0:
                    ratking['hp']=0
                print("Encounter! - The Rat King")
                print("""Damage: 1-3
                Defence: 1
                HP=""",ratking['hp'])
                if player['hp']==0:
                    break
                #continue combat
                if ratking['hp']!=0:
                    print()
                    print(combatmenu)
                    combat_choice=int(input("Enter choice: "))
                    #run
                    if combat_choice==2:
                        break
                    print()
                if ratking['hp']==0:
                    print("""The Rat King is dead! You are victorious!
Congratulations, you have defeated the Rat King!
The world is saved! You win!
""")                    
                    recordScore()
                    exitGame()
                    break
        #run 
        if combat_choice==2:
            print(outdoor_menu)
            outdoor_choice=int(input("Enter choice: "))
            print()
            #if player does not move away, player will be attacked by rat king again
            if outdoor_choice==1 or outdoor_choice==2 or outdoor_choice==4:
                rat_king()
            #move
            if outdoor_choice==3:
                map()
                move()    
            #exit game
            if outdoor_choice==5:
                exitGame()
            #invalid choice
            if outdoor_choice!=1 and outdoor_choice!=2 and outdoor_choice!=3 and outdoor_choice!=4 and outdoor_choice!=5:
                print("Invalid choice")
                print(outdoor_menu)
                outdoor_choice=int(input("Enter choice: "))
                print()     
        #invalid choice   
        if combat_choice!=1 and combat_choice!=2:
            print("Invalid choice")
            print(combatmenu)
            combat_choice=int(input("Enter choice: "))
            print()


#town actions function
def town_actions():
    global day
    print("Day", player['day'],": You are in a town")
    print(town_menu)
    town_choice=int(input("Enter choice: "))
    print()
    #display character
    if town_choice==1:
        view_chara()
        town_actions()
    #display starting map
    if town_choice==2:
        map()
        town_actions()
    #move
    if town_choice==3:
        map()
        move()
    #rest
    if town_choice==4:
        player['day']+=1
        player['hp']=20
        print("You are fully healed.")
        town_actions()
    #save game
    if town_choice==5:
        print("Game saved")
        print()
        save_data()
        town_actions()
    #exit game
    if town_choice==6:
        exitGame()

#outdoor actions
def outdoor_actions():
    print(outdoor_menu)
    outdoor_choice=int(input("Enter choice: "))
    print()
    #validation
    while outdoor_choice!=-1:
        #character
        if outdoor_choice==1 or outdoor_choice==2 or outdoor_choice==4: 
            if outdoor_choice==1:
                view_chara()
            if outdoor_choice==2:
                map()
            if outdoor_choice==4:
                sense_orb()
            print(outdoor_menu)
            outdoor_choice=int(input("Enter choice: "))
        #move
        if outdoor_choice==3:
            map()
            move()
            x=player['location'][0]
            y=player['location'][1]
        #exit game
        if outdoor_choice==5:
            exitGame()
            break
        #invalid choice
        if outdoor_choice!=1 and outdoor_choice!=2 and outdoor_choice!=3 and outdoor_choice!=4 and outdoor_choice!=5:
                print("Invalid choice")
                print(outdoor_menu)
                outdoor_choice=int(input("Enter choice: "))
                print()

#main menu
while display_choice!=-1:
    #new game
    if display_choice==1:
        player['name']=input("Enter name: ")
        print()
        randomization()
        town_actions()
    #resume game
    if display_choice==2:
        load_data()
        town_actions()     
    #exit game 
    if display_choice==3:
        exitGame()
    #invalid
    if display_choice!=1 and display_choice!=2 and display_choice!=3:
        print("Invalid choice")
        display_choice=int(input("Enter choice: "))
        print()

