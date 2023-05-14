import psycopg2

class Conexion:
    def __init__(self, **args):
        for clave, valor in args.items():
            setattr(self, clave, valor)
        self.conexion = None
        
    def conectar(self):
        """Establece la conexión con la base de datos"""
        self.conexion = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )

        return self.conexion

    def desconectar(self):
        """Cierra la conexión con la base de datos"""
        if self.conexion:
            self.conexion.close()
            self.conexion = None