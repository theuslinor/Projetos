import modulos.Organizador as mod
fotos = ('.png', '.jpg', '.jpeg', '.webp', '.avif')
videos = ('.mp4','.mkv','.mov')
musicas = ('.mp3', '.wav')
rar = ('.rar', '.zip', '.7z')
doc = ('.docx', '.pdf', '.odt', '.txt')
exe = ('.exe')

#Pasta de fotos
mod.mover_arquivos('E:/download navegador', 'E:/JOGA TUDO/Fotos', fotos)
#Pasta de Videos
mod.mover_arquivos('E:/download navegador', 'E:/JOGA TUDO/Vdeos', videos)
#Pasta de Musicas
mod.mover_arquivos('E:/download navegador', 'E:/JOGA TUDO/Musica', musicas)
#Pasta de Rar
mod.mover_arquivos('E:/download navegador', 'E:/JOGA TUDO/Rar', rar)
#Pasta de Documentos
mod.mover_arquivos('E:/download navegador', 'E:/JOGA TUDO/Documentos', doc)
#Pasta de Executaveis
mod.mover_arquivos('E:/download navegador', 'E:/JOGA TUDO/Executavel', exe)

print('The end')