# RPC1Activity

### -> Criação de um cliente e servidor que possuem classes Server e Client em um arquivo rpc.py que gerencia cálculos básicos desses sockets.

- O programa foi feito utilizando a linguagem Python;
- As bibliotecas usadas nesse código foram: socket e threading;
- Foram criadas 2 classes sendo:
   - Uma classe Client que fornece métodos para a manipualação de dados do cliente e comunicação com o servidor;
   - Uma classe Servder que fornece métodos para manipular os dados vindos do cliente, processá-las e devolve-las ao cliente;
- Os arquivos client.py e server.py só instanciam,inicializam suas classes e chamam os métodos;
- Os arquivos acima se conectam a esse arquivo rpc.py pela importação:
    - client.py: import rpc from Client;
    - server.py: import rpc from Server;
- O código possui multiprocessos, o servidor pode atender a mais de um cliente por criar uma thread para cada um desses clientes.
