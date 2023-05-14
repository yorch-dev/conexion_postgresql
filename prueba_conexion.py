import os
from dotenv import load_dotenv
from conexion_postgres import config, conexion

load_dotenv()
ini_file_path = os.getenv('INI_FILE_PATH')

# Cargando datos de conexión
data_conn = config.config(ini_file_path)
# crear objeto conexion
con = conexion.Conexion(**data_conn)

# Conectando a la base
conn = con.conectar()
cur = conn.cursor()

# Gestionando consulta
print('PostgreSQL database version:')
cur.execute('SELECT version()')
resultados = cur.fetchall()
print(resultados)

# Cerrando conexión
cur.close()
con.desconectar()

