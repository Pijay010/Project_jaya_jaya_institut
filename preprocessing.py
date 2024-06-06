import numpy as np
import pandas as pd
import joblib

encoding_application_mode = joblib.load('encoding_application_mode.joblib')
encoding_course = joblib.load('encoding_course.joblib')
encoding_debtor = joblib.load('encoding_debtor.joblib')
encoding_tuition_fees_up_to_date = joblib.load('encoding_tuition_fees_up_to_date.joblib')
encoding_scholarship_holder = joblib.load('encoding_scholarship_holder.joblib')
scaling_age_at_enrollment = joblib.load('scaling_age_at_enrollment.joblib')
scaling_GDP = joblib.load('scaling_GDP.joblib')
pca_model = joblib.load('pca.joblib')

scaling_curricular_units_1st_sem_approved = joblib.load('scaling_curricular_units_1st_sem_approved.joblib')
scaling_curricular_units_1st_sem_grade = joblib.load('scaling_curricular_units_1st_sem_grade.joblib')
scaling_curricular_units_2nd_sem_approved = joblib.load('scaling_curricular_units_2nd_sem_approved.joblib')
scaling_curricular_units_2nd_sem_grade = joblib.load('scaling_curricular_units_2nd_sem_grade.joblib')

pca_columns = ['curricular_units_1st_sem_approved', 'curricular_units_1st_sem_grade', 'curricular_units_2nd_sem_approved', 'curricular_units_2nd_sem_grade']

def data_preprocessing(data):
    data = data.copy()
    df = pd.DataFrame()
    df['application_mode'] = encoding_application_mode.transform(data['application_mode'])
    df['course'] = encoding_course.transform(data['course'])
    df['debtor'] = encoding_debtor.transform(data['debtor'])
    df['tuition_fees_up_to_date'] = encoding_tuition_fees_up_to_date.transform(data['tuition_fees_up_to_date'])
    df['scholarship_holder'] = encoding_scholarship_holder.transform(data['scholarship_holder'])
    df['age_at_enrollment'] = scaling_age_at_enrollment.transform(np.asarray(data['age_at_enrollment']).reshape(-1,1))[0]
    df['GDP'] = scaling_GDP.transform(np.asarray(data['GDP']).reshape(-1,1))[0]
 
    #PCA
    data['curricular_units_1st_sem_approved'] = scaling_curricular_units_1st_sem_approved.transform(np.asarray(data['curricular_units_1st_sem_approved']).reshape(-1,1))[0]
    data['curricular_units_1st_sem_grade'] = scaling_curricular_units_1st_sem_grade.transform(np.asarray(data['curricular_units_1st_sem_grade']).reshape(-1,1))[0]
    data['curricular_units_2nd_sem_approved'] = scaling_curricular_units_2nd_sem_approved.transform(np.asarray(data['curricular_units_2nd_sem_approved']).reshape(-1,1))[0]
    data['curricular_units_2nd_sem_grade'] = scaling_curricular_units_1st_sem_approved.transform(np.asarray(data['curricular_units_2nd_sem_grade']).reshape(-1,1))[0]

    df[['pc1_1','pc1_2','pc1_3']] = pca_model.transform(data[pca_columns])

    return df