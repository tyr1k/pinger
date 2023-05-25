import tkinter as tk
import subprocess

def check_ping(host):
    # command = ['ping', '-n', '1', host]  # Для Windows
    command = ['ping', '-c', '1', host]  # Для Linux/Mac
    try:
        output = subprocess.check_output(command)
        return True
    except subprocess.CalledProcessError:
        return False

def update_window():
    host = '10.0.1.233'  # Изменить на нужный хост
    is_ping_successful = check_ping(host)
    
    if is_ping_successful:
        window.configure(bg='green')
    else:
        window.configure(bg='red')
    
    window.after(1000, update_window)  # Периодическое обновление каждую секунду

window = tk.Tk()
window.title("Пингер")
window.geometry("200x200")

update_window()

window.mainloop()
