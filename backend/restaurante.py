import datetime

reservas = []
clientes = {}
mesas = []

class Reserva:
    """
    Representa uma reserva de mesa com seus dados e métodos para interação com as reservas.
    """
    def __init__(self, cliente, mesa, data_hora, numero_pessoas, status):
        self.idReserva = len(reservas) + 1
        self.cliente = cliente
        self.mesa = mesa
        self.data_hora = data_hora
        self.numero_pessoas = numero_pessoas
        self.status = status
        print(self)

    def verificarVagas(self):
        """
        Retorna o número de vagas restantes.
        """
        reservas_ativas = 0
        for i in reservas:
            if i.mesa.idMesa == self.mesa.idMesa and i.status != 'Cancelada':
                reservas_ativas += 1
        return self.mesa.capacidadeMaxima - reservas_ativas

    def listarReservas(self):
        """
        Retorna uma lista de todas as reservas para esta mesa.
        """
        lista_reservas = []
        for i in reservas:
            if i.mesa.idMesa == self.mesa.idMesa:
                lista_reservas.append(i)
        return lista_reservas

    def confirmar_reserva(self):
        """
        Altera o status da reserva para 'Confirmada'.
        """
        self.status = 'Confirmada'
        print(f"Reserva {self.idReserva} confirmada")

    def cancelar_reserva(self):
        """
        Altera o status da reserva para 'Cancelada'.
        """
        self.status = 'Cancelada'
        print(f"Reserva {self.idReserva} cancelada")

    def alterar_reserva(self, nova_data_hora=None, novo_numero_pessoas=None):
        """
        Altera dados da reserva.
        """
        if nova_data_hora:
            self.data_hora = nova_data_hora
        if novo_numero_pessoas:
            self.numero_pessoas = novo_numero_pessoas
        print(f"Reserva {self.idReserva} alterada")

    def __str__(self):
        return f"Reserva: {self.idReserva} - Mesa: {self.mesa.idMesa} - Cliente: {self.cliente.nome} - Pessoas: {self.numero_pessoas} - Status: {self.status}"

class Cliente:
    """
    Representa uma pessoa que pode fazer reservas em mesas.
    """
    def __init__(self, ID_cliente, nome, telefone):
        self.ID_cliente = ID_cliente
        self.nome = nome
        self.telefone = telefone
        print(self)

    def listarReservas(self):
        """
        Retorna uma lista de todas as reservas do cliente.
        """
        lista_reservas = []
        for i in reservas:
            if i.cliente.ID_cliente == self.ID_cliente:
                lista_reservas.append(i)
        return lista_reservas

    def consultar_reserva(self):
        """
        Consulta reservas do cliente.
        """
        return self.listarReservas()

    def cancelar_reserva(self, reserva):
        """
        Cancela uma reserva específica.
        """
        reserva.cancelar_reserva()

    def atualizar_dados(self, novo_telefone=None):
        """
        Atualiza dados do cliente.
        """
        if novo_telefone:
            self.telefone = novo_telefone
        print(f"Dados do cliente {self.nome} atualizados")

    def __str__(self):
        return f"ID: {self.ID_cliente} - Cliente: {self.nome} (telefone: {self.telefone})"

class Mesa:
    """
    Esta classe representa uma mesa no restaurante.
    """
    def __init__(self, idMesa, capacidadeMaxima, localizacao):
        self.idMesa = idMesa
        self.capacidadeMaxima = capacidadeMaxima
        self.localizacao = localizacao
        self.disponivel = True
        print(self)

    def reservar_mesa(self):
        """
        Marca a mesa como reservada.
        """
        self.disponivel = False
        print(f"Mesa {self.idMesa} reservada")

    def liberar_mesa(self):
        """
        Marca a mesa como disponível.
        """
        self.disponivel = True
        print(f"Mesa {self.idMesa} liberada")

    def listarReservas(self):
        """
        Retorna uma lista de todas as reservas para esta mesa.
        """
        lista_reservas = []
        for i in reservas:
            if i.mesa.idMesa == self.idMesa:
                lista_reservas.append(i)
        return lista_reservas

    def __str__(self):
        disponivel_str = "Disponível" if self.disponivel else "Ocupada"
        return f"Mesa: {self.idMesa} - Capacidade: {self.capacidadeMaxima} - Local: {self.localizacao} - {disponivel_str}"

# --- Simulação do Sistema ---

print("Criando mesas e os salvando na lista global")
mesa1 = Mesa(1, 3, "Sala Principal")
mesa2 = Mesa(2, 2, "Sala VIP") 
mesa3 = Mesa(3, 4, "Varanda")
mesas.extend([mesa1, mesa2, mesa3])

print("\n\nCriando clientes e os salvando na lista global")
cliente1 = Cliente("1", "Ana Silva", "99111-2222")
cliente2 = Cliente("2", "Bruno Costa", "99333-4444")
cliente3 = Cliente("3", "Carla Souza", "99555-6666")
cliente4 = Cliente("4", "Diego Mendes", "99777-8888")
cliente5 = Cliente("5", "Elisa Gomes", "99999-0000")
for c in [cliente1, cliente2, cliente3, cliente4, cliente5]:
     clientes[c.ID_cliente] = c

print("\n\n--- Realizando Reservas ---")

# Reservas para a mesa 1 (capacidade 3)
reserva1 = Reserva(cliente1, mesa1, datetime.datetime(2024, 1, 15, 19, 0), 2, "Confirmada")
reservas.append(reserva1)
reserva2 = Reserva(cliente2, mesa1, datetime.datetime(2024, 1, 15, 20, 0), 3, "Confirmada")
reservas.append(reserva2)
reserva3 = Reserva(cliente3, mesa2, datetime.datetime(2024, 1, 16, 18, 0), 2, "Pendente")
reservas.append(reserva3)

print(f"\nEstão reservados no {mesa1}:")
for i in mesa1.listarReservas():
    print(f" - {i}")

print("\n\n"+"-" * 25)

# Reservas para a mesa 2 (capacidade 2)
print(reserva3)
reserva4 = Reserva(cliente1, mesa2, datetime.datetime(2024, 1, 16, 20, 0), 2, "Confirmada")
reservas.append(reserva4)
print(f"Estão reservados no {mesa2}:")
for i in mesa2.listarReservas():
    print(f" - {i}")

print("\n\n"+"-" * 25)

# Reserva para a mesa 3 (capacidade 4)
reserva5 = Reserva(cliente2, mesa3, datetime.datetime(2024, 1, 17, 19, 0), 4, "Confirmada")
reservas.append(reserva5)
reserva6 = Reserva(cliente2, mesa3, datetime.datetime(2024, 1, 17, 21, 0), 3, "Confirmada")
reservas.append(reserva6)

print(f"\nEstão reservados no {mesa3}:")
for i in mesa3.listarReservas():
    print(f" - {i}")


# Verificando o estado do sistema
print("\n\n--- Verificação do Sistema ---")

print(f"Mesas em que '{cliente1.nome}' está reservado:")
mesasCliente1 = cliente1.listarReservas()
for m in mesasCliente1:
    print(f"- {m}")

print()
mesasCliente1[0].cancelar_reserva()

print(f"\nMesas em que '{cliente1.nome}' está reservado:")
mesasCliente1 = cliente1.listarReservas()
for m in mesasCliente1:
    print(f"- {m}")
print
for m in mesas:
    print(m)
print()

for e in clientes:
    print(clientes[e])
print()

for e in reservas:
    print(e)
print()