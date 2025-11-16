from pyfiglet import Figlet
from colorama import init, Fore
import os
import sys
import time
import shutil
import urllib.request
import zipfile
import platform

init(autoreset=True)

# ============================
# SISTEMA DE LINGUAGEM
# ============================

LANG = {
    "pt": {
        "credits": "[CREDITOS] > Desenvolvido por DevHiOliveira.",
        "checking_system": "[INFO] > Checando ambiente do sistema...",
        "system_detected": "[INFO] > Sistema operacional detectado: ",
        "install_deps": "Instalar dependências para o CancunfFlash? (s/n): ",
        "cancelled": "Instalação cancelada.",
        "installing_libs": "[INFO] > Instalando bibliotecas Python...",
        "libs_ok": "[OK] > Bibliotecas instaladas.",
        "checking_tools": "[INFO] > Verificando ADB e Fastboot...",
        "not_found": "[FALTA] > {} não encontrado.",
        "found": "[OK] > {} encontrado.",
        "missing_tools": "[AVISO] > Ferramentas ausentes: ",
        "auto_install": "[INFO] > Instalando Platform-Tools automaticamente...",
        "all_good": "Tudo pronto! Ambiente configurado.",
        "need_admin": "[ERRO] > Este processo exige privilégios elevados.",
        "downloading": "[INFO] > Baixando Platform-Tools...",
        "extracting": "[INFO] > Extraindo arquivos...",
        "tools_installed": "[OK] > Platform-Tools instalado com sucesso.",
        "path_updated": "PATH atualizado. Reinicie o terminal.",
        "press_enter": "Pressione ENTER para continuar...",
        "exit": "Pressione ENTER para sair..."
    },

    "en": {
        "credits": "[CREDITS] > Developed by DevHiOliveira.",
        "checking_system": "[INFO] > Checking system environment...",
        "system_detected": "[INFO] > Detected operating system: ",
        "install_deps": "Install CancunfFlash dependencies? (y/n): ",
        "cancelled": "Installation cancelled.",
        "installing_libs": "[INFO] > Installing Python libraries...",
        "libs_ok": "[OK] > Libraries installed.",
        "checking_tools": "[INFO] > Checking ADB and Fastboot...",
        "not_found": "[MISSING] > {} not found.",
        "found": "[OK] > {} found.",
        "missing_tools": "[WARNING] > Missing tools: ",
        "auto_install": "[INFO] > Installing Platform-Tools automatically...",
        "all_good": "All set! Environment configured.",
        "need_admin": "[ERROR] > Elevated privileges are required.",
        "downloading": "[INFO] > Downloading Platform-Tools...",
        "extracting": "[INFO] > Extracting files...",
        "tools_installed": "[OK] > Platform-Tools successfully installed.",
        "path_updated": "PATH updated. Restart your terminal.",
        "press_enter": "Press ENTER to continue...",
        "exit": "Press ENTER to exit..."
    }
}

# Escolher idioma
print("\nSelect language / Selecione o idioma:")
print("1 - Português (PT-BR)")
print("2 - English (EN-US)")
lang_choice = input("\n> ").strip()

if lang_choice == "2":
    L = LANG["en"]
else:
    L = LANG["pt"]

# Diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

system = platform.system()

if system == "Windows":
    os_name = "Windows"
elif system == "Linux":
    os_name = "Linux"
elif system == "Darwin":
    os_name = "MacOS"
else:
    os_name = f"Unknown ({system})"


# ============================
# Verifica admin
# ============================
def is_admin():
    if system == "Windows":
        import ctypes
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:
        return os.geteuid() == 0


# ============================
# PATH
# ============================
def add_to_path(path_to_add):
    if system == "Windows":
        import winreg
        reg_path = r"System\CurrentControlSet\Control\Session Manager\Environment"

        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_READ) as key:
            current_path, _ = winreg.QueryValueEx(key, "Path")

        if path_to_add.lower() in current_path.lower():
            print(Fore.GREEN + "[OK] > Platform-Tools already in PATH.")
            return

        updated = current_path + ";" + path_to_add
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, updated)

        print(Fore.GREEN + "[OK] > PATH updated successfully.")

    else:
        shell_profiles = ["~/.bashrc", "~/.zshrc", "~/.profile"]
        line = f'export PATH="$PATH:{path_to_add}"\n'

        for profile in shell_profiles:
            profile = os.path.expanduser(profile)
            if os.path.exists(profile):
                with open(profile, "r") as f:
                    if line.strip() in f.read():
                        print(Fore.GREEN + "[OK] > Platform-Tools already in PATH.")
                        return

            with open(profile, "a") as f:
                f.write(line)

        print(Fore.GREEN + "[OK] > " + L["path_updated"])


# ============================
# Baixar Platform Tools
# ============================
def install_platform_tools():

    if not is_admin():
        print(Fore.RED + "\n" + L["need_admin"])
        input(L["press_enter"])
        sys.exit(1)

    print(Fore.CYAN + "\n" + L["downloading"])

    if system == "Windows":
        url = "https://dl.google.com/android/repository/platform-tools-latest-windows.zip"
    elif system == "Linux":
        url = "https://dl.google.com/android/repository/platform-tools-latest-linux.zip"
    elif system == "Darwin":
        url = "https://dl.google.com/android/repository/platform-tools-latest-darwin.zip"
    else:
        print(Fore.RED + "\nSO not supported.")
        sys.exit(1)

    zip_name = "platform-tools.zip"
    urllib.request.urlretrieve(url, zip_name)

    print(Fore.CYAN + L["extracting"])
    with zipfile.ZipFile(zip_name, "r") as z:
        z.extractall(script_dir)

    os.remove(zip_name)

    extract_dir = os.path.join(script_dir, "platform-tools")
    print(Fore.GREEN + L["tools_installed"])
    add_to_path(extract_dir)

    input("\n" + L["press_enter"])


# ============================
# INTERFACE
# ============================
fbig = Figlet(font='big')
print(Fore.CYAN + fbig.renderText("SETUP"))
print(Fore.YELLOW + L["credits"] + "\n")
print(Fore.CYAN + L["checking_system"])
time.sleep(1)
print(Fore.CYAN + L["system_detected"] + os_name)
time.sleep(1)

choice = input("\n" + L["install_deps"]).strip().lower()

if choice not in ["s", "y"]:
    print(Fore.RED + L["cancelled"])
    sys.exit(0)

print(Fore.CYAN + "\n" + L["installing_libs"])
os.system("pip install -r requirements.txt")
print(Fore.GREEN + L["libs_ok"] + "\n")

print(Fore.CYAN + L["checking_tools"] + "\n")
time.sleep(1)

missing = []

for tool in ["adb", "fastboot"]:
    if shutil.which(tool) is None:
        print(Fore.RED + L["not_found"].format(tool))
        missing.append(tool)
    else:
        print(Fore.GREEN + L["found"].format(tool))

if missing:
    print(Fore.YELLOW + "\n" + L["missing_tools"] + ", ".join(missing))
    print(Fore.CYAN + L["auto_install"])
    install_platform_tools()
else:
    print(Fore.GREEN + "\n" + L["all_good"])

input("\n" + L["exit"])
