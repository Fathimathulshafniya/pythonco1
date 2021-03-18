s="roses are red , but not red"
for x in s.strip().split():
    print("the occurance of the text is:",x,s.strip().split().count(x))