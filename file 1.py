print ("пітвердження особистості")
print ('='*25,'\033[0m\n')
age=int(input('ващ вік: '))
if age >=0 and age <14:
    print('свідоцтво про народження')
elif 14<=age<=35 :
    print('id-паспорт')
elif 35<=age<=110 :
    print('паспорт страого зразку')
else:
    print('помилка')