# instalamos pandas y openpyxl para exel: pip install pandas openpyxl
import pandas as pd

# dataframe es la informacion basica con el nombre de las piezas y centimetros para poder armar el exel

data = {
    "piezas": ["pata", "tablero", "puerta", "estante", "panel lateral"],
    "centimetros": [40, 120, 60, 30, 180],
}

df = pd.DataFrame(data)

# guardar el dataframe en un exel, csv, cualquiera que necesiten

df.to_csv("muebles_medidas.csv", index=False)
