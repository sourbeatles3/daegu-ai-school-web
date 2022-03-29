시도 = int(input('몇 개의 슛을 시도했니?  '))
성공 = int(input('몇 개의 슛을 성공했니?  '))
성공률 = (성공/시도) * 100
def shot(a, b):
    if(시도 >= 성공):
        print(f'네 슛 성공률은 {성공률}%구나')
    else:
        print('네가 시도한 슛보다 많이 성공했을리가 없어')
print(shot(시도, 성공))