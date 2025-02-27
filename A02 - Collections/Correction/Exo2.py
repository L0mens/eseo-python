import copy

classDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

#1

print(classDict['class']['student']['name'])

#2

classDict['class']['student']['marks']['physics'] = 89

#3
notes = classDict['class']['student']['marks'].values()


classDict['class']['student']['average'] = sum(notes)/len(notes)
print(classDict)

#4
#Pour garder les premières questions fonctionnels on va dupliquer le dict
classDictLi = copy.deepcopy(classDict)

classDictLi['class']['student'] = [classDictLi['class']['student']]

#5 #6

classDictLi['class']['student'].append({
            "name": "Ted",
            "marks": {
                "physics": 39,
                "history": 99
            },
            "average": (39+99)/2
        })



#7

lst_moy= []

for student in classDictLi['class']['student']:
    lst_moy.append(student['average'])

classDictLi['class']['average_grade'] = sum(lst_moy)/len(lst_moy)

#8
print(classDictLi)