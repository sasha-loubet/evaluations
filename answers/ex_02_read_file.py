nameslist = open("nameslist.txt", "r") 
  
dico = dict() 
  
for line in nameslist: 
    line = line.strip() 
    line = line.lower() 
    words = line.split(" ") 
  
    for word in words: 
        if word in dico: 
            dico[word] = dico[word] + 1
        else: 
            dico[word] = 1

for key in list(dico.keys()): 
    print(key, ":", dico[key]) 