colnames=['id','Title','Author','Price']
result=(1,"mary", "story", 21)
item = {}

for i, colName in enumerate(colnames):
    value = result[i]
    item[colName] = value

print(item)