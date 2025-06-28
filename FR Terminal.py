import tkinter as tk
import os
import requests
import subprocess
import git
import zipfile
import ctypes

program_files = os.environ.get("APPDATA")
freeinternet_path = os.path.join(program_files,"Free İnternet")
addictions_path = os.path.join(freeinternet_path,"Addictions")
turkey_dnsredir_cmd_path = os.path.join(addictions_path,"turkey_dnsredir.cmd")
service_remove_cmd_path = os.path.join(addictions_path,"service_remove.cmd")
service_install_dnsredir_turkeycmd = os.path.join(addictions_path,"service_install_dnsredir_turkey.cmd")

def custom_command(command):
    if command == "cls":
        return ""
    elif command.startswith("gbdt -run ~comme turkey_dnsredir.cmd"):
        ctypes.windll.shell32.ShellExecuteW(
        None, "runas", turkey_dnsredir_cmd_path, None, None, 1
    )
    elif command.startswith("gbdt -run ~comme service_remove.cmd"):
         ctypes.windll.shell32.ShellExecuteW(
        None, "runas", service_remove_cmd_path, None, None, 1
    )
    elif command.startwith("gbdt -run ~comme service install ~turkey"):
           ctypes.windll.shell32.ShellExecuteW(
        None, "runas", service_install_dnsredir_turkeycmd, None, None, 1
    )
    elif command == "clear":
        return ""  
    elif command.startswith("fr install goodbyedpiTR"): 
        try:
    
            appdata_path = os.environ.get("APPDATA")  
            free_internet_path = os.path.join(appdata_path, "Free İnternet", "Addictions")

            if not os.path.exists(free_internet_path):
                os.makedirs(free_internet_path)  
                print("Free İnternet klasörü oluşturuldu.")
            
            # Zip dosyasını indirir
            zip_url = "https://github.com/cagritaskn/GoodbyeDPI-Turkey/releases/download/release-0.2.3rc3-turkey/goodbyedpi-0.2.3rc3-turkey.zip"
            zip_file_path = os.path.join(free_internet_path, "goodbyedpi-0.2.3rc3-turkey.zip")
            
            # Zip dosyasını indirir
            response = requests.get(zip_url)
            with open(zip_file_path, 'wb') as f:
                f.write(response.content)
            print("Zip dosyası indirildi.")
            
            # Zip dosyasını çıkarır
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(free_internet_path)
            print("Zip dosyası başarıyla çıkarıldı.")
            
            return f"Dosyalar çıkarıldı: {free_internet_path}"
        
        except Exception as e:
            return f"Hata: {str(e)}"
    else:
        return None  

def FRTERMINALE():
    def FRTERMINALE_termınal():
        command = entry.get()  
        result = custom_command(command)  

        if result is not None:
            # Özel komut varsa sonucu göster
            output_text.config(state=tk.NORMAL)
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, result)
            output_text.config(state=tk.DISABLED)
        else:
            try:
                
                result = subprocess.run(command, shell=True, text=True, capture_output=True)

                
                output_text.config(state=tk.NORMAL)
                output_text.delete(1.0, tk.END)
                output_text.insert(tk.END, result.stdout)
                output_text.insert(tk.END, result.stderr)
                output_text.config(state=tk.DISABLED)

            except Exception as e:
                output_text.config(state=tk.NORMAL)
                output_text.delete(1.0, tk.END)
                output_text.insert(tk.END, f"Hata: {str(e)}")
                output_text.config(state=tk.DISABLED)

    
    root = tk.Tk()
    root.title("|FRTERMINAL|")
    root.geometry("500x400")

    # Label
    label = tk.Label(root, text="Run Command n:")
    label.pack(pady=5)

    # Entry
    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)

    # Button
    run_button = tk.Button(root, text="Çalıştır", command=FRTERMINALE_termınal)
    run_button.pack(pady=10)

    # Text
    output_text = tk.Text(root, height=10, width=60, wrap=tk.WORD, state=tk.DISABLED)
    output_text.pack(pady=10)

    # Mainlooper
    root.mainloop()  

FRTERMINALE()
