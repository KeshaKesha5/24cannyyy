import subprocess

def run_git_command(command):
    """Запуск git-команд с обработкой ошибок."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print("Қате орын алды:", e.stderr.strip())
        return None

# 1. Показать последний коммит
last_commit = run_git_command(["git", "log", "-1"])
if last_commit:
    print("Последний коммит перед новым коммитом:\n")
    print(last_commit)
    print("\n" + "="*60 + "\n")

# 2. Добавить все изменения
run_git_command(["git", "add", "."])

# 3. Сделать коммит с уникальным сообщением
commit_message = "Автоматтандырылған commit для ученика 24"
run_git_command(["git", "commit", "-m", commit_message])

# 4. Пуш на origin/master
push_result = run_git_command(["git", "push", "-u", "origin", "master"])
if push_result:
    print("Push выполнен успешно!")
