# projeto_tarot
projeto pessoal para estudos de codigo python e sql 
## **🔮 Sistema de Gerenciamento de Tarot**
Um sistema em Python para gerenciamento e consulta de cartas de tarot, com banco de dados SQL Server.

### ✨ Funcionalidades
- 📋 Listar todas as cartas - Visualize todas as cartas cadastradas no banco de dados

- 🎲 Puxar carta aleatória - Sorteio aleatório de uma carta com seu significado

- ➕ Inserir nova carta - Adicione novas cartas ao seu baralho virtual

- 💾 Banco de dados - Armazenamento persistente em SQL Server

### 🛠️ Tecnologias Utilizadas
- Python 3.x
- pyodbc - Conexão com banco de dados
- SQL Server - Banco de dados
- Windows Authentication - Autenticação segura

### 📋 Pré-requisitos
- Python 3.x instalado
- SQL Server instalado e configurado
- Driver ODBC para SQL Server
- Biblioteca pyodbc: pip install pyodbc

### 🚀 Como Executar
1. Clone o repositório:

``` 
git clone [url-do-repositorio]
cd tarot_db
``` 
2. Configure o banco de dados:
   - Crie um banco chamado tarot_db no SQL Server
   - Crie a tabela cartas_tarot com a estrutura apropriada

3. Configure a conexão:
   - Edite o arquivo tarot_db.py e ajuste o nome do servidor:

```
server = 'NOME_DO_SEU_SERVIDOR'
```
4. Execute o sistema:

``` 
python tarot_db.py
``` 
### 🗃️ Estrutura do Banco de Dados
A tabela `cartas_tarot` deve conter os seguintes campos:

|Campo			|Tipo			|Descrição|
|---------------|---------------|--------------------------------------
|`id`				|INT			|Chave primária autoincrementável|
|`nome_carta`		|VARCHAR(100)	|Nome da carta (ex: "O Louco", "O Mago")|
|`significado`	|TEXT			|Significado completo da carta|
|`arcano`			|VARCHAR(10)	|Tipo de arcano ("Maior" ou "Menor")|
|`numero`			|INT			|Número da carta (opcional, figuras de corte não contém numeros)|
|`naipe	`		|VARCHAR(20)	|Naipe da carta (opcional, para Arcanos Menores)|


## 📝 Exemplo de Uso
```
--- Menu de Tarot ---
1. Listar todas as cartas
2. Puxar uma carta aleatória
3. Inserir uma nova carta
4. Sair

Escolha uma opção (1-4): 2

--- Carta Sorteada ---
Nome: O Louco
Significado: Representa novos começos, espontaneidade e liberdade.
``` 


## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs

- Sugerir novas funcionalidades

- Enviar pull requests

Desenvolvido com 💜 para estudos e prática de programação Python com banco de dados por Daniell Goes

