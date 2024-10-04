import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("PREDICCIÓN DE PLOIDÍA")

edad_ovocitos = st.slider("Edad Ovocitos", 0, 100)

# Crear dos columnas
col1, col2, col3 = st.columns(3)

# Variables en la primera columna
with col1:
    procedencia_ovocitos = st.selectbox("Procedencia Ovocitos", ["ÓVULO PROPIO", "ÓVULO DONADO"])
    procedencia_semen = st.selectbox("Procedencia Semen", ["SEMEN PROPIO", "SEMEN DONADO"])
    
# Variables en la segunda columna
with col2:
    mci = st.selectbox("MCI", ["A", "B", "C/D"])
    trofodermo = st.selectbox("Trofodermo", ["A", "B", "C"])
    grado_expansion = st.selectbox("Grado Expansión", ["1", "2", "3", "4", "5", "6"])

with col3: 
    destino = st.selectbox("Destino", ["CONGELADO", "FRESCO"])
    dia_embrion = st.selectbox("Día Embrion", ["5", "6"])

# Almacenar los valores en un diccionario (o puedes hacer lo que necesites con ellos)
variables = {
    "EDAD PTE OVOCITOS": edad_ovocitos,
    "PROCEDENCIA OVOCITOS": procedencia_ovocitos,
    "PROCEDENCIA SEMEN": procedencia_semen,
    "DIA EMBRION": dia_embrion,
    "GRADO EXPANSIÓN": grado_expansion,
    "MCI": mci,
    "TROFODERMO": trofodermo,
    "DESTINO": destino
}

df = pd.DataFrame([variables])
df
