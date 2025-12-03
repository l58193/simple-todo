#!/usr/bin/env python3
import sys
from todo import TodoManager

WELCOME = "Simple TODO Maker"  

def print_usage():
    print("Usage: python3 main.py [list|add|done|remove] [args...]")
    print("Commands:")
    print("  list                 - list all tasks")
    print("  add <description>    - add a new task")
    print("  add --urgent <desc>  - add a new urgent task  # TODO: implementar")
    print("  done <id>            - mark task id as done")
    print("  remove <id>          - remove task id")

def main():
    print(WELCOME)
    if len(sys.argv) < 2:
        print_usage()
        return

    cmd = sys.argv[1]
    manager = TodoManager("tasks.json")

    if cmd == "list":
        manager.list_tasks()
    elif cmd == "add":
        urgent = False
        # TODO:
        # 1. Verificar se o utilizador passou o argumento --urgent
        if sys.argv[2] == "--urgent":
            urgent = True
            args = sys.argv[3:]
        # 2. Passar essa informação para o método add_task(...)
        # 3. Alterar o JSON para guardar um campo "urgent": true/false
        #
        # Atualmente o suporte a "urgent" NÃO está implementado.
        else:
            args = sys.argv[2:]
        if not args:
            print("Error: missing description")
            return
        description = " ".join(args)
        # Por enquanto, chama add_task sem o parâmetro urgent (default).
        manager.add_task(description, urgent)
    elif cmd == "done":
        if len(sys.argv) < 3:
            print("Error: missing id")
            return
        manager.mark_done(int(sys.argv[2]))
    elif cmd == "remove":
        if len(sys.argv) < 3:
            print("Error: missing id")
            return
        manager.remove_task(int(sys.argv[2]))
    else:
        print_usage()

if __name__ == "__main__":
    main()
