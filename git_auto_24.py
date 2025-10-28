import subprocess

def run_git_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print("Қате орын алды:", e.stderr.strip())
        return None

last_commit = run_git_command(["git", "log", "-1"])
if last_commit:
    print("Последний коммит перед новым коммитом:\n")
    print(last_commit)
    print("\n" + "="*60 + "\n")

run_git_command(["git", "add", "."])

commit_message = "Автоматизированный commit для 24"
run_git_command(["git", "commit", "-m", commit_message])

push_result = run_git_command(["git", "push", "-u", "origin", "master"])
if push_result:
    print("Push выполнен успешно!")
