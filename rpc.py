import socket
import threading

#Instanciação de constantes
SUM = "soma"
SUB = "subtracao"
MUL = "multiplicacao"
DIV = "divisao"

class Client:
    #Construtor da classe Client
    def __init__(self, porta:int,host:str):
        self.porta = porta
        self.host = host
        self.socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket_client.connect((self.host,self.porta))

    #Responsável por preparar os dados e reenviar para o arquivo client.py o resultado da soma retornado pelo servidor
    def sumC(self, number1:float, number2:float) -> float :
        lista_soma = [SUM,number1,number2]
        return self.edit_data(lista_soma)
    
    #Responsável por preparar os dados e reenviar para o arquivo client.py o resultado da subtração retornado pelo servidor
    def sub(self,number1:float,number2:float) -> float :
        lista_sub = [SUB,number1,number2]
        return self.edit_data(lista_sub)

    #Responsável por preparar os dados e reenviar para o arquivo client.py o resultado da multiplicação retornado pelo servidor
    def mul(self,number1:float,number2:float) -> float :
        lista_mul = [MUL,number1,number2]
        return self.edit_data(lista_mul)
    
    #Responsável por preparar os dados e reenviar para o arquivo client.py o resultado da divisão retornado pelo servidor
    def div(self, number1:float, number2:float) -> float :
        lista_div = [DIV,number1,number2]
        return self.edit_data(lista_div)
    
    #Converte a lista em string, envia essa string ao servidor e recebe do servidor um dado e o retorna pra quem a chamou
    def edit_data(self,lista) -> float:
        #Convertendo lista em String
        data_str = ",".join(map(str,lista))
        self.socket_client.send(data_str.encode())
        result = self.socket_client.recv(1024).decode()
        return float(result)

class Server:
    #construtor da classe Server
    def __init__(self,porta:int,host:str):
        self.porta = porta
        self.host = host
        self.socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket_server.bind((host,porta))
        self.socket_server.listen()

    #Aceita as conexões de clientes e cria uma tread para cada um desses clientes
    def createThread(self):
        client, addr = self.socket_server.accept()
        client_new = threading.Thread(target= self.handle_client, args=(client,))
        client_new.start()
    
    #Comunicação/funcionalidades que o servidor realizara para cada cliente
    def handle_client(self,socket_client):
        while True:
            data = socket_client.recv(1024).decode()
            if not data:
                break

            type_operation, number1,number2 = data.split(",")
            number1 = float(number1)
            number2 = float(number2)

            result = None

            if(type_operation == SUM):
                result = number1 + number2
            elif (type_operation == SUB):
                result = number1 - number2
            elif(type_operation == MUL):
                result = number1 * number2
            elif (type_operation == DIV):
                if number2 != 0:
                    result = number1 / number2
            
            if result is not None:
                socket_client.send(str(result).encode())
            
        socket_client.close()
                    

