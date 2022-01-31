# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 08:55:35 2022

@author: groja
"""

import streamlit as st
import datetime
from PIL import Image

#%%

beso = 'beso.jpeg'
abrazo = 'abrazo.jpeg'
parral = 'parral.png'
heart = 'corazon.png'

beso_im = Image.open(beso)
abrazo_im = Image.open(abrazo)
parral_im = Image.open(parral)
heart_im = Image.open(heart)

col1, mid, col2 = st.columns([10,50,10])

with col1:
    st.image(heart_im,width=120)
with mid:
    st.markdown("<h1 style='text-align: center; color: white;'>3er Contrato de Renovación!</h1>", unsafe_allow_html=True)
with col2:
    st.image(parral_im,width=200)

st.write('Versión digital v.2')
st.header('Te amo con todo mi corazoncito')

st.write("""
    OLAAAAAAAAAAA MI AMORRRRR QUE ESTAMOS LLEGANDO LEJOS (carita ojitos tiernos), de verdad que loco todo
    lo que ha pasado hasta el día de hoy, demasiado loco pensar de que cada día que pasa me enamoras más
    y más. He pensado mucho en ti y en como fuimos construyendo el amor que tanto se siente ahora, el primer
    día que nos vimos, en donde hablamos por muchas más horas de la que nosotros esperábamos, te pase el calendario
    que nos dió un señor (en realidad lo compramos fksdjhfsdkj) y te fui a dejar a la micro en donde no pude evitar
    darte un abracito después de un dia tan lindo como ese. Después vinieron las otras citas en donde cada vez yo
    me sentía más atraído a ti, tanto física como emocionalmente (carita ojitos tiernos), tanto mi amor que las
    ganas de querer darte un beso me ganaron en la tercera cita. Fue pasando el tiempo y el amor seguía creciendo, 
    hasta ya se me salían solo los te amo, mi cariño por ti estaba explotando dentro de mi y hasta el día de hoy
    sigue pasando. Y AQUI ESTAMOS PO ayia, enamorados hasta las patas. Mi amor quiero acompañarte y cuidarte
    todo el tiempo, mi corazoncito me sigue diciendo que aki esssss (estrellitas) sdfhjksdf, te amo, jamás me cansaré
    de decirtelo<3
    
    Eres una personita muy fuerte y especial a quien admiro y amo muchisimoooooooo<3<3<3
    
    Ahora sigamos con el contrato ayia, en donde mi firma siempre va a estar<3
    
         
         """)


st.write('ia que andas x aki si quieres me puedes besar o dar un abracito<3')

col1, mid, col2 = st.columns([10,60,1])

with col1:
    beso_but = st.button('Bésame')
if beso_but:
    st.image(beso_im,width=300)
with mid:
    st.image(heart_im,width=30)

with col1:
    abrazo_but = st.button('Abrazame')
if abrazo_but:
    st.image(abrazo_im,width=300)
with mid:
    st.image(heart_im,width=30)


st.header("""
          
          YA! ahoraaaa como siempreee un quizzzzzz jijijiji<3
          
          """)
st.write('Veamos como andamos con las fechas (carita lente)')

#%%

d1 = datetime.date.today()
d2 = d1 + datetime.timedelta(days=1)
d3 = d2 + datetime.timedelta(days=1)
st.write('CUAL ES LA FECHA DEEEEEEEEE:')



first_date = st.date_input('Primera cita:', d1)
second_date = st.date_input('Segunda cita:', d2)
third_date = st.date_input('Tercera cita:', d3)
confirmar = st.button('Confirmar')

if first_date == datetime.date(2021,12,3) and second_date == datetime.date(2021,12,14) and third_date == datetime.date(2021,12,16) and confirmar:
    st.success('SHIII MI AMORRRR MUY BIENNN TE AMOOOOOOO')
    st.image(beso_im,width=300)
    col1, mid, col2 = st.columns([1,1,1])
    with col1:
        st.write('Gonzalo Rojas B.')
        st.write('Aquí está mi firma vida mía, te amo mucho <3')
    with col2:
        st.write('____________________')
        st.write('(Contrato versión digital, favor envíar firma por Instagram si desea firmar)')
elif confirmar:
    st.error('EQUIVOCADO MI AMOOOOR INTENTALO DE NUEVO<3')



















