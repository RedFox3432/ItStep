print ("система оцінювання по 100 бальній системі")
print ('='*25,'\033[0m\n')
bal=int(input('ваша оцінка: '))
if bal >=0 and bal <49:
    print('незадовільно')
elif 50<=bal<=69 :
    print('задовільно')
elif 70<=bal<=89 :
    print('добре')
elif 90 <= bal <= 100:
    print('відмінно')
else:
    print('помилка')
