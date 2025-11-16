#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyfiglet import Figlet
from colorama import init, Fore
import platform
import time
import shutil
import sys
import os
import subprocess
import importlib.util
import tkinter as tk
from tkinter import filedialog

init(autoreset=True)
fbig = Figlet(font='big')
os_name = platform.system()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# ---------- util: carregar módulo a partir de arquivo ----------
def load_module_from_path(module_name, path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None:
        raise ImportError(f"Não foi possível criar spec para {path}")
    module = importlib.util.module_from_spec(spec)
    loader = spec.loader
    if loader is None:
        raise ImportError(f"Loader ausente para {path}")
    loader.exec_module(module)
    return module


# ---------- carregar módulos locais ----------
assets_dir = os.path.join(BASE_DIR, "assets")
utils_dir = os.path.join(BASE_DIR, "utils")

def path_in_assets(name):
    return os.path.join(assets_dir, name)

def path_in_utils(name):
    return os.path.join(utils_dir, name)

# load lang
lang_path = path_in_assets("lang.py")
if not os.path.isfile(lang_path):
    raise FileNotFoundError(f"{lang_path} not found. Coloque assets/lang.py")
lang_mod = load_module_from_path("assets.lang", lang_path)
LANG = getattr(lang_mod, "LANG", None)
if LANG is None:
    raise RuntimeError("assets/lang.py deve definir LANG = {...}")

# load helpers
helpers_path = path_in_utils("helpers.py")
if not os.path.isfile(helpers_path):
    raise FileNotFoundError(f"{helpers_path} not found. Coloque utils/helpers.py")
helpers_mod = load_module_from_path("utils.helpers", helpers_path)

# load assets modules
flash_mod = load_module_from_path("assets.flash", path_in_assets("flash.py"))
docs_mod = load_module_from_path("assets.docs", path_in_assets("docs.py"))
ksu_mod = load_module_from_path("assets.install_ksu", path_in_assets("install_ksu.py"))
ksunext_mod = load_module_from_path("assets.install_ksunext", path_in_assets("install_ksunext.py"))


# ---------- injetar dependências ----------
setattr(helpers_mod, "tk", tk)
setattr(helpers_mod, "filedialog", filedialog)
setattr(helpers_mod, "Fore", Fore)
setattr(helpers_mod, "subprocess", subprocess)
setattr(helpers_mod, "os", os)
setattr(helpers_mod, "time", time)
setattr(helpers_mod, "input", input)
setattr(helpers_mod, "print", print)

setattr(flash_mod, "Fore", Fore)
setattr(flash_mod, "time", time)
setattr(flash_mod, "os", os)
setattr(flash_mod, "subprocess", subprocess)

if hasattr(helpers_mod, "select_file_dialog"):
    setattr(flash_mod, "select_file_dialog", getattr(helpers_mod, "select_file_dialog"))

if hasattr(helpers_mod, "bootloader_check"):
    setattr(flash_mod, "bootloader_check", getattr(helpers_mod, "bootloader_check"))

setattr(flash_mod, "input", input)
setattr(flash_mod, "print", print)

setattr(docs_mod, "tk", tk)

setattr(ksu_mod, "Fore", Fore)
setattr(ksu_mod, "input", input)
setattr(ksunext_mod, "Fore", Fore)
setattr(ksunext_mod, "input", input)


# ---------- garantir chaves mínimas ----------
def ensure_lang_defaults():
    defaults = {
        "device_reboot": {
            "pt": "[INFO] > Agora reinicie o sistema no dispositivo.",
            "en": "[INFO] > Now reboot the device."
        },
        "no_securestate": {
            "pt": "[ERRO] > Não foi possível verificar o estado do bootloader (securestate).",
            "en": "[ERROR] > Could not read bootloader securestate."
        }
    }
    for key, vals in defaults.items():
        for lang in ("pt", "en"):
            if key not in LANG.get(lang, {}):
                LANG.setdefault(lang, {})[key] = vals[lang]

ensure_lang_defaults()

# =========================
# select language
# =========================
def select_language():
    print("\n1 - Português (PT-BR)")
    print("2 - English (EN-US)\n")
    choice = input("> ").strip()
    return LANG["en"] if choice == "2" else LANG["pt"]


# =========================
# Docs page: abre Toplevel e espera fechar
# =========================
def docs_page(L):
    # obtém a função de abrir docs
    open_fn = getattr(docs_mod, "open_docs_window", None)
    if open_fn is None:
        print(Fore.RED + "Módulo docs não implementado corretamente.")
        input(L.get("return_menu", "\nPress ENTER to continue..."))
        return

    # cria root apenas AGORA — não na inicialização
    root = tk.Tk()
    root.withdraw()  # não pisca e não rouba foco

    # cria janela de docs (que também não rouba foco)
    win = open_fn(L, root)

    # espera fechar
    try:
        root.wait_window(win)
    finally:
        root.destroy()




# =========================
# Menu
# =========================
def menu(L):
    while True:
        print("\n" + L["menu_main"])
        print(L["menu1"])
        print(L["menu2"])
        print(L["menu3"])
        print(L["menu4"])
        print(L["menu0"])

        choice = input("\n> ").strip()
        if choice == "1":
            fn = getattr(flash_mod, "flash_custom_rom", None)
            if fn: fn(L)
            else:
                print(Fore.RED + "flash_custom_rom ausente.")
                input(L.get("return_menu", "\nPress ENTER to continue..."))

        elif choice == "2":
            docs_page(L)

        elif choice == "3":
            fn = getattr(ksu_mod, "install_ksu", None)
            if fn: fn("en" if L == LANG["en"] else "pt")  # passa string, não dicionário
            else:
                print(Fore.RED + "install_ksu ausente.")
                input(L.get("return_menu", "\nPress ENTER to continue..."))

        elif choice == "4":
            fn = getattr(ksunext_mod, "install_ksu_next", None)
            if fn: fn("en" if L == LANG["en"] else "pt")  # passa string, não dicionário
            else:
                print(Fore.RED + "install_ksu_next ausente.")
                input(L.get("return_menu", "\nPress ENTER to continue..."))

        elif choice == "0":
            print(Fore.CYAN + L["warn"])
            print("Bye.")
            sys.exit(0)

        else:
            print(Fore.RED + "Opção inválida / Invalid option.")


# =========================
# Main
# =========================
if __name__ == "__main__":
    L = select_language()

    print(Fore.CYAN + fbig.renderText(L["title"]))
    print(Fore.YELLOW + L["warn"])
    time.sleep(0.5)

    missing = []
    for t in ("adb", "fastboot"):
        if shutil.which(t) is None:
            missing.append(t)

    if missing:
        print(Fore.RED + "[ERRO] > Ferramentas faltando: " + ", ".join(missing))
        print("Instale adb/fastboot e execute novamente.")
        sys.exit(1)

    menu(L)
