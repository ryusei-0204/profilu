# ヌメロンをやりたい
# 3桁の重複しない数を産出する
print("ヌメロンゲームです")
print("数を当てゲームです")
print("ルール")
print("イート＝桁も数もあっている")
print("バイト＝数字はあるが桁が間違っている")


import time
import random
import math
a=0
b=0
c=0
count=0
while (a == b or a == c or b == c) :
  a=random.randint(0,9)
  b=random.randint(0,9)
  c=random.randint(0,9)
bot=[int(a),int(b),int(c)]
# print(bot)


class bite_et:

  def e_t (self):
    global eat
    eat=0
    if anser[0] == bot[0] :
      eat+=1
    if anser[1] == bot[1]:
      eat+=1
    if anser[2] == bot[2]:
      eat+=1  
    # print(str(eat)+"イートです")
  
  def bite(self):
    bite=0
    if bot[0] == anser[1] or bot[0] == anser[2]:
      bite+=1
    if bot[1] == anser[2] or bot[1] == anser[0]:
      bite+=1
    if bot[2] == anser[0] or bot[2] == anser[1]:
      bite+=1
    print(str(bite)+"バイトです")



# プレイイヤーがルールにのっとり数字を入力
print("数を当ててください")
anser=input("0~9の重複しない3桁の数を入力してください:")
anser_len=len(anser)
count+=1
# anser_lenをもう一度定義しなければならない
#andにすると3桁かつ重複しない数値の時繰り返すになる
#そのためanser_lenが３のときで重複してた場合繰り返さない
while ( anser_len!=3 or anser[0] == anser[1] or anser[0] == anser[2] or anser[1]==anser[2]):
  print("ルールに従ってください")
  anser=input("0~9の重複しない3桁の数を入力してください:")
  anser_len=len(anser)
  count+=1
anser=[int(anser[0]),int(anser[1]),int(anser[2])]
  
# player_count=[int(anser[0]),int(anser[1]),int(anser[2])]
ryusei=bite_et()
# ryusei.bitebite()
ryusei.e_t()

if eat == 3:
  print("正解です")
else:
  while ( eat!=3):
    ryusei.bite()
    ryusei.e_t()
    print(str(eat)+"イートです")
    anser=input("0~9の重複しない3桁の数を入力してください:")
    anser_len=len(anser)
    anser=[int(anser[0]),int(anser[1]),int(anser[2])]
    count+=1
    ryusei.e_t()
    if eat==3:
      print("正解です")

if eat==3:
  print(str(count)+"回目で当たりました")

  time.sleep(10)











