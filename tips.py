import pandas as pd
import streamlit as st

path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(path)
tips = pd.DataFrame(tips)

tot_tip_frame = tips[['total_bill','tip']]   # Связь чаевых и выручки за все время
group_frame = tips.groupby('day')[['tip', 'total_bill']].sum()   # Сумма чаевых и выручки по дням недели

st.title('Holla Holla Get a Dolla!💸')
page_name = ['Связь чаевых и выручки за все время 🌮', 'Сумма чаевых и выручки по дням недели 🌯']
page = st.radio('make a choice!', page_name)

if page == 'Связь чаевых и выручки за все время 🌮':
    st.subheader('Связь чаевых и выручки за все время 🌮')
    st.write('💵')
    st.area_chart(data = tot_tip_frame, width = 0, height= 0)
else:
    st.subheader('Сумма чаевых и выручки по дням недели 🌯')
    st.write('💶')
    st.bar_chart(data = group_frame, width = 0, height= 0)