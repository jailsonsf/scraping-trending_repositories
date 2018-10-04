import requests
from bs4 import BeautifulSoup

r = requests.get('https://github.com/trending')
bs = BeautifulSoup(r.text, 'lxml')

lista_repo = bs.find_all('ol', class_='repo-list')

arquivo = open('trending.txt', 'w')

for lr in lista_repo:

    aux = lr.find_all('div', class_='d-inline-block col-9 mb-1')
    for ld in aux:
        
        rank = ld.find_all('a')

        arquivo.writelines(str(rank))
        arquivo.writelines('\n')

arquivo.close()

arquivo = open('trending.txt', 'r')

texto = []
for x in arquivo:

    if x[0] == '[' and x[1] == '<' and x[2] == 'a':

        na = x.split('"')
        texto.append(na[1])
arquivo.close()

arquivo = open('trending.txt', 'w')
arquivo.writelines('{} {}, {}.\n\n'.format('pos', 'nome', 'repositorio'))
for i in range(10):

    tex = texto[i].split('/')
    nome = tex[1]
    repo = tex[2]

    arquivo.writelines('{}° {}, {}.'.format(i + 1, nome, repo))
    arquivo.writelines('\n')
arquivo.close()


arquivo = open('trending.txt', 'r')

print(arquivo.read())

arquivo.close()