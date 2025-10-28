import subprocess
import sys
import random

# ===============================
# Конфигурация
# ===============================
# Өз нөміріңізге сәйкес эмодзи таңдау
EMOJIS = ["🚀", "🧠", "🔧", "✨", "🐛", "🔥", "💡"]
# Мысалы, оқушы 1 болса тек 🚀 қосу:
# EMOJIS = ["🚀"]

# ===============================
# Функциялар
# ===============================

def run_command(command):
    """Python арқылы shell команданы орындау"""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Қате орын алды: {e.stderr}")
        sys.exit(1)

def git_add_all():
    """Барлық өзгерістерді қосу"""
    print("Git add...")
    run_command("git add .")

def git_commit():
    """Commit жасау, эмодзи қосу"""
    emoji = random.choice(EMOJIS)
    message = input(f"Commit хабарламасын енгізіңіз (эмодзи {emoji} автоматты түрде қосылады): ")
    full_message = f"{emoji} {message}"
    print(f"Commit жасау: {full_message}")
    run_command(f'git commit -m "{full_message}"')

def git_push():
    """Push жасау"""
    print("Git push...")
    run_command("git push")

# ===============================
# Негізгі блок
# ===============================
if __name__ == "__main__":
    git_add_all()
    git_commit()
    git_push()
