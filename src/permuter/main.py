import sys
import os
from utils.colors import Bgc
from utils.banners import help_banner, app_banner, more_args_required_banner
from utils.iter import num_of_perms, iterate_elemets
from utils.interactions import ask_for_special_chars, ask_for_minimum_password_length



def main() -> None:
    minimum_password_lenght = 0
    data = []

    app_banner()

    if len(sys.argv) == 1 or sys.argv[1] == "--help":
        help_banner()
        sys.exit()

    if len(sys.argv) < 4:
        more_args_required_banner()
        sys.exit()

    try:
        use_esp_chars = input(ask_for_special_chars)
        minimum_password_lenght = int(input(ask_for_minimum_password_length))

        if use_esp_chars in ['y', 'Y']:
            data = ['-', '_', '.', '!', '*']

    except KeyboardInterrupt:
        print(Bgc.Red + Bgc.Bold + "\n\n[X]User abort" + Bgc.End)
        sys.exit()

    for arg in range(1, len(sys.argv)):
        data.append(sys.argv[arg])

    print("\n" + Bgc.Blue + "[+]Num of items to be permuted: " + Bgc.End + str(len(data)))
    print(Bgc.Blue + "[+]Num of permutations: " + Bgc.End + str(num_of_perms(len(data))))

    with open('passw.txt', 'w', encoding='utf-8') as file:
        print("\n" + Bgc.Yellow + "[!]Creating password list" + Bgc.End)
        print(Bgc.Yellow + "[!]File location: " + Bgc.Blue + \
              os.getcwd() + "/" + Bgc.End + "passw.txt")

        list_of_passwords = iterate_elemets(data, minimum_password_lenght)

        for password in list_of_passwords:
            if len(password) >= minimum_password_lenght:
                file.write(password)

    print(Bgc.Green + Bgc.Bold + "[!]File generated successfully" + Bgc.End)


if __name__ == "__main__" :
    main()
