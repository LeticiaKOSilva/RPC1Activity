from rpc import Client

client = Client(14000,'127.0.0.1')

print(str(client.sumC(10,20)))
print(str(client.sub(10,15)))
print(client.mul(5,5))
print(client.div(10,2))