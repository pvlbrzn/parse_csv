import json

lines = []
# open file "BelFactory.csv" and read line by line
with open("BelFactory.csv", "r") as f:
    keys = f.readline().strip().split(",") #strip() delet \n in the end str
    res = [dict(zip(keys, line.strip().split(","))) for line in f] #split() separation string sep=","

print(res) #print list of dictionaries with datas from file

#open file "BelFactory.json" and write file using the module json.dump
with open('BelFactory.json', 'w') as file:
    json.dump(res, file, indent=4) 
