import pyodbc

#configurção de conexão
server = localhost
database = tarot_db
username = 
password = 

#string de conexão 
con_str = f'DRIVER={{Sql Server}};SERVER={localhost},DATABASE{tarot_db},Trusted_Conection=yes'

#conectar ao banco
try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Conexão bem sucedida!")
except Exception as e:
    print(f'Erro ao conectar: {e}')
    exit()

#consultar todas as cartas:
cursor.execute("SELECT id_carta, nome_carta, arcano, numero, naipe FROM cartas_tarot")
cartas = cursor.fetchall()


print("\n--- Cartas no Banco ---")
for carta in cartas:
    print(carta)

#fechar conexão 
conn.close()