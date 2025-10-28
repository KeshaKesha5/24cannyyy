import subprocess
import sys
import random
import os

# ===============================
# Конфигурация
# ===============================
# Эмодзи тізімі
EMOJIS = ["🚀", "🧠", "🔧", "✨", "🐛", "🔥", "💡"]

# ===============================
# Функциялар
# ===============================

def run_command(command, cwd=None):
    """
    Python арқылы shell команданы орындау
    cwd - жұмыс директориясы (репозиторий)
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            text=True,
            capture_output=True,
            cwd=cwd
        )
        if result.stdout.strip():
            print(result.stdout.strip())
        if result.stderr.strip():
            print(result.stderr.strip())
    except subprocess.CalledProcessError as e:
        print(f"Қате орын алды: {e.stderr.strip()}")
        sys.exit(1)

def git_add_all(repo_path="."):
    """Барлық өзгерістерді қосу"""
    print("Git add...")
    # Қосымша дәйексөздермен қоршау
    run_command('git add "."', cwd=repo_path)

def git_commit(repo_path="."):
    """Commit жасау, эмодзи қосу"""
    emoji = random.choice(EMOJIS)
    message = input(f"Commit хабарламасын енгізіңіз (эмодзи {emoji} автоматты түрде қосылады): ")
    full_message = f"{emoji} {message}"
    print(f"Commit жасау: {full_message}")
    run_command(f'git commit -m "{full_message}"', cwd=repo_path)

def git_push(repo_path="."):
    """Push жасау"""
    print("Git push...")
    run_command("git push", cwd=repo_path)

# ===============================
# Негізгі блок
# ===============================
if __name__ == "__main__":
    # Репозиторий жолын кириллица/бос орындар үшін абсолют жолмен алуға болады
    repo_path = os.path.abspath(".")
    
    git_add_all(repo_path)
    git_commit(repo_path)
    git_push(repo_path)

    print("Барлық Git операциялары сәтті орындалды ✅")
