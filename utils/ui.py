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
            flash_custom_rom(L)
        elif choice == "2":
            docs_page(L)
        elif choice == "3":
            install_ksu(L)
        elif choice == "4":
            install_ksu_next(L)
        elif choice == "0":
            print(Fore.CYAN + L["warn"])
            print("Bye.")
            sys.exit(0)
        else:
            print(Fore.RED + "Opção inválida / Invalid option.")