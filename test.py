id = "606234127"
for i in open("chat_id.txt", 'r').readlines():
    if int(i) == int(id):
        print("yes")
    else:
        print("no")
