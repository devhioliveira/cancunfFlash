# =========================
# Helper: Tk file selector
# =========================
def select_file_dialog(title):
    root = tk.Tk()
    root.withdraw()
    # choose zip files
    filepath = filedialog.askopenfilename(title=title, filetypes=[("ZIP Files", "*.zip")])
    root.destroy()
    return filepath

# =========================
# Bootloader check (securestate)
# =========================
def bootloader_check(L):
    print(Fore.CYAN + L["boot_check"])
    try:
        # 'fastboot getvar securestate' prints to stderr in some fastboot versions; capture both
        result = subprocess.check_output(["fastboot", "getvar", "securestate"], stderr=subprocess.STDOUT)
        text = result.decode(errors="ignore").lower()
        if "flashing_unlocked" in text:
            print(Fore.GREEN + L["boot_unlocked"])
            return True
        else:
            print(Fore.RED + L["boot_locked"])
            input("> ")
            return False
    except subprocess.CalledProcessError as e:
        # if fastboot returns with error text, it's in e.output
        out = e.output.decode(errors="ignore").lower() if e.output else ""
        if "flashing_unlocked" in out:
            print(Fore.GREEN + L["boot_unlocked"])
            return True
        print(Fore.RED + L["no_securestate"])
        return False
    except Exception:
        print(Fore.RED + L["no_securestate"])
        return False