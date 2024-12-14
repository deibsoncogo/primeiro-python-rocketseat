def addTask(tasks, nameTarefa):
  task = { "name": nameTarefa, "isCompleted": False}
  tasks.append(task)
  print(f"Tarefa {nameTarefa} foi adicionada com sucesso")
  return

def getTasks(tasks):
  print("\nLista de tarefas:")

  for index, task in enumerate(tasks, start=1):
    status = "✓" if task["isCompleted"] else " "
    print(f"{index}. [{status}] {task["name"]}")

  return

def updateNameTask(tasks, indexTask, newNameTask):
  if indexTask >= 0 and indexTask < len(tasks):
    tasks[indexTask - 1]["name"] = newNameTask
    print(f"\nTarefa {indexTask} atualizada para {newNameTask}")
  else:
    print("\nÍndice da tarefa inválida")

  return

tasks = []

while True:
  print("\nMenu do Gerenciador de Lista de Tarefas:")
  print("1. Adicionar tarefas")
  print("2. Ver tarefas")
  print("3. Atualizar tarefa")
  print("4. Completar tarefa")
  print("5. Deletar tarefas concluídas")
  print("6. Sair")

  select = input("\nDigite a sua escolha: ")

  if select == "1":
    nameTask = input("\nDigite o nome da tarefa que deseja adicionar: ")
    addTask(tasks, nameTask)
  elif select == "2":
    getTasks(tasks)
  elif select == "3":
    getTasks(tasks)
    indexTask = int(input("\nDigite o número da tarefa que deseja alterar: "))
    nameTask = input("Digite o novo nome da tarefa: ")
    updateNameTask(tasks, indexTask, nameTask)
  elif select == "6":
    break

print("\nPrograma finalizado")
