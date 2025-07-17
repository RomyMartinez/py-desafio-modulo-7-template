'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''


class TaskHandler:
    def create_task():
        print("Criando nova tarefa")

    def update_task():
        print("Atualizando tarefa")

    def remove_task():
        print("Removendo tarefa")

class APIHandler:
    def connect_api():
        print("Conectando ao API")

class  NotificationHandler:
    def send_notification():
        print("Enviando notificação")

class ReportHandler:
    def generate_report():
        print("Gerando relatório")
        
    def send_report():
        print("Enviando relatório")

