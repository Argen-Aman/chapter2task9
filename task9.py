str1 = input("Word(string):\n")

if str1.count("f") >= 2:
    print('The index of the first appearance of f: ' + str(str1.find('f')))
    print('The index of the last appearance of f: ' + str(str1.rfind('f')))
elif str1.count("f") == 1:
    print('The index of the appearance of f: ' + str(str1.find("f")))
else:
    print('')
