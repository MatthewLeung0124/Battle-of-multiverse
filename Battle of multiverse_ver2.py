import os
import sys
import gc
import random
import time

class Hero:

    def __init__(self, Hero_id, name, attack, skill):
        self.Hero_id = Hero_id
        self.name = name
        self.attack = attack
        self.skill = skill

    def show_player1_GorupList(self):
        print('你的選擇:')  
        for no_member in player1_hero:
            print(no_member.name,end=' ')
                         
    def show_computer_GorupList(self):
        print('電腦選擇:')
        for no_member in computer_hero:
            print(no_member.name,end=' ')
    
    def show_sick_Character(self):
        print(self.name)

    def show_Charater_sorted(self):
        return '  :{0:<3}\t 攻擊力:{1}\t 技能:{2}'.format( self.name, self.attack, self.skill) 

    def show_detail(self):
        return '{0:<3}:{1:<3}\t 攻擊力:{2}\t 技能:{3}'.format(self.Hero_id, self.name, self.attack, self.skill)

hero1 = Hero(1, '戰士', 100, '一定機率傷害增加至150。')
hero2 = Hero(2, '聖騎士', 60, '讓一名前排隊友傷害減半。')
hero3 = Hero(3, '弓箭手', 125, '隊友攻擊目標時，對目標攻擊25傷害。')
hero4 = Hero(4, '醫師', 60, '回復我方生命155。')
hero5 = Hero(5, '販毒家', 70, '3回含內對對手造成傷害50。')
hero6 = Hero(6, '舞者', 85, '增加我方另外2名隊友攻擊力1.5倍。')
hero7 = Hero(7, '爆咒師', 210, '(負面技能)攻擊一名後排對手英雄時，自身減少90HP。')
hero8 = Hero(8, '咒術師', 120, '隨機禁止一名對手英雄發動技能。')
hero9 = Hero(9, '研術者', 100, '降低一名對手英雄30%傷害。')
hero10 = Hero(10, '祭師', 130, '吸取對手40HP血。')
hero11 = Hero(11, '魔人', 80, '一定機率回避對手英雄1次傷害。')
hero12 = Hero(12, '武士', 110, '隨機必定攻擊2名對手英雄。')
hero13 = Hero(13, '護衛', 60, '一定機率主動承受傷害並無效化。')
hero14 = Hero(14, '法師', 130, '(例外)只可攻擊後排成員。')
hero15 = Hero(15, '念力師', 110, '一定機率該回合沒有弱點角色。')
hero16 = Hero(16, '學者', 30, '一名後排成員被攻擊時，回復傷害攻擊值的70%HP。')
hero17 = Hero(17, '占卜師', 50, '當猜中對手弱點角色，回復傷害攻擊值60%HP。')
hero18 = Hero(18, '小丑', 50, '指定一名隊友，當他是後排並受攻擊，攻擊者受自身傷害。')
hero19 = Hero(19, '交際花', 90, '當弱點角色被攻擊時，自己前排角色受到傷害下降25%。')
hero20 = Hero(20, '獵人', 55, '對同一名對手英雄攻擊隨機1~5次。')

hero_list = [
    hero1, hero2, hero3, hero4, hero5, hero6, hero7, hero8, hero9, hero10,
    hero11, hero12, hero13, hero14, hero15, hero16, hero17, hero18, hero19, hero20]

player1_hero = []
player1_front = []
player1_behind = []
player1_sick_Charater = []
player1_hp = 1000

computer_hero = []
computer_front = []
computer_behind = []
compyter_sick_Charater = []
compyter_hp = 1000

def menu():
    print('===' * 25)
    print('Battle of multiverse\n')
    print('1.開始')
    print('2.角色技能')
    print('3.遊戲玩法')
    print('4.背景故事')
    print('5.離開')
    print('請輸入數字')
    print('\n遊戲玩法參考\"世界樹迷宮\"')
    option = int(input())
    if(option == 1):
        print('option 1 OK')
        start()
    elif(option == 2):
        print('option 2 OK')
        # characters_detail()
    elif(option == 3):
        print('option 3 OK')
        # How_to_play()
    elif(option == 4):
        print('option 4 OK')
        # background_Story()
    elif(option == 5):
        print('option 5 OK')
        sys.exit()
    else:
        print('輸入錯誤')
        menu()

def start():
    print('===' * 25)
    print('option 11 OK')
    packing_Hero()

def packing_Hero():
    for hero in hero_list:
        print(Hero.show_detail(hero))
    print('請選擇5位角色')
    while len(player1_hero) < 5:
        skip = False
        if len(player1_hero) > 0 and skip == True:        
            print()
        chioce = int(input())
        skip = True
        # print(' This is OK')
        if chioce == 0:
            for hero in hero_list:
                print(Hero.show_detail(hero))
            print('請選擇角色!')
            print(Hero.show_player1_GorupList(player1_hero))
            print()
        elif chioce < 1 or chioce > 20:
            print('請輸入0至20!  按0查看角色例表')
            continue          
        elif hero_list[int(chioce - 1)] in player1_hero:
            skip = False
            print('不能重複選擇角色，請重新選擇!  按0查看角色例表')
            continue
        else:
            #chiocelist.append(chioce)
            player1_hero.insert(-1,hero_list[int(chioce) - 1])
            player1_hero.sort(key = lambda x: x.Hero_id)
            #chiocelist.sort()
            print('你選擇了' + hero_list[int(chioce) - 1].name + '  按0查看角色例表') #LIST.NAME
            Hero.show_player1_GorupList(player1_hero)
            #print(player1_hero)
            #print(chiocelist)
            print()
    
def computer_packing_Hero():
    while len(computer_hero) < 5:
        computer_pick = random.randint(1,20)
        if hero_list[int(computer_pick - 1)] in computer_hero:
            continue
        else:
            computer_hero.insert(-1,hero_list[int(computer_pick) - 1])
            computer_hero.sort(key = lambda x: x.Hero_id)
    print('請等候，電腦選擇中')
    time.sleep(3.0)
    Hero.show_computer_GorupList(computer_hero)
    time.sleep(2.0)
    print()
    show_bothside()

def show_bothside():
    print()
    print('我方角色')
    for index, hero in enumerate(player1_hero):
        print(str(index + 1) + Hero.show_Charater_sorted(hero))
    print()
    print('敵方角色')
    for index, hero in enumerate(computer_hero):
        print(str(index + 1) + Hero.show_Charater_sorted(hero))
    print()
    print('按鍵繼續Enter')
    space = input()
    print()
    show_sick()

def show_sick():
    sick = random.randint(1, 6)
    print(sick)
    print('你的弱化角色為' + str(player1_hero[int(sick - 1)].name))
    print('弱化角色不能在後排,請安排另外兩位前例角色。')
    player1_sick_Charater.insert(-1,player1_hero[int(sick - 1)])
    
menu()
computer_packing_Hero()

