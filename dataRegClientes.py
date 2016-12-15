import json

class clientes:
    clientes = []

    def readRegClientes(self):
        with open('data/clientes.json','r') as file:
            clientes = json.load(file)
            self.clientes = clientes['results']

    def getCliente(self):
        cliente = []
        for row in self.clientes:
            RegClientes = row['nombre']
            if RegClientes not in cliente:
                cliente.append(RegClientes)
        return cliente