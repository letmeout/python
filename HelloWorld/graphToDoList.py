def getToDo (start, todos):
    if (len(todos[start]) == 0):
        return [start]
    elif (len(todos[start]) >= 1):
        list = [start]
        for todo in todos[start]:
            list += getToDo(todo, todos)

        return list

graph = {}
graph["getup"] = ["ready4lunch", "breash", "sport"]
graph["breash"] = ["breakfirst"]
graph["sport"] = ["bath"]
graph["bath"] = ["cloth"]
graph["ready4lunch"] = []
graph["cloth"] = []
graph["breakfirst"] = []

print(getToDo("getup", graph))

