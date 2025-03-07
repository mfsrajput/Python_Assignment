import click # to create a Cli
import json  # to save and load data tasks 
import os # to create a directory


TODO_FILE = "todo.json" # Define the filename where tasks are stored

# Function to load tasks from the JSON file
def load_tasks():
    if not os.path.exists(TODO_FILE): 
        return[]
    with open(TODO_FILE, "r") as file:
        return json.load(file)
    
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

@click.group()
def cli():
    """Simple Todo List Manager"""
    pass
@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Task added successfully: {task}")


@click.command()
def list():
    """List all the tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks found!.")
        return
    for index, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else '❌'
        click.echo(f"{index}. {task['task']} [{status}]")

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):

    """Mark a task as completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
         tasks[task_number - 1]["done"] = True
         save_tasks(tasks)
         click.echo(f"Task {task_number} marked as completed.")
    else:
        click.echo("Invalid task number: {task_number}")

@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """Remove a task from the list"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Task {task_number} removed: {removed_task['task']}")
    else:
        click.echo("Invalid task number: {task_number}")




cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)

if __name__ == "__main__":
    cli()


