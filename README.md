# Atualização chegou:
> Data da atualização: 22/04/2021

O que mudou?

- Tratamento de erro e excessão.
- Mudanças na estética. (atualização de hoje 21/04/2021)
- Opção de baixar uma playlist foi totalmente refeita. (atualização de hoje 21/04/2021)
- Filtros de extensões adicionados para cada extensão. (atualização de hoje 21/04/2021)
- Script mais interativo e colorido para deixar mais fácil o uso. (atualização de hoje 21/04/2021)
- Progresso de download de vídeos adicionada! (atualização de hoje 22/04/2021)
- Adicionado um patch de reparo. Opção 5 no script. (atualização de hoje 24/04/2021)
- Adicionado a função histórico, onde seus links de vídeos favoritos ficam salvos! (Atualização de hoje 25/04/2021)
- Adicionado a opção de converter para um MP3 na opção 3! (atualização de hoje 26/04/2021)
- Mudanças na estética pt(2). (atualização de hoje 29/04/2021)
- Mudanças para deixar o script mais rápido! (atualização de hoje 29/04/2021)
- Adicionada a opção de baixar um vídeo/foto/foto do perfil do instagram! (atualização de hoje 01/05/2021)


# Nova função (Download do Instagram)
#### Saiba utilizar corretamente:

- Entre com usuário ou email
- Pegue o link da foto ou vídeo
- Exemplo de link válido: https://www.instagram.com/p/COVhUQhLBqr/

## Onde encontro os vídeos do instagram?

- O script logo após o download irá criar uma pasta chamada: POST
- Entre nessa pasta e lá vai estar os videos e fotos baixados
- Já a foto de perfil que você baixar, vai ficar armazenada na pasta com o mesmo nome de usuário!

# Pasta POST:
![Veja como fica a pasta ](https://user-images.githubusercontent.com/69327287/116791891-b3e55e00-aa93-11eb-902e-901190e3285a.png)

# Arquivos baixados estão dentro da pasta POST:
![Arquivos baixados ](https://user-images.githubusercontent.com/69327287/116791920-e1caa280-aa93-11eb-8bfe-30d3b5e2317c.png)



# Função histórico?
- Sim, é uma função que eu adicionei para guardar os links dos seus videos preferidos, playlists preferidas

# Como usar a função histórico?

- Rode esse comando dentro da pasta do script E-tube:
- python links.py --visualizar ou --v
- Em seguida todo o histórico de links vai aparecer para você!

# [Função Histórico] Ajuda a encontrar vídeos esquecidos:
- Essa função também facilita na busca por seus vídeos favoritos, caso tenha esquecido
- de algum vídeo, rode o script links.py que você achará!
 
# Cinco opções novas implementadas. São elas:

- Baixar música
- Mudar a cor do banner de entrada
- Meios de contato para falar comigo
- Reparar erros do script
- Na opção 3 o vídeo pode ser convertido para um audio.mp3

# COMO FAZER A CONVERSÃO? [Siga o exemplo abaixo]:

- ![clique aqui para ver o exemplo](https://user-images.githubusercontent.com/69327287/116332575-670a3a80-a7a8-11eb-9cd0-9caa88bf341d.png)

# E-tube
Script para downloads de video/playlists de video/ música do youtube

- ![Clique aqui para ver o script](https://user-images.githubusercontent.com/69327287/116332915-fc0d3380-a7a8-11eb-883c-f403b46f2bb5.png)


# Terá mais atualizações?
- Sim


# Como instalar o script?
- Siga os passos abaixo para instalar corretamente o E-tube:


# PASSOS PARA USUÁRIOS DO TERMUX!!!

- Pelo terminal, acesse a pasta de Downloads porque é onde você vai deixar o script!
- termux-setup-storage
- cd storage/downloads
- git clone https://github.com/lucas-Dk/E-tube
- cd E-tube
- pip install --upgrade pip
- pip install -r requirements.txt
- python3 setup.py
- python3 e-tube.py
- Pronto, já está rodando o meu script e já pode baixar os vídeos!

# PASSOS PARA USUÁRIOS DO PC/LINUX!!!

- Pelo terminal, acesse a pasta de Downloads porque é onde você vai deixar o script!
- cd \Users\Cliente\Downloads (cole o caminho assim, lembrando que o seu pode ta diferente, cole certo!)
- git clone https://github.com/lucas-Dk/E-tube
- cd E-tube
- pip install --upgrade pip
- pip install -r requirements.txt
- python3 setup.py
- python3 e-tube.py
- Pronto, já está rodando o meu script e já pode baixar os vídeos!

# Onde fica o video baixado?

- O processo de download de vídeos/playlist ou o MP3 do arquivo, todos
- ficam armazenados dentro das pastas com os respectivos nomes:
- Vídeos-baixados (armazena apenas vídeos)
- Playlist YT (armazena apenas as playlists)
- VideosConvertidos (armazena o vídeo que será/foi convertido para MP3)
- Fora dessas pastas, na parte onde você encontra o script e etc
você vai encontrar o áudio do vídeo que foi convertido para mp3

- ![Exemplo](https://user-images.githubusercontent.com/69327287/116333196-7047d700-a7a9-11eb-9494-c5a098982baf.png)


# Para acessar os vídeos rapidamente pelo terminal:

## PASSOS PARA USUÁRIOS DO TERMUX!!!
- Saia do script e na mesma pasta digite > cd Vídeos-baixados (aqui vão estar todos os vídeos)
- cd Playlist YT (aqui vão estar todos os vídeos da playlist que você baixou)
- cd Músicas (aqui vão estar todos os vídeos que foram convertidos para mp3)
- Se quiserem usar um gerenciador de arquivos para achar mais rápido ainda:
- Podem usar este > https://play.google.com/store/apps/details?id=com.alphainventor.filemanager

- Abra o gerenciador
- Abra a pasta Downloads que vai aparecer de primeira para você!
- Abra a pasta E-tube
- E ai dentro vai ter todas as pastas/músicas.mp3

## PASSOS PARA USUÁRIOS DO PC/LINUX!!!

- Saia do script e na mesma pasta digite > cd Vídeos-baixados (aqui vão estar todos os vídeos)
- cd Playlist YT (aqui vão estar todos os vídeos da playlist que você baixou)
- cd VideosConvertidos (aqui vão estar todos os vídeos que foram convertidos para mp3)





> script by > Lucas-DK

