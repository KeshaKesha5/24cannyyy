import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        print(f"Қате орын алды: {result.stderr}")
        return None

def main():
    print(" Git автоматтандыру басталды...\n")

    print(" Файлдарды git add арқылы қосу...")
    run_command("git add .")

    print("\n Соңғы commit туралы ақпарат:")
    last_commit = run_command("git log -1")
    if last_commit:
        print(last_commit)
    else:
        print("Commit табылмады немесе log бос.")

    message = input("\n Commit хабарламасын енгізіңіз: ")
    run_command(f'git commit -m "{message}"')
    print(" Commit жасалды!")

    print("\n Өзгерістерді серверге жіберу (git push)...")
    push_result = run_command("git push")
    if push_result is not None:
        print(push_result)
        print("\n Барлық өзгерістер push етілді!")
    else:
        print(" Push кезінде қате шықты.")

if __name__ == "__main__":
    main()
