import pyodbc

#configurção de conexão
server = 'DESKTOP-QMFT4D7'
database = 'tarot_db'

#string de conexão 
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE{database};Trusted_Connection=yes'

#conectar ao banco
try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Conexão bem sucedida!")
except Exception as e:
    print(f'Erro ao conectar: {e}')
    exit()

#consultar todas as cartas:
cursor.execute("SELECT id_carta, nome_carta, arcano, numero, naipe FROM tarot_db.dbo.cartas_tarot")
cartas = cursor.fetchall()


print("\n--- Cartas no Banco ---")
for carta in cartas:
    print(carta)

#fechar conexão 
conn.close()