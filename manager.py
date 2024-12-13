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
  elif select == "6":
    break

print("\nPrograma finalizado")
