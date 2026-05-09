arquivo = open('chamada.txt', '+w')

linhas = []

linhas.append('Geovana\n')
linhas.append('Alexandre\n')
linhas.append('Pedro\n')
linhas.append('Joel\n')
linhas.append('Sid\n')
linhas.append('Leonardo\n')

arquivo.writelines(linhas)

arquivo.close()

arquivo = open('chamada.txt', '+r')

conteudo = arquivo.readlines()
print(conteudo)
