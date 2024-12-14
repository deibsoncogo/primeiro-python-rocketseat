def addTask(tasks, name):
  task = { "name": name, "isCompleted": False}
  tasks.append(task)
  print(f"Tarefa {name} foi adicionada com sucesso")
  return

def getTasks(tasks):
  print("\nLista de tarefas:")

  for index, task in enumerate(tasks, start=1):
    status = "✓" if task["isCompleted"] else " "
    print(f"{index}. [{status}] {task["name"]}")

  return

def updateNameTask(tasks, index, newName):
  if index >= 0 and index < len(tasks):
    tasks[index - 1]["name"] = newName
    print(f"\nTarefa {index} atualizada para {newName}")
  else:
    print("\nÍndice da tarefa inválida")

  return

def completeTask(tasks, index):
  if index >= 0 and index < len(tasks):
    tasks[index - 1]["isCompleted"] = True
    print(f"\nTarefa {index} completada")
  else:
    print("\nÍndice da tarefa inválida")

  return

tasks = []

while True:
  print("\nMenu do Gerenciador de Lista de Tarefas:")
  print("1. Adicionar tarefa")
  print("2. Ver tarefas")
  print("3. Atualizar tarefa")
  print("4. Completar tarefa")
  print("5. Deletar tarefas concluídas")
  print("6. Sair")

  select = input("\nDigite a sua escolha: ")

  if select == "1":
    name = input("\nDigite o nome da tarefa que deseja adicionar: ")
    addTask(tasks, name)
  elif select == "2":
    getTasks(tasks)
  elif select == "3":
    getTasks(tasks)
    index = int(input("\nDigite o número da tarefa que deseja alterar: "))
    name = input("Digite o novo nome da tarefa: ")
    updateNameTask(tasks, index, name)
  elif select == "4":
    getTasks(tasks)
    index = int(input("\nDigite o número da tarefa que deseja completar: "))
    completeTask(tasks, index)
  elif select == "6":
    break

print("\nPrograma finalizado")
