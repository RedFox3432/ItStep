print ("система оцінювання по 100 бальній системі")
print ('='*25,'\033[0m\n')
age=int(input('ваша оцінка: '))
if age >=0 and age <49:
    print('незадовільно')
elif 50<=age<=69 :
    print('задовільно')
elif 70<=age<=89 :
    print('добре')
elif 90 <= age <= 100:
    print('відмінно')
else:
    print('помилка')
