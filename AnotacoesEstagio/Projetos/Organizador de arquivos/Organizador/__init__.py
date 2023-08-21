
def mover_arquivos(diretorio_origem, diretorio_destino, extensao=''):
    import os
    import shutil
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    for arquivo in os.listdir(diretorio_origem):
        if arquivo.endswith(extensao):
            caminho_completo = os.path.join(diretorio_origem, arquivo)

            nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
            contador = 1
            novo_nome_arquivo = nome_arquivo + extensao_arquivo
            while os.path.exists(os.path.join(diretorio_destino, novo_nome_arquivo)):
                novo_nome_arquivo = f"{nome_arquivo} ({contador}){extensao_arquivo}"
                contador += 1

            caminho_destino = os.path.join(diretorio_destino, novo_nome_arquivo)
            shutil.move(caminho_completo, caminho_destino)


