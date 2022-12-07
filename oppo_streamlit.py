import matplotlib as mpl
import matplotlib.pyplot as plt
import mysql.connector as mysql
import numpy as np
import pandas as pd
import seaborn as sns
import seaborn.objects as so
import streamlit as st
import random
import json
import pickle
import matplotlib.patches as mpatches
from IPython.display import clear_output
from sklearn import datasets
from sklearn import metrics
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Charge le modèle enregistré et test à partir du fichier chargé
import cloudpickle as cp
from urllib.request import urlopen
mydict = cp.load(urlopen("https://github.com/Dimitri-J/Opossum/raw/main/fl.pkl")) 

# mydict = pickle.load(pick)         # load file content as mydict
# f.close()                       
# test = np.array([6.7, 3.1, 5.6, 2.4])
# test = test.reshape(1, -1)
print(mydict)
# mydict["model"].predict(mydict["stand"].transform(test))



# with open('fl.pkl', 'rb') as f: # 'r' for reading; can be omitted
#     mydict = pickle.load(f)         # load file content as mydict
#     f.close()                       
#     # test = np.array([6.7, 3.1, 5.6, 2.4])
#     # test = test.reshape(1, -1)
#     print(mydict)
#     # mydict["model"].predict(mydict["stand"].transform(test))


# Déclaration de variable formulaire

hdlngth= "hdlngth"
totlngth= "totlngth"
taill= "taill"
footlgth= "footlgth"
earconch= "earconch"
belly= "belly"
test= []
y_pred= []


# Config page Streamlit

st.set_page_config(page_title="e-Shop Predictor", layout="wide")
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://4kwallpapers.com/images/wallpapers/macos-monterey-stock-purple-dark-mode-layers-5k-3840x2160-5896.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
st.subheader('Bonjour,')
st.title("E-Shop simulator")
st.write("[Clique-ici >](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")

# Formulaire de dimentions iris

col1, col2, col3 = st.columns(3)

with col1:
    st.header("hdlngth")
    hdlngth = st.slider(label = "Indiquer la grosseur de la tête", key=hdlngth, min_value = 80.0, max_value = 110.0, value = 90.0, step=0.1)
    st.write('La grosseur de la tête est de ', hdlngth, 'cm')


with col2:
    st.header("totlngth")
    totlngth = st.slider("Indiquer la longeur total", key=totlngth, min_value = 75.0, max_value = 100.0, value = 90.0, step=0.1)
    st.write('La taille totale est de ', totlngth, 'cm')

with col3:
    st.header("taill")
    taill = st.slider('Indiquer la taille de la queue', key=taill, min_value = 30.0, max_value = 45.0, value = 35.0, step=0.1)
    st.write('La queu mesure ', taill, 'cm')

col4, col5, col6 = st.columns(3)

with col4:
    st.header("footlgth")
    footlgth = st.slider('Indiquer la longeur des pieds', key=footlgth, min_value = 55.0, max_value = 80.0, value = 65.0, step=0.1)
    st.write('Les pieds mesurent ', footlgth, 'cm')


with col5:
    st.header("earconch")
    earconch = st.slider("Indiquer l'espace entre les oreilles", key=earconch, min_value = 35.0, max_value = 60.0, value = 50.0, step=0.1)
    st.write("L'espacement des oreilles est de  ", earconch, 'cm')

with col6:
    st.header("belly")
    belly = st.slider('Indiquer le tour de ventre', key=belly, min_value = 20.0, max_value = 45.0, value = 30.0, step=0.1)
    st.write('Le tour de ventre est de ', belly, 'cm')



if st.button("Estimation d'achat"):
    import time

    col_b1, col_b2 = st.columns([2,1])
    test = np.array([hdlngth, totlngth, taill, footlgth, earconch, belly])

    print(test)
    test = test.reshape(1, -1)
    print(test)
    predic = mydict["model"].predict(mydict["scaler"].transform(test))
    print(predic)
    st.success(f'Son âge serait de {predic}', icon="✅")
        