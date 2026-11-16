def f(name):
    count = 0
    string = ''
    string = string + name[0]
    while count < len(name):
        for i in name:
            if i == " ":
                string = string + name[count+1]
            count += 1
    return string