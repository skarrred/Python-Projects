
import pickle
import random
import time

storage = []
while True:
    inp = input("Do you want to load an existing file? (y/n): ")
    if inp == 'y':
        file_name= input("Enter file name: ")
        with open(file_name, 'rb') as f:
            storage = pickle.load(f)
        break
    elif inp == 'n':
        capacity = int(input("How many inputs do you have?: "))
        for i in range(capacity):
            storage.append(input("Enter value: "))
        file_name = input("Enter file name to save: ")
        pickle.dump(storage, open(file_name, 'wb'))
        break
    else:
        print("invalid response")
        continue

print(storage)

trig = True
while trig:
    inp = int(input("\n=============================================\n(1)Select item at random.\n(2)Show list\n(3)Exit\n(4)Add item to list\n"))
    if inp == 1:
        if storage:
            inx = random.randrange(len(storage))
            print(storage[inx])
            del storage[inx]
        elif not storage:
            print("empty")
        else:
            print('confused lol')
        time.sleep(1)
    elif inp == 2:
        print(storage)
    elif inp == 3:
        break
    elif inp == 4:
        storage.append(input("Enter value to add: "))
    else:
        print("you had 4 options and you still messed up shame on you")
        continue

pickle.dump(storage, open(file_name, 'wb'))
