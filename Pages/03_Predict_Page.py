import streamlit as st
import pandas as pd
import joblib
import os
import datetime

st.set_page_config(
    page_title='Predict Page',
    page_icon=':',
    layout='wide'
)

# Load models
@st.cache_data(show_spinner=False)
def decision_tree_pipeline():
    model = joblib.load('./models/decision_tree_pipeline.pkl')
    return model, "Decision Tree"

@st.cache_data(show_spinner=False)
def logistic_regression_pipeline():
    model = joblib.load('./models/logistic_regression_pipeline.pkl')
    return model, "Logistic Regression"

@st.cache_data(show_spinner=False)
def random_forest_pipeline():
    model = joblib.load('./models/random_forest_pipeline.pkl')
    return model, "Random Forest"

@st.cache_data(show_spinner=False)
def load_encoder():
    encoder = joblib.load('./models/label_encoder.pkl')
    return encoder

def select_model():
    column1, column2 = st.columns(2)
    
    with column1:
        model_name = st.selectbox('Select a Model', options=['Decision Tree', 'Logistic Regression', 'Random Forest'])
        if model_name == 'Decision Tree':
            selected_model, model_display_name = decision_tree_pipeline()   
        elif model_name == 'Logistic Regression':
            selected_model, model_display_name = logistic_regression_pipeline()
        else:
            selected_model, model_display_name = random_forest_pipeline()
        
        encoder = load_encoder()
    with column2:
        pass
        
    return selected_model, encoder, model_display_name

if 'prediction' not in st.session_state:
    st.session_state['prediction'] = None
            
if 'probability' not in st.session_state:
    st.session_state['probability'] = None
        
def make_prediction(model, encoder, model_display_name):
    # Make prediction
    df = st.session_state['df']
    prediction = model.predict(df)
    prediction = int(prediction[0])
    prediction = encoder.inverse_transform([prediction])
    
    df['Prediction Time'] = datetime.date.today()
    df['Model Used'] = model_display_name
    
    history_dir = './history_data'
    if not os.path.exists(history_dir):
        os.makedirs(history_dir)
    
    df.to_csv(os.path.join(history_dir, 'history.csv'), mode='a', header=not os.path.exists(os.path.join(history_dir, 'history.csv')), index=False)

    # Get probabilities
    probability = model.predict_proba(df)
    
    # Updating state
    st.session_state['prediction'] = prediction
    st.session_state['probability'] = probability
  
    if 'probability' not in st.session_state:
        st.session_state['probability'] = None 

    return prediction

def predict():
    # Dictionary to store input features
    model, encoder, model_display_name = select_model()
    
    with st.form('input feature'):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.write('### Personal Information')
            # Add input fields and store values in input_features dictionary
            gender = st.selectbox('gender', options=['Male', 'Female'], key='gender')
            SeniorCitizen = st.selectbox('SeniorCitizen', options=['Yes', 'No'], key='SeniorCitizen')
            Partner = st.selectbox('Partner', options=['Yes', 'No'], key='Partner')
            Dependents = st.selectbox('Dependents', options=['Yes', 'No'], key='Dependents')
            tenure = st.number_input('tenure', min_value=0, max_value=71, step=1, key='tenure')  
        
        with col2:
            st.write('### Subscriptions')
            # input fields for subscription-related features
            PhoneService = st.selectbox('PhoneService', options=['Yes', 'No'], key='PhoneService') 
            MultipleLines = st.selectbox('MultipleLines', options=['Yes', 'No'], key='MultipleLines') 
            InternetService = st.selectbox('InternetService', options=['Fiber optic', 'DSL'], key='InternetService') 
            OnlineSecurity = st.selectbox('OnlineSecurity', options=['Yes', 'No'], key='OnlineSecurity') 
            
        with col3:  
            st.write('### Additional Subscriptions')
            OnlineBackup = st.selectbox('OnlineBackup', options=['Yes', 'No'], key='OnlineBackup')
            DeviceProtection = st.selectbox('DeviceProtection', options=['Yes', 'No'], key='DeviceProtection') 
            TechSupport = st.selectbox('TechSupport', options=['Yes', 'No'], key='TechSupport') 
            StreamingTV = st.selectbox('StreamingTV', options=['Yes', 'No'], key='StreamingTV') 
            StreamingMovies = st.selectbox('StreamingMovies', options=['Yes', 'No'], key='StreamingMovies')  
        
        with col4:
            st.write('### Payment Options')
            # input fields for payment-related features
            Contract = st.selectbox('Contract', options=['Month-to-month', 'Two year', 'One year'], key='Contract') 
            PaperlessBilling = st.selectbox('PaperlessBilling', options=['Yes', 'No'], key='PaperlessBilling') 
            PaymentMethod = st.selectbox('PaymentMethod', options=['Electronic check', 'Credit card (automatic)', 'Mailed check', 'Bank transfer (automatic)'], key='PaymentMethod') 
            MonthlyCharges = st.number_input('MonthlyCharges', min_value=0, key='MonthlyCharges')
            TotalCharges = st.number_input('TotalCharges', min_value=0, key='TotalCharges') 
   
        input_features = pd.DataFrame({
            'gender': [gender], 
            'SeniorCitizen': [SeniorCitizen], 
            'Partner': [Partner], 
            'Dependents': [Dependents], 
            'tenure': [tenure],
            'PhoneService': [PhoneService],
            'MultipleLines': [MultipleLines], 
            'InternetService': [InternetService],
            'OnlineSecurity': [OnlineSecurity],
            'OnlineBackup': [OnlineBackup], 
            'DeviceProtection': [DeviceProtection], 
            'TechSupport': [TechSupport], 
            'StreamingTV': [StreamingTV],
            'StreamingMovies': [StreamingMovies], 
            'Contract': [Contract], 
            'PaperlessBilling': [PaperlessBilling], 
            'PaymentMethod': [PaymentMethod],
            'MonthlyCharges': [MonthlyCharges], 
            'TotalCharges': [TotalCharges]
        })
        
        st.session_state['df'] = input_features
        st.form_submit_button('Make Prediction', on_click=make_prediction, kwargs=dict(model=model, encoder=encoder, model_display_name=model_display_name))
   
# Call the data function directly
if __name__ == '__main__':
    st.title('Make a Prediction')
    predict()
    
    prediction = st.session_state['prediction']
    probability = st.session_state['probability']
           
    if not prediction:
        st.markdown("### Prediction will show here")
    elif prediction == "Yes":
        probability_of_yes = probability[0][1] * 100
        st.markdown(f"### The employee will leave the company with a probability of {probability_of_yes}%")
    else:
        probability_of_no = probability[0][0] * 100
        st.markdown(f"### Employee will not leave with a probability of {round(probability_of_no, 2)}%")
