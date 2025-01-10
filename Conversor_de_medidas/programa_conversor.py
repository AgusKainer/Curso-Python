import pandas as pd


def cm_a_pulgadas(cm):
    return cm / 2.54


# Leer el archivo exel

df = pd.read_excel("muebles_medidas.xlsx")

# Añadir una columna al datafram que sea de pulgadas y se llene con el calculo de cm / 2.54

df["pulgadas"] = df["centimetros"].apply(cm_a_pulgadas)

df.to_excel("mueble_medidas_convertidas.xlsx", index=False)

print("conversion exitosa, en un archivo nuevo_; mueble_medidas_convertidas ")
