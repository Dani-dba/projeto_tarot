import pyodbc
import random
from time import sleep

#configuração de conexão.
server = 'DESKTOP-QMFT4D7'
database = 'tarot_db'

#string de conexão
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

def conectar_banco():
    try:
        conn = pyodbc.connect(conn_str)
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
def listar_cartas():
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT nome_carta, significado FROM tarot_db.dbo.cartas_tarot")
        cartas = cursor.fetchall()
        print("\n --- Cartas no Banco ---")
        for carta in cartas:
            print(carta)
        conn.close()

def puxar_carta_aleatoria():
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT nome_carta, significado FROM tarot_db.dbo.cartas_tarot ORDER BY NEWID()")
        carta = cursor.fetchone()
        print("\n --- Carta Sorteada ---")
        print(f'Nome:{carta[0]}')
        print(f'Significado:{carta[1]}')
        conn.close()

def inserir_carta():
    nome = input("Digite o nome da carta: ")
    significado = input("Digite o significado da carta: ")
    arcano = input("Digite o arcano (Maior/Menor): ")   
    numero = input("Se houver, digite o número da carta (ou deixe em branco): ")
    naipe = input("Digite o naipe (Paus, Copas, Espadas, Ouros ou deixe em branco):")

    conn = conectar_banco()
    if conn:
        cursor=conn.cursor()
        cursor.execute("INSERT INTO tarot_db.dbo.cartas_tarot (nome_carta, significado, arcano, numero, naipe) VALUES (?, ?, ?, ?, ?)",
            (nome, significado, arcano, numero if numero else None, naipe if naipe else None)
            )
        conn.commit()
        print("Carta inserida com sucesso!")
        conn.close()

while True:
    print("\n--- Menu de Tarot ---")
    print("1. Listar todas as cartas")
    print("2. Puxar uma carta aleatória")
    print("3. Inserir uma nova carta")
    print("4. Sair")
    opção = input("Escolha uma opção (1-4):")
    if opção == '1':
        listar_cartas()
    elif opção == '2':
        puxar_carta_aleatoria()
    elif opção == '3':
        inserir_carta()
    elif opção == '4':
        sleep(1)
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")