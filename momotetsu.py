from itertools import product #デカルト積用のライブラリ
def probability(n_dices, target): #n_dices:さいころの数、target:出したい目
    rolls = range(1, 6+1)  # サイコロの目の一覧 [1, 2, ..., sides]
    cnt = 0  # 和が target となる通り数
    for pip in product(rolls, repeat=n_dices):
        if(sum(pip) == target):
            cnt += 1
    return cnt
d_max = 6 * 8
card = {"通常":1, "急行":2,"特急":3,"新幹線":4,"のぞみ":5,"ロイヤル":6,"リニア":8}
min_d = input("最短の距離：")

if"," in min_d:
    min_d = min_d.split(",") #入力した数字を","で区切ってリストを生成
    
min_d = [int(n) for n in min_d] #int型に変換

loop = int(input("利用できるループのマス数："))
l_d = int(input("利用できるループと、最短ルートのマス数(片道)："))

Dists = []

for d in min_d:
    Dists.append(d)
    num = d + 2*l_d
    if loop == 0:
        pass
    else:
        while num <= 6*8:
            num += loop
            Dists.append(num)

Dists = list(set(Dists)) #Dists内の重複する数字を削除し、かつ昇順に並べる

for k, v in card.items(): #v:さいころをふる数
    values = 0
    for d in Dists: #d:出したい数
        value = probability(v, d)
        values += value
    result = values/(6**v)
    print(k,'{:.2%}'.format(result))