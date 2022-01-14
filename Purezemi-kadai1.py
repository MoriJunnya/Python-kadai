# for文を使い，１から100までの数字を表示する．
# ただし3の倍数のときは数字を表示せずに「勉強したい」と表示，
# 5の倍数のときは「就活したい」と表示，
# 3の倍数かつ5の倍数のときは「だいがく爆破したい」と表示するプログラム
for num in range(1, 101):           #1以上101未満の数字を1ずつ増やしながら回す
    if num % 15 == 0:               #3と5の公倍数は3*5=15.つまり15の倍数
        print("だいがく爆発したい")  #最初のif節が実行されたところで条件が成立してif文が終了してしまうため
    elif num % 3 == 0:              #15を最初に条件付ける
        print("勉強したい")          #elif = else if
    elif num % 5 == 0:
        print("就活したい")
    else: print(num)                #elseはすべての条件が成立しなかったときに実行する