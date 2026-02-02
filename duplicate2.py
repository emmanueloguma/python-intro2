#to check for duplicatee item and print them out ignore the extensions
listme2=["pawpaw.txt","tomato.txt","apple.mb","apple.mb","apple.mb","carrot.pg","goat.jpg","goatt.jpg","cashew.mb","cashew.mb","groundnut.jpg"]
opt=[]
duplicateitem=[]

for item in listme2:
    opt.append(item)
    if opt.count(item)>1:
        duplicateitem.append(item)
    else:
        continue
print("duplicate items found biut not stored anyway")
print(duplicateitem)