import filecmp
import shutil

# Caminho das pastas.

servidor = 'C:/Users/mateus/Desktop/SERVIDOR'

estudante = 'C:/Users/mateus/Desktop/ESTUDANTE'

# Criação do comparador de pastas

comparador = filecmp.dircmp(servidor, estudante)

# Listar arquivos exclusivos em ambas as pastas

arquivos_exclusivos_servidor = comparador.left_only

arquivos_exclusivos_estudante = comparador.right_only

print("Arquivos exclusivos em servidor:", arquivos_exclusivos_servidor)

print("Arquivos exclusivos em Estudante:", arquivos_exclusivos_estudante)

lab2 = 48
lab1 = 35
lab3 = 12

# Use a função shutil.copy para copiar o arquivo

for item in arquivos_exclusivos_servidor:
    print(item)
    shutil.copy(servidor+'/'+item, estudante)
    print(f'O arquivo {item} foi copiado para {estudante}')
# Se você quiser mover o arquivo em vez de copiá-lo, use shutil.move
# shutil.move(origem, destino)





# Liste as subpastas que são comuns a ambas as pastas

#subpastas_comuns = comparador.common_dirs

#print("Subpastas comuns a ambas as pastas:", subpastas_comuns)

# Liste as subpastas que são exclusivas para cada pasta

#subpastas_exclusivas_servidor = comparador.subdirs

#print("Subpastas exclusivas no servidor:", subpastas_exclusivas_servidor)

# Listar arquivos comuns
# arquivos_comuns = comparador.common_files
# print("Arquivos comuns a ambas as pastas:", arquivos_comuns)

