# passo 1 entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
# passo 2 fazer login no sistema
# passo 3 importar a base de dados
# passo 4 cadastrar 1 produto
# passo 5 repetir todos os produtos
# pyautogui site na cheat sheet tem dicas da biblioteca

import pandas
import pyautogui
import time

pyautogui.PAUSE = 0.5  # delay de meio segundo entre cada comando
# pyautogui.click
# pyautogui.press apertar
# pyautogui.write escrever
# pyautogui.hotkey apertar combinação de teclas

pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
# computador precisa esperar os comandados anteriores para ser executado,usando o comando delay, para não se atropelar
# pyautogui.PAUSE lá encima

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# computador precisa esperar a pagina carregar
# precisa usar biblioteca time para controlar o tempo de espera #import time lá emcima
# o comando time.sleep faz ele esperar 2 segundos APENAS NESSE COMANDO, pyautogui.pause espera 0.5 segundos em TODOS comandos
time.sleep(2)

# passo 2 fazer o login
# preciso dizer pro comando exatamete onde ele vai clicar
# inserindo email
pyautogui.click(x=632, y=480)
pyautogui.write('gabrielabobrinha@gmail.com')
time.sleep(3)
# inserindo senha
pyautogui.press('tab')
pyautogui.write('GabrielAbobrinha123')
time.sleep(2)
# logando no sistema
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)

# passo 3 importando a base de dados
# sempre lembrar que provavelmente alguem ja resolveu o seu problema, então procure no google
# instalar panda

# usar o comando para ler a base de dados no diretório
pandas.read_csv('produtos.csv')
# preciso armazenar a base de dados em uma variavel
# crie variaveis com nomes que façam sentido para fácil manutençao e compreensão
# a variavel fica na esquerda e recebe o que esta na direita
tabela = pandas.read_csv('produtos.csv')

print(tabela)
# passo 4 cadastrar 1 produto
# cadastre o primeiro manualmente e depois se preocupe em automatizar tudo

for linha in tabela.index:
    pyautogui.click(x=753, y=340)

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)  # digita a variavel que esta armazenada

    pyautogui.press('tab')  # passa para o proximo campo
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press('tab')
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press('tab')
    categoria = str(tabela.loc[linha , 'categoria '])
    pyautogui.write (categoria)

    pyautogui.press('tab')
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)

    pyautogui.press('tab')
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)

    pyautogui.press('tab')
    obs = str(tabela.loc[linha, "obs"])
    pyautogui.write(obs)

    pyautogui.press('tab')
    pyautogui.press('enter')

    
    pyautogui.scroll(10000) 
    
    # depois disso preciso voltar para a parte inicial do ssistema para cadastrar outro produto usando o scroll
 # scroll para cima
# numero positivo scroll para cima, numero negativo scroll para baixo
# posso colocar um scroll muito grande para ele simplesmente ir para o topo da pagina, sem medir

# custo = tabela.loc[linha , "custo"] = variavel custo = tabela.loc(localiza na tabela) de acordo com [linha ,
# "valor da linha vira custo"]

# valores entre aspas sao os nomes das colunas da tabela OBRIGATORIAMENTE

# os nomes tem que ser exatamente iguais aos da tabela, inclusive maiusculas e minusculas

# passo 5 automatizar a tarefa para repetir todos os produtos

# usar loop for para repetir a açao para todos os produtos

# o loop for no python é tudo que tiver espaço dentro do loop, sem espaço antes do comando ele NAO esta mais dentro do loop

# custo = tabela.loc[linha , "custo"] = variavel custo = tabela.loc(localiza na tabela) de acordo com [linha ,
# "valor da linha vira custo"]

# valores entre aspas sao os nomes das colunas da tabela OBRIGATORIAMENTE

# preciso pegar todos os dados automaticamente da tabela

#posso criar condições para tratar erros como ifs != "nan"

# para pausar a automação colocar mouse no canto superior esquerdo da tela para dar um failed safe
