import os
import sys
import gc
import random


class Hero:

    def __init__(self, Hero_id, name, attack, skill, prop):
        self.Hero_id = Hero_id
        self.name = name
        self.attack = attack
        self.skill = skill
        self.prop = prop

    def show_detail(self):
        return '{0:<3}:{1}\t 攻擊力:{2}\t 技能:{3}'.format(self.Hero_id, self.name, self.attack, self.skill)


hero1 = Hero(1, '戰士', 100, '一定機率傷害增加至150。', '弱化')
hero2 = Hero(2, '聖騎士', 60, '讓一名前排隊友傷害減半。', '弱化')
hero3 = Hero(3, '弓箭手', 125, '隊友攻擊目標時，對目標攻擊25傷害。', '弱化')
hero4 = Hero(4, '醫師', 60, '回復我方生命155。', '弱化')
hero5 = Hero(5, '販毒家', 70, '3回含內對對手造成傷害50。', '弱化')
hero6 = Hero(6, '舞者', 85, '增加我方另外2名隊友攻擊力1.5倍。', '弱化')
hero7 = Hero(7, '爆咒師', 210, '(負面技能)攻擊一名後排對手英雄時，自身減少90HP。', '弱化')
hero8 = Hero(8, '咒術師', 120, '隨機禁止一名對手英雄發動技能。', '弱化')
hero9 = Hero(9, '研術者', 100, '降低一名對手英雄30%傷害。', '弱化')
hero10 = Hero(10, '祭師', 130, '吸取對手40HP血。', '弱化')
hero11 = Hero(11, '魔人', 80, '一定機率回避對手英雄1次傷害。', '弱化')
hero12 = Hero(12, '武士', 110, '隨機必定攻擊2名對手英雄。', '弱化')
hero13 = Hero(13, '護衛', 60, '一定機率主動承受傷害並無效化。', '弱化')
hero14 = Hero(14, '法師', 130, '(例外)只可攻擊後排成員。', '弱化')
hero15 = Hero(15, '念力師', 110, '一定機率該回合沒有弱點角色。', '弱化')
hero16 = Hero(16, '學者', 30, '一名後排成員被攻擊時，回復傷害攻擊值的70%HP。', '弱化')
hero17 = Hero(17, '占卜師', 50, '當猜中對手弱點角色，回復傷害攻擊值60%HP。', '弱化')
hero18 = Hero(18, '小丑', 50, '指定一名隊友，當他是後排並受攻擊，攻擊者受自身傷害。', '弱化')
hero19 = Hero(19, '交際花', 90, '當弱點角色被攻擊時，自己前排角色受到傷害下降25%。', '弱化')
hero20 = Hero(20, '獵人', 55, '對同一名對手英雄攻擊隨機1~5次。', '弱化')


# for obj in gc.get_objects():
#    if isinstance(obj, Hero):
#        print(obj.name)

hero_list = [
    hero1, hero2, hero3, hero4, hero5, hero6, hero7, hero8, hero9, hero10,
    hero11, hero12, hero13, hero14, hero15, hero16, hero17, hero18, hero19, hero20]

player1_hero = []
# player1_hero_name = []
front = []
behind = []


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


def packing_Hero():
    for hero in hero_list:
        print(Hero.show_detail(hero))
    print('請選擇5位角色')
    while len(player1_hero) < 5:
        chioce = int(input())
        # print(' This is OK')
        if chioce < 1 or chioce > 20:
            print('請輸入1至20')
            continue
        if chioce in player1_hero:
            print('不能重複選擇角色，請重新選擇!')
            continue
        else:
            player1_hero.append(hero_list[int(chioce) - 1])
            # player1_hero_name.append(hero_list[int(chioce) - 1].name)
            print('你選擇了' + hero_list[int(chioce) - 1].name)
            # print(player1_hero_name)
            print(player1_hero.name)
    position()


def position():
    print('===' * 25)
    print('戰鬥開始')
    for i in player1_hero:
        print(Hero.show_detail(i))
    sick = random.randint(0, 4)
    print(sick)
    print(type(sick))  # int
    # 宣告
    print('你的弱化角色為' + str(player1_hero[sick].name))
    print('弱化角色不能在後排,請安排另外兩位前例角色。')
    player1_hero.remove(player1_hero[sick])
    print(player1_hero.name)
    for infront in range(2):
        print('請输入1-' + str(int(5 - infront)))
        infront_hero = input()
        player1_hero.remove(infront_hero)
        print(player1_hero)
    print('OK')


def start():
    print('===' * 25)
    print('option 11 OK')
    packing_Hero()


menu()
