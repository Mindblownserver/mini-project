test=[{"comp": "uter", "tabl": "ette"},{"comp": "d", "tabl": "tch"},{"comp": "uta", "tabl": "dawg"}]
def recherche(cond,text):
    dictt = list(dict())
    for dic in test:
        if text in dic[cond]:
            dictt.append(dic)
    return dictt
print(recherche("comp","ut"))