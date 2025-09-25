from datetime import datetime

class Reserva:
    def __init__(self, qtd_cliente, mesa, data_hora, status):
        self.qtd_cliente = qtd_cliente
        self.mesa = mesa
        self.data_hora = data_hora
        self.status = status

class GerenciamentoReservas:
    def __init__(self):
        self.reservas = []

    def adicionar_reserva(self, reserva):
        self.reservas.append(reserva)
        
    def reserva_por_mesa_status(self, mesa, status):
        contador = 0
        for reserva in self.reservas:
            if reserva.mesa == mesa and reserva.status == status:
                contador += 1
        return contador

class Cliente:
    def __init__(self, id_cliente, nome, telefone, status):
        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.status = status

class GerenciamentoClientes:
    def __init__(self):
        self.clientes = []
    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def lista_clientes_ativos(self):
        lista_clientes_ativos = []
        for i in self.clientes:
            if i.status == 'confirmado':
                lista_clientes_ativos.append(i)
        return lista_clientes_ativos

class Mesa:
    def __init__(self, id_mesa, capacidade_maxima, localização, status):
        self.id_mesa = id_mesa
        self.capacidade_maxima = capacidade_maxima
        self.localização = localização
        self.status = status

class GerenciamentoMesas:
    def __init__(self):
        self.mesas = []
    
    def adicionar_mesa(self, mesa):
        self.mesas.append(mesa)

    def listar_mesas_disponiveis(self):
        lista_mesas_disponiveis = []
        for i in self.mesas:
            if i.status != 'disponível':
                lista_mesas_disponiveis.append(i)
        return lista_mesas_disponiveis

# - Gerenciadores
gerenciador_clientes = GerenciamentoClientes()
gerenciador_mesas = GerenciamentoMesas()
gerenciador_reservas = GerenciamentoReservas()

# - Adicionando clientes
cliente1 = Cliente(1, "Maria", "1234-5678", "confirmado")
cliente2 = Cliente(2, "Frederico", "8765-4321", "pendente")
cliente3 = Cliente(3, "Valentina", "1122-3344", "cancelado")

gerenciador_clientes.adicionar_cliente(cliente1)
gerenciador_clientes.adicionar_cliente(cliente2)
gerenciador_clientes.adicionar_cliente(cliente3)

# - Adicionando mesas
mesa1 = Mesa(1, 4, "Janela", "disponível")
mesa2 = Mesa(2, 2, "Centro", "ocupada")
mesa3 = Mesa(3, 6, "Varanda", "disponível")

gerenciador_mesas.adicionar_mesa(mesa1)
gerenciador_mesas.adicionar_mesa(mesa2)
gerenciador_mesas.adicionar_mesa(mesa3)

# - Adicionando reservas
gerenciador_reservas = GerenciamentoReservas()
reserva1 = Reserva(2, mesa1, datetime(2024, 7, 20, 19, 0), "confirmado")
reserva2 = Reserva(4, mesa2, datetime(2024, 7, 20, 20, 0), "pendente")
reserva3 = Reserva(3, mesa1, datetime(2024, 7, 21, 18, 30), "cancelado")

gerenciador_reservas.adicionar_reserva(reserva1)
gerenciador_reservas.adicionar_reserva(reserva2)
gerenciador_reservas.adicionar_reserva(reserva3)

# - Simulação dos status das reservas
status_mesa1 = gerenciador_reservas.reserva_por_mesa_status(mesa1, "confirmado")
print(f"Reserva confirmada para a mesa 1: {status_mesa1}")

status_mesa2 = gerenciador_reservas.reserva_por_mesa_status(mesa2, "pendente")
print(f"Reserva pendente para a mesa 2: {status_mesa2}")

status_mesa1_cancelada = gerenciador_reservas.reserva_por_mesa_status(mesa1, "cancelado")
print(f"Reserva cancelada para a mesa 1: {status_mesa1_cancelada}")

# - Lista de clientes ativos
print("Clientes ativos:")
for cliente in gerenciador_clientes.lista_clientes_ativos():
    print(f"Nome: {cliente.nome}, Telefone: {cliente.telefone}")

# - Lista de mesas disponíveis
print("Mesas disponíveis:")
for mesa in gerenciador_mesas.listar_mesas_disponiveis():
    print(f"Capacidade: {mesa.capacidade_maxima}, Localização: {mesa.localização}, Status: {mesa.status}")