di = {'vk':9,'gk':12,'mk':15,'rm':7}

# x = di.values()

# winner = max(x)

# if winner in di:
#     print("Yes")

max = 0
win = ""
for key in di:
    if di[key] > max:
        max = di[key]       
    else:
        max = 0 + max

for name, cost in di.items():
    if cost == max:
        print(f"Winner Amount is {max} and Winner name is {name}")


    