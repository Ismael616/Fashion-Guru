import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
import time
from time import sleep
from stqdm import stqdm




### Config 

st.set_page_config(
    page_title="Fashion Guru",
    page_icon="Media/Logo.png",
    layout="wide"
)

st.header("FASHION GURU ")
df=pd.read_csv('Data/dataset.csv')
marques=list(df['Marque '].unique())
sexes=list(df['Sexe '].unique())
selected = option_menu(None, ["Home", "Fit Recommender", "Profile","Contact"], 
   icons=['house', 'magic', "person-circle","envelope"],
   menu_icon="cast", default_index=0, orientation="horizontal")
#selected2   

if selected=="Home":

    st.write("you selected",selected)
    st.write("Todo: Page de présentation de Fashion Guru")

elif selected=="Fit Recommender":

    with st.form("my_form"):
        st.write("Enter Your  Informations")
        marque = st.selectbox('Select the brand',marques)
        sexe =st.radio("What's your Gender ",sexes)
        taille=st.slider('What\'s your height ?(in cm)',100, 230,160)
        tour_poitrine=st.slider('What\'s your Chest Mesurement ?(in cm)', 0, 200,100)
        tour_taille=st.slider('What\'s your Waistline ?(in cm)', 0, 200, 100)
        tour_hanche=st.slider('What\'s your hip circumference ?(in cm)', 0, 200, 100)
        submit1=st.form_submit_button('Génerer la prédiction')
    if submit1 :
        taille_reco='S'
        my_bar=st.progress(0)
        for percent_complete in range(100):
                time.sleep(0.002)
                my_bar.progress(percent_complete +1 ) 
        succes=st.success(f'La taille recommandé est {taille_reco}')
    try:
        if succes :
            txt = st.text_area("Prompt")
    except:
         pass 
elif selected=="Profile":
    
    st.write('TODO: Design une page de login et Signup Si le temps le permet ')

else :
    st.header("Function not supported yet")


