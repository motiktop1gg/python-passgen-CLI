import random
import datetime as dt

all_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "@", "!", "$", "%", "&", "^", "*", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
memorable_list = ["apple", "river", "mountain", "sky", "ocean", "forest", "computer", "python", "music", "sun", "moon", "star", "dream", "light", "shadow", "fire", "water", "earth", "wind", "stone", "cloud", "tree", "flower", "bird", "fish", "dog", "cat", "house", "car", "road", "train", "plane", "book", "pen", "paper", "lamp", "chair", "table", "phone", "keyboard", "mouse"]
password = ""
counter = 0

def gen_pass(length, count, memorable_mode, notrepeat_mode):
    global password
    global counter
    global all_list
    print(f"\n\n\nHere are your {count} passwords ({length} characters each)\n")
    ct = dt.datetime.now()

    with open("passwords.txt", "a") as ps:
        ps.write(f"\n=== passwords {ct.year}.{ct.month}.{ct.day} {ct.hour}:{ct.minute} ===\n")

    if memorable_mode:
        for word in memorable_list:
            if len(word) > length:
                pass
            else:
                all_list.append(word)
        while counter < count:
            current_length = 0
            counter += 1

            while len(password) < length:
                randIndex = random.randrange(len(all_list))
                if current_length + len(str(all_list[randIndex])) <= length:
                    password += str(all_list[randIndex]).upper() if random.getrandbits(1) else str(all_list[randIndex]).lower()
                    current_length += len(str(all_list[randIndex]))
                else:
                    pass
                
            print(password)
            with open("passwords.txt", "a") as ps:
                ps.write(f"\n{password}")
            password = ""

    elif notrepeat_mode and length <= len(all_list):
        while counter < count:
            current_length = 0
            counter += 1
            all_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "@", "!", "$", "%", "&", "^", "*", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            while len(password) < length:
                randIndex = random.randrange(len(all_list))
                password += str(all_list[randIndex]).upper() if random.getrandbits(1) else str(all_list[randIndex]).lower()
                all_list.pop(randIndex)

            print(password)
            with open("passwords.txt", "a") as ps:
                ps.write(f"\n{password}")
            password = ""

    elif not memorable_mode and not notrepeat_mode:
        while counter < count:
            counter += 1
            while len(password) < length:
                randIndex = random.randrange(len(all_list))
                password += str(all_list[randIndex]).upper() if random.getrandbits(1) else str(all_list[randIndex]).lower()

            print(password)
            with open("passwords.txt", "a") as ps:
                ps.write(f"\n{password}")
            password = ""
    
    else:
        print("Wrong parameters!")
        exit()

    print("\n\nAll passwords are also saved in passwords.txt.")
