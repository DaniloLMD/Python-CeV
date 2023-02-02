from operator import itemgetter
dic = {'1': 0, '2': 1, '3': 2}
print(sorted(dic.items(), key=itemgetter(1), reverse=True))