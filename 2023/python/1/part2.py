file = open("input.txt", "r")
lines = file.readlines()

def is_number(string):
    match string:
        case "zero": return 0
        case "one": return 1
        case "two": return 2
        case "three": return 3
        case "four": return 4
        case "five": return 5
        case "six": return 6
        case "seven": return 7
        case "eight": return 8
        case "nine": return 9

def is_number_reversed(string):
    match string:
        case "orez": return 0
        case "eno": return 1
        case "owt": return 2
        case "eerht": return 3
        case "ruof": return 4
        case "evif": return 5
        case "xis": return 6
        case "neves": return 7
        case "thgie": return 8
        case "enin": return 9


total = []
total2 = [] 
for line in lines:
    line_rev = line[::-1]
    for i in range(len(line)):
        if line[i].isnumeric():
            total.append(line[i])
            break
        try: 
            if is_number(line[i:i+5]):
                total.append(str(is_number(line[i:i+5])))
                break
            if is_number(line[i:i+4]):
                total.append(str(is_number(line[i:i+4])))
                break
            if is_number(line[i:i+3]):
                total.append(str(is_number(line[i:i+3])))
                break
        except: pass
    for i in range(len(line_rev)):
        if line_rev[i].isnumeric():
            total2.append(line_rev[i])
            break
        try: 
            if is_number_reversed(line_rev[i:i+5]):
                total2.append(str(is_number_reversed(line_rev[i:i+5])))
                break
            if is_number_reversed(line_rev[i:i+4]):
                total2.append(str(is_number_reversed(line_rev[i:i+4])))
                break
            if is_number_reversed(line_rev[i:i+3]):
                total2.append(str(is_number_reversed(line_rev[i:i+3])))
                break
        except: pass
    
total2.reverse()
for i in range(len(total)):
    total[i] += total2[i]
total = [int(x) for x in total]

print(sum(total))