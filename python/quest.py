suc3 = int(input('몇 개의 3점슛을 성공시켰니?  '))
try3 = int(input('몇 번의 3점슛을 시도했니?  '))
def threeP(a, b):
    if(a > b):
        print('네가 시도한 3점슛보다 성공한 3점슛이 많을리 없어')
    else:
        return a/b
print(threeP(suc3, try3))