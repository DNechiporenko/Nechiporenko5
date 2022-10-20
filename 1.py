import random
def massiv(s,arr):
    for x in range(s):
        arr.append(random.randint(0,100))
amount1=int(input("Введите размерность первого массива: "))
amount2=int(input("Введите размерность второго массива: "))
arra=[]
arrb=[]
massiv(amount1,arra)
massiv(amount2,arrb)
otvet=[]
print("Общие элементы массивов:")
for m in (arra):
    if m in arrb:
        otvet.append(m)
print(otvet)
print("Если числа не появились на экране, значит общих элементов нет")
