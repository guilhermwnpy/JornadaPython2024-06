import flet as ft

def main(pagina):

    # tunel de comunicação online para multiplos usuarios
    def enviar_msg_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()
    pagina.pubsub.subscribe(enviar_msg_tunel)
    texto = ft.Text("Mwnzaps")
    
    chat = ft.Column()

    def enviar_msg(evento):
        texto_campo_msg = f"{nome_usuario.value}: {campo_msg.value}"
        
        campo_msg.value = ""
        # enviando ao tunel a informaçao de texto_campo_msg
        pagina.pubsub.send_all(texto_campo_msg)
        pagina.update()
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_msg)
    campo_msg = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_msg)

    def entrar_chat(evento):
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.add(chat)
        linha_msg = ft.Row([campo_msg, botao_enviar])
        pagina.add(linha_msg)
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.update()

    nome_usuario = ft.TextField(label="Escreva seu nome", on_submit=entrar_chat)
    popup = ft.AlertDialog(open=False, 
                           modal=True, 
                           title=ft.Text("Mwnzaps"),
                           content=nome_usuario,
                           actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)])
    
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)
    
    
    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(main, view=ft.WEB_BROWSER)