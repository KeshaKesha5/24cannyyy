import os
import subprocess
import time
import datetime
import zipfile
import platform

LOG_FILE = 'system_log.txt'

def log_message(message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f'[{timestamp}] {message}\n')
    print(f'[{timestamp}] {message}')

def get_cpu_temp_linux():
    try:
        result = subprocess.run(['sensors'], capture_output=True, text=True, check=True)
        output = result.stdout
        for line in output.splitlines():
            if 'Package id 0:' in line or 'Core 0:' in line:
                parts = line.split()
                for part in parts:
                    if '°C' in part:
                        temp = part.strip('+').replace('°C','')
                        return temp
        return "N/A"
    except Exception as e:
        log_message(f'Ошибка при получении температуры на Linux: {e}')
        return "Error"

def get_cpu_temp_windows_wmi():
    try:
        import wmi
    except ImportError:
        log_message('Библиотека wmi не установлена. Установите через pip install wmi')
        return "Error"
    try:
        w = wmi.WMI(namespace="root\\wmi")
        temperature_infos = w.MSAcpi_ThermalZoneTemperature()
        temps = []
        for sensor in temperature_infos:
            temp_c = (sensor.CurrentTemperature / 10) - 273.15
            temps.append(round(temp_c, 1))
        if temps:
            return str(min(temps))
        else:
            return "N/A"
    except Exception as e:
        log_message(f'Ошибка при получении температуры через wmi библиотеку: {e}')
        return "Error"

def backup_log():
    try:
        if os.path.exists(LOG_FILE):
            backup_name = f"{LOG_FILE}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
            with zipfile.ZipFile(backup_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(LOG_FILE)
            log_message(f'Лог файл заархивирован в {backup_name}')
            open(LOG_FILE, 'w').close()
        else:
            log_message('Лог файл не найден для бэкапа.')
    except Exception as e:
        log_message(f'Ошибка при создании резервной копии лога: {e}')

def main():
    log_message('Скрипт запущен')
    try:
        while True:
            system = platform.system()
            if system == 'Linux':
                temp = get_cpu_temp_linux()
            elif system == 'Windows':
                temp = get_cpu_temp_windows_wmi()
            else:
                temp = "Unsupported OS"
                log_message(f'Операционная система {system} не поддерживается')

            log_message(f'Температура CPU: {temp} °C')

            if os.path.exists(LOG_FILE):
                size = os.path.getsize(LOG_FILE)
                if size > 1024*1024:  
                    backup_log()

            time.sleep(300)  
    except KeyboardInterrupt:
        log_message('Скрипт остановлен вручную')
    except Exception as e:
        log_message(f'Неожиданная ошибка: {e}')

if __name__ == '__main__':
    main()
