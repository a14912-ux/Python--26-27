tarefas = ["Tarefa 1" ,"Tarefa 2"]

tarefas.append("Tarefa 3") 
tarefas.extend(["Tarefa 4","Tarefa 5"]) 
tarefas.insert(2,"Tarefa 9") 
tarefas.remove("Tarefa 5")
tarefas.pop(2)
tarefas.clear()
tarefas.count("Tarefa 3")
tarefas.index(4)
tarefas.sort(reverse=True)
tarefas.reverse()
tarefas1 = [1,2,3]
tarefas2 = tarefas 
print(tarefas1,tarefas2)
tarefas.append(5)
print(tarefas,tarefas2)
tarefas3 = tarefas.copy() 
tarefas.append(7)
print(tarefas, tarefas2, tarefas3)
print(tarefas)




