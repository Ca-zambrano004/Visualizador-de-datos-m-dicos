import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Importa los datos y asígnalos a df
df = pd.read_csv(r"C:\Users\WIN10\Desktop\CURSO PYTHON\3\medical_examination.csv")

# Agrega columna overweight (IMC > 25)
df['overweight'] = ((df['weight'] / ((df['height']/100) ** 2)) > 25).astype(int)

# Normaliza cholesterol y gluc (0 = bueno, 1 = malo)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# -------------------------------------------------------------------
# Función 1: Gráfico categórico
# -------------------------------------------------------------------
def draw_cat_plot():
    # Convierte datos a formato long
    df_cat = pd.melt(df, id_vars=['cardio'], 
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # Agrupa y reformatea datos
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # Dibuja gráfico categórico
    catplot = sns.catplot(x="variable", y="total", hue="value", col="cardio", 
                          data=df_cat, kind="bar")
    
    # Obtén la figura
    fig = catplot.fig
    
    # Devuelve la figura
    return fig

# -------------------------------------------------------------------
# Función 2: Mapa de calor
# -------------------------------------------------------------------
def draw_heat_map():
    # Limpia datos según condiciones
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calcula matriz de correlación
    corr = df_heat.corr()

    # Genera máscara para triángulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Configura figura
    fig, ax = plt.subplots(figsize=(12, 8))

    # Grafica matriz de correlación
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0, vmax=0.3, vmin=-0.1, cmap="coolwarm")

    # Devuelve la figura
    return fig
