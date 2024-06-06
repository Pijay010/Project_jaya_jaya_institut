import pandas as pd
import streamlit as st
import joblib
from preprocessing import data_preprocessing, encoding_course, encoding_debtor, encoding_application_mode, encoding_tuition_fees_up_to_date, encoding_scholarship_holder
from prediction import prediction

st.header('Students Performance Prediction')

data = pd.DataFrame()
col1, col2, col3 = st.columns(3)
with col1 :
    application_mode = st.selectbox(label='Application Mode (Select)', options=encoding_application_mode.classes_, index=1)
    data['application_mode'] = [application_mode]
with col1:
    course = st.selectbox(label='Course (Select)', options=encoding_course.classes_, index=1)
    data['course'] = [course]
with col1 :
    debtor = st.selectbox(label='Debtor (Yes/No)', options=encoding_debtor.classes_, index=1)
    data['debtor'] = [debtor]

col1, col2, col3 = st.columns(3)
with col1:
    tuition_fees_up_to_date = st.selectbox(label='tuition_fees_up_to_date (Yes/No)', options=encoding_tuition_fees_up_to_date.classes_, index=1)
    data['tuition_fees_up_to_date'] = [tuition_fees_up_to_date]
with col1:
    scholarship_holder = st.selectbox(label='scholarship_holder (Select)', options=encoding_scholarship_holder.classes_, index=1)
    data['scholarship_holder'] = [scholarship_holder]
with col1:
    age_at_enrollment = int(st.number_input(label='age_at_enrollment (Input)', value=20))
    data['age_at_enrollment'] = [age_at_enrollment]

col1, col2, col3 = st.columns(3)
with col1:
    GDP = float(st.number_input(label='Gross Domestic Product (Input)', value=0))
    data['GDP'] = [GDP]
with col1:
    curricular_units_1st_sem_approved = int(st.number_input(label='curricular_units_1st_sem_approved (input)', value=0))
    data['curricular_units_1st_sem_approved'] = [curricular_units_1st_sem_approved]
with col1:
    curricular_units_1st_sem_grade = float(st.number_input(label='curricular_units_1st_sem_grade (Input)', value=0))
    data['curricular_units_1st_sem_grade'] = [curricular_units_1st_sem_grade]


col1, col2= st.columns(2)
with col1:
    curricular_units_2nd_sem_approved = int(st.number_input(label='curricular_units_2nd_sem_approved (Input)', value=0))
    data['curricular_units_2nd_sem_approved'] = [curricular_units_2nd_sem_approved]
with col1:
    curricular_units_2nd_sem_grade = float(st.number_input(label='curricular_units_2nd_sem_grade (Input)', value=0))
    data['curricular_units_2nd_sem_grade'] = [curricular_units_2nd_sem_grade]

with st.expander('Evaluating the Data'):
    st.dataframe(data=data, width= 950, height=15)

if st.button('Predict'):
    data_baru = data_preprocessing(data=data)
    with st.expander('View the Preprocessing Data'):
        st.dataframe(data=data_baru, width=800, height=15)
        st.write('Students Performance: {}'.format(prediction(data_baru)))