import subprocess

def run_git_command(command):
    """Git командаларын орындау"""
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Қате орын алды: {result.stderr}")
    else:
        print(result.stdout)

def main():
    # 1. Файлдарды қосу
    run_git_command(["git", "add", "."])
    
    # 2. Оқушының нөміріне сай ерекшелік
    # Мысалы, №24 оқушы commit алдында соңғы commit-ты шығарады
    run_git_command(["git", "log", "-1"])
    
    # 3. Commit жасау
    run_git_command(["git", "commit", "-m", "Автоматтандырылған commit"])
    
    # 4. Push жасау
    run_git_command(["git", "push", "-u", "origin", "master"])

if __name__ == "__main__":
    main()
