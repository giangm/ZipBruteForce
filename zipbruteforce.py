from zipfile import ZipFile
import argparse
import colorama
from colorama import Fore, Style
import time, os

# Colored text
colorama.init(autoreset=True)

# Instantiate parser
parser = argparse.ArgumentParser(description="\nUsage: python3 zipbruteforce.py -z [archive.zip] -p [passwords.txt]")

# Adding zip file arugment
parser.add_argument("-z", dest="ziparchive", help="Zip archive file")

# Adding password file argument
parser.add_argument("-p", dest="passwordfile", help="Password file")

# Parsing arguements
args = parser.parse_args()

try:

    # Instantiate variables
    found = ""
    ziparchive = ZipFile(args.ziparchive)
    password_file = args.passwordfile

except:

    # Print program usage
    print(parser.description)
    exit(1)

with open(password_file, "r") as file:

    counter = 0

    print(Fore.YELLOW + "[+] CRACKING ARCHIVE...")
    time.sleep(1)


    # Iterating through each password in password file
    for line in file:

        # Stripping the new line at the end of password and encoding
        password = line.strip("\n").encode("utf-8")

        # Counting number of passwords attempted
        counter += 1

        try:

            # Attempt to extract zip archive with password from file
            found = ziparchive.extractall(pwd = password)

            # Check if archive was extracted successfully
            if found == None:
                print(Fore.GREEN + "[+] Password is: " + password.decode())
                print(Fore.GREEN + f"[+] Tested {counter} passwords.")

                # Get extracted contents
                extracted = os.listdir(args.ziparchive.rstrip(".zip"))
                print(Fore.GREEN + f"[+] Extracted {len(extracted)} item: ")

                # Print each item that is extracted
                for i in range(len(extracted)):
                    print(Fore.GREEN + f"[{i + 1}] " + extracted[i])

        except RuntimeError:

            # Bad passwords
            pass

    # If found is empty then it means that no password matched
    if found == "":
        print(Fore.RED + "[!] Password was not found in file, try different password file.")
        print(Fore.RED + f"[!] Tested {counter} passwords.")
