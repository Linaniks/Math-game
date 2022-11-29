print ("Привет! Вы зашли в игру. Укажите ваше имя")
first_name = input ()
print ("Добро пожаловать,", first_name, ", Хотите начать? Укажите: \"да/нет\"")
while True:
    answer = input ()
    if answer == 'нет':
        print ("Подумайте ещё... Теперь вы хотите начать?")
    elif answer == 'да':
        break
    else:
        print ("Подумайте ещё... Теперь вы хотите начать?")

print ("Замечательно!")
print ("Загадай двухзначное число, а я разделю его на 2")

while True:
    number = input()
    try:
        number = int (number)
        if number >= 10 and number <= 99:
            break
        else:
            print ('Вы ввели не двухзначное число. Попробуйте ещё раз')
    except ValueError:
        test = number.isalpha()
        if test==True:
            print ("Вы ввели буквенные символы. Введите 2х-значное число")
        else:
            print ("Вы ввели не 2х-значное число. Попробуйте ещё раз")

ix = number/2
print ("Ответ будет ", ix, "Теперь твоя очередь! Сколько будет ", ix, "-3.1?")

while True:
    ygrek = input()
    try:
        ygrek = float (ygrek)
        if (ix - 3.1) == ygrek:
            break
        else:
            print ("В ответе ошибка. Ничего страшного, решите пример ещё раз")
    except ValueError:
        test = ygrek.isalpha()
        if test==True:
            print (f"Вы ввели буквенные символы. Нужно ввести ответ {ix} - 3.1")
        else:
            print ("Вы ввели не число. Попробуйте ещё раз!")

while True:
    ygrek = float(ygrek)
    if (ix - 3.1) == ygrek:
        break
    else:
        print ("В ответе ошибка. Ничего страшного, решите пример ещё раз")
        
print ("Ваш ответ - ", ygrek, "Молодец!")
print ("Давай теперь возьмёмся за более сложные числа? Укажите: \"да/нет\" ")

while True:
    answer_2 = input ()
    if answer_2 == 'нет':
            print ("Вы уверенны?... Введите ваш ответ ещё раз")
    elif answer_2 == 'да':
        break
    else:
        print ("Вы уверенны?... Введите ваш ответ ещё раз")

rex3 = (ygrek+100)//1
rex4 = ygrek*1000
print ("Тогда я даю тебе два числа!", rex3, "и", rex4, "Возьми одно из чисел, которое меньше 200 и вычти из него 100. А я скажу сколько в нём десятков и едениц")

while True:
    xerx = input ("Введи ответ ")
    try:
        xerx = int (xerx)
        if (rex3 - 100) == xerx:
            break
        else:
            print ("Вы решили пример не верно. Попробуйте ещё раз")
    except ValueError:
        test_1 = xerx.isalpha()
        if (test_1==True):
            print (f"Вы ввели буквенные символы. Нужно ввести ответ: выбранное число - 100")
        else:
            print ("Вы ввели не число, либо не целое число. Попробуйте ещё раз!")
    
while True:     
    xerx = int (xerx)
    if (rex3 - 100) == xerx:
        break
    else:
        print ("Вы решили пример не верно. Попробуйте ещё раз")

print ("Ваш ответ - ", xerx,'. Он правильный. Отличная работа!')

def calc(xerx):
    xerx = int(xerx)
    f1 = xerx//10
    f2 = xerx%10
    result = 'В твоём числе: десятков - ' +str(f1)+ ' a едениц - ' +str(f2)+ '. Спасибо за игру! До новых встреч!'
    return result

print (calc(xerx))


    

