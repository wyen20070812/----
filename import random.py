import random
import time

class Player:
    bullet = 6
    true = True
    def __init__(self,name):
        self.name = name

n=int(input("人数"))
player=["0"]*n
card=[[] for i in range(n)]
total_card = ['j','j','j','j','q','q','q','q','k','k','k','k','wang','wang']
for i in range(n):
    player[i]=Player(input("Enter your name:"))
playerset=set(player)
player = list(playerset)
print(f"huihewei{[play.name for play in player]})")
flag=1
aft0=0
def new_turn(aft3):
    zhu=random.choice(['j','q','k'])
    print(f"主牌{zhu}")
    input()
    total_card2=total_card[:]
    random.shuffle(total_card2)
    for num_play in range(n):
        card[num_play]=[]
        for i in range(int(14/n)):
            card[num_play].append(total_card2.pop())
    turn(aft3,zhu)

def turn(play,zhu):
    if play>=n-1:
        aft = 0
    else:
        aft = play+1

    print(f"主牌{zhu}")
    print(f"{player[play].name}的回合。 your card:{card[play]}")
    print("which do you want throw?")
    discard=input().split()
    for c in discard:
        if c!=zhu and c!= 'wang':
            player[play].true=False
        if c not in total_card or c not in discard:
            print("again")
            turn(play,zhu)
            break
        card[play].remove(c)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(f"{player[aft].name}小心, {player[play].name}出{len(discard)}张，他还{len(card[play])}张，你要质疑吗")
    if int(input())==1:
        check_play(play,aft,player[play].true)
    elif len(card[play])==0:
        print("你必须质疑")
        check_play(play,aft,player[play].true)
    else:
        play=aft
        turn(play,zhu)


def check_play(play1,aft1,playtrue):
    global n,player
    if playtrue==1:
        print(f"{player[play1].name}是真的")
        for i in range(3,0,-1):
            print(i)
            time.sleep(1)
        if random.randint(0,player[aft1].bullet)==0:
            print(f"{player[aft1].name} you die")
            n-=1
            player.remove(player[aft1])
            card[play1].remove([aft1])
            is_win(play1)
        else:
            player[aft1].bullet-=1
            print(f"你还有{player[aft1].bullet}发子弹")
            new_turn(aft1)
    else:
        print(f"{player[play1].name}是假的")
        for i in range(3,0,-1):
            print(i)
            time.sleep(1)
        if random.randint(0,player[play1].bullet)==0:
            print(f"{player[play1].name} you die")
            n-=1
            player.remove(player[play1])
            card.remove(card[play1])
            is_win(aft1)
        else:
            player[play1].bullet-=1
            print(f"你还有{player[play1].bullet}发子弹")
            new_turn(aft1)
def is_win(aft2):
    if n==1:
        print(f"{player[0].name} you win")
        flag=0
    else:
        new_turn(aft2)

while flag:
    new_turn(aft0)