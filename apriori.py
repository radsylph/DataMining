import psycopg2
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder

def Project():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432",
            database="andres"
        )
        cursor = connection.cursor()
        consulta = "SELECT  ARRAY_AGG(DISTINCT p.nombre ORDER BY p.nombre) AS productos FROM recibos r JOIN recibos_productos rp ON r.id = rp.id_recibo JOIN productos p ON rp.id_producto = p.id GROUP BY r.id ORDER BY r.id"
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        matriz_productos = [list(t[0]) for t in resultados]
        matriz_short = matriz_productos[:10]

        # Crear el dataframe de transacciones binarias (0 o 1)
        def crear_dataframe_transacciones(datos):
            te = TransactionEncoder()
            te_ary = te.fit(datos).transform(datos)
            return pd.DataFrame(te_ary, columns=te.columns_)

        # Crear el DataFrame de transacciones
        df = crear_dataframe_transacciones(matriz_short)

        print(df)

        # Obtener conjuntos de ítems frecuentes con el algoritmo Apriori
        conjuntos_frecuentes = apriori(df, min_support=0.9, use_colnames=True)

        # Obtener reglas de asociación a partir de los conjuntos de ítems frecuentes
        print(conjuntos_frecuentes)
        reglas_asociacion = association_rules(conjuntos_frecuentes, metric="confidence", min_threshold=0.8)

        print(reglas_asociacion)

    except (Exception, psycopg2.Error) as error:
        print("Error al conectar o interactuar con la base de datos:", error)

    finally:
        # Cerrar el cursor y la conexión
        if connection:
            cursor.close()
            connection.close()
            print("Conexión a PostgreSQL cerrada.")

Project()
