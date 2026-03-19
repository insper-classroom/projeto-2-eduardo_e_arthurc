from dotenv import load_dotenv
load_dotenv()

from database import get_connection

with open("imoveis (1).sql", "r", encoding="utf-8") as f:
    sql_script = f.read()

conn = get_connection()
cursor = conn.cursor()

for comando in sql_script.split(";"):
    comando = comando.strip()
    if comando:
        print("Executando comando...")
        cursor.execute(comando)

conn.commit()

cursor.close()
conn.close()

print("Banco criado com sucesso!")