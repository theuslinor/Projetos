from keyboard import write
from io import open
from time import sleep

with open('./arquivo.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
sleep(5)
write(conteudo, delay=0.05)
