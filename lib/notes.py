
def notes_function(tasks):
    newdict = {}
    for key in tasks.keys():
        if key == "#TODO":
            newdict[key] = tasks.get(key)
            return newdict








#As a user
#So that I can find my tasks among all my notes
#I want to check if a line from my notes includes the string `#TODO`.
