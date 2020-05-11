dic = {}

with open('conf.txt', 'r') as file:
    for line in file:
        if line[0] != '#' and line[0] != ';' and line[0] != '\n':
            if '\n' in line:
                line = line[:-1]

            line = line.split(' ', 1)

            if len(line) > 1:
                key = line[0]
                dic[key] = line[1]
            else:
                key = line[0]

                dic[key] = "no value"
flag = True
while flag:

    num = input("Enter parameter (get param ....): ")
    slovo = num.split()
    counter = 0
    for key in dic:
        if len(slovo) > 2:
            if slovo[2] == key:
                print(key, '= ', dic[key])
                counter += 1
        else:
            counter = 0

    if counter == 0:
        print('no parameter')
    command = input("Continue? Yes or No: ")
    if command.lower() == 'yes':
        flag = True
    elif command.lower() == "no":
        flag = False
