import pandas as pd


def listaPeliculas(rutaFileCsv: str) -> str:
    if ".csv" in rutaFileCsv:
        try:
            df = pd.read_csv(rutaFileCsv, header=0)
            subconjunto = df[["Country", "Language", "Gross Earnings"]]
            resultado = pd.pivot_table(
                subconjunto, index=["Country", "Language"], values=["Gross Earnings"]
            )
            return print(resultado.head(10))
        except:
            print("Error al leer el archivo de datos.")

    else:
        return print(resultado)


listaPeliculas(
    "https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true"
)
