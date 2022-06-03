import pandas as pd

rutaFileCsv = "https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true"


def listaPeliculas(rutaFileCsv: str) -> str:
    if ".csv" in rutaFileCsv:
        try:
            df = pd.read_csv(rutaFileCsv, header=0)
            subconjunto = df[["Country", "Language", "Gross Earnings"]]
            resultado = pd.pivot_table(
                subconjunto, index=["Country", "Language"], values=["Gross Earnings"]
            )
            return resultado.head(10)
        except:
            return print("Error al leer el archivo de datos.")

    else:
        print("Extensión inválida.")


print(listaPeliculas(rutaFileCsv))
