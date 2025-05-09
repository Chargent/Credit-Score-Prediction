import streamlit as st
import pandas as pd
import joblib
joblib_file = "rf_model.pkl"
model = joblib.load(joblib_file)

st.set_page_config(
    page_title="Credit Score Calculator", page_icon="💳")


st.sidebar.title("💳 Credit Score Calculator")
st.sidebar.write(
    "Estimate your credit score by filling out the form on this page. "
    "Your data never leaves your browser."
)

if st.sidebar.checkbox("Show quick tips"):
    st.sidebar.info(
        """
        • Provide realistic figures for best results.
        • Revisit any tab to adjust inputs before calculating.
        """
    )
st.title("Welcome to Credit Score Calculator")
st.subheader("Please fill in the following details:")

personal_tab, loan_tab = st.tabs([
    "👤 Personal & Financial", "🏦 Loan Portfolio"
])

with personal_tab:
    Month=st.select_slider("Month", ["January", "February", "March", "April", "May", "June", "July", "August"])
    Occupation= st.segmented_control("Occupation",['Manager' ,'Teacher' ,'Developer', 'Architect', 'Journalist','Scientist',
                                           'MediaManager' ,'Unemployed' ,'Lawyer' ,'Cleaner' ,'Farmer', 'Artist','Student'
                                            'Accountant', 'Writer' ,'Engineer' ,'Entrepreneur', 'Doctor' ,'Musician','Mechanic' ,'Pension'])
    
    Credit_Mix = st.pills( "Credit Mix", ["Bad","Standard","Good" ])

    Payment_of_Min_Amount = st.pills("Payment of Minimum Amount", ["Yes", "No"])

    Annual_Income = st.number_input("Annual Income", min_value=0.0, value=0.0)

    Monthly_Inhand_Salary = st.number_input("Monthly In-hand Salary", min_value=0.0, value=0.0)

    Num_of_Bank_Accounts = st.number_input("Number of Bank Accounts", min_value=0, value=0,step=1)

    Num_of_Credit_Card = st.number_input("Number of Credit Cards", min_value=0, value=0,step=1)
    
    Interest_Rate = st.number_input("Interest Rate (%)", min_value=0.0, value=0.0)
    
    Num_of_Loan = st.number_input("Number of Loans", min_value=0, value=0)
    
    Delay_from_due_date = st.number_input("Delay From Due Date (days)", value=0,step=1)
    
    Num_of_Delayed_Payment = st.number_input("Number of Delayed Payments",min_value=0 ,value=0,step=1)
    
    Changed_Credit_Limit = st.number_input("Changed Credit Limit", min_value=0.0, value=0.0)
    
    Num_Credit_Inquiries = st.number_input("Number of Credit Inquiries", min_value=0, value=0)
    
    Outstanding_Debt = st.number_input("Outstanding Debt", min_value=0.0, value=0.0)
    
    Credit_Utilization_Ratio = st.number_input("Credit Utilization Ratio", min_value=0.0, value=0.0)
    
    Credit_History_Age_ = st.number_input("Credit History Age (months)", min_value=0, value=0,step=1)
    
    Amount_invested_monthly = st.number_input("Amount Invested Monthly", min_value=0.0, value=0.0)



with loan_tab:

    Payday_Loan = st.slider("Payday Loan", min_value=0,max_value=10, value=0,step=1)
    Home_Equity_Loan = st.slider("Home Equity Loan", min_value=0,max_value=10,value=0,step=1)
    Personal_Loan = st.slider("Personal Loan", min_value=0,max_value=10, value=0,step=1)
    Credit_Builder_Loan = st.slider("Credit Builder Loan", min_value=0,max_value=10, value=0,step=1)
    Debt_Consolidation_Loan = st.slider("Debt Consolidation Loan", min_value=0,max_value=10, value=0,step=1)
    Student_Loan = st.slider("Student Loan", min_value=0,max_value=10, value=0,step=1)
    Auto_Loan = st.slider("Auto Loan", min_value=0,max_value=10, value=0,step=1)
    Mortgage_Loan = st.slider("Mortgage Loan", min_value=0,max_value=10, value=0,step=1)
    Not_Specified = st.slider("Not Specified", min_value=0,max_value=10, value=0,step=1)
    No_Loan = st.slider("No Loan", min_value=0,max_value=10, value=0,step=1)





#run the model
if st.button("Calculate Credit Score"):
    # Convert for data inputing

    Credit_Mix_mapping = {"Good": 2, "Standard": 1, "Bad": 0}

    month_mapping = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8}

    
    

    Payment_of_Min_Amount_mapping = {"Yes": 1, "No": 0}


    Occupation_Accountant   = (1 if Occupation == 'Accountant'    else 0)
    Occupation_Architect    = (1 if Occupation == 'Architect'     else 0)
    Occupation_Artist       = (1 if Occupation == 'Artist'        else 0)
    Occupation_Cleaner      = (1 if Occupation == 'Cleaner'       else 0)
    Occupation_Developer    = (1 if Occupation == 'Developer'     else 0)
    Occupation_Doctor       = (1 if Occupation == 'Doctor'        else 0)
    Occupation_Engineer     = (1 if Occupation == 'Engineer'      else 0)
    Occupation_Entrepreneur = (1 if Occupation == 'Entrepreneur'  else 0)
    Occupation_Farmer       = (1 if Occupation == 'Farmer'        else 0)
    Occupation_Journalist   = (1 if Occupation == 'Journalist'    else 0)
    Occupation_Lawyer       = (1 if Occupation == 'Lawyer'        else 0)
    Occupation_Manager      = (1 if Occupation == 'Manager'       else 0)
    Occupation_Mechanic    = (1 if Occupation == 'Mechanic'      else 0)
    Occupation_MediaManager = (1 if Occupation == 'MediaManager'  else 0)
    Occupation_Musician     = (1 if Occupation == 'Musician'      else 0)
    Occupation_Pension      = (1 if Occupation == 'Pension'       else 0)
    Occupation_Scientist    = (1 if Occupation == 'Scientist'     else 0)
    Occupation_Student      = (1 if Occupation == 'Student'       else 0)
    Occupation_Teacher      = (1 if Occupation == 'Teacher'       else 0)
    Occupation_Unemployed   = (1 if Occupation == 'Unemployed'    else 0)
    Occupation_Writer       = (1 if Occupation == 'Writer'        else 0)






#Create a DataFrame for the input data
    input_df = pd.DataFrame({
    'Month':                            month_mapping[Month],
    'Annual_Income':                    Annual_Income,
    'Monthly_Inhand_Salary':            Monthly_Inhand_Salary,
    'Num_Bank_Accounts':                Num_of_Bank_Accounts,
    'Num_Credit_Card':                  Num_of_Credit_Card,
    'Interest_Rate':                    Interest_Rate,
    'Num_of_Loan':                      Num_of_Loan,
    'Delay_from_due_date':              Delay_from_due_date,
    'Num_of_Delayed_Payment':           Num_of_Delayed_Payment,
    'Changed_Credit_Limit':             Changed_Credit_Limit,
    'Num_Credit_Inquiries':             Num_Credit_Inquiries,
    'Credit_Mix':                       Credit_Mix_mapping[Credit_Mix],
    'Outstanding_Debt':                 Outstanding_Debt,
    'Credit_Utilization_Ratio':         Credit_Utilization_Ratio,
    'Credit_History_Age':               Credit_History_Age_,
    'Payment_of_Min_Amount':            Payment_of_Min_Amount_mapping[Payment_of_Min_Amount],
    'Amount_invested_monthly':          Amount_invested_monthly,
    
    'No Loan':                          No_Loan,
    'Mortgage Loan':                    Mortgage_Loan,
    'Credit-Builder Loan':              Credit_Builder_Loan,
    'Personal Loan':                    Personal_Loan,
    'Payday Loan':                      Payday_Loan,
    'Home Equity Loan':                 Home_Equity_Loan,
    'Auto Loan':                        Auto_Loan,
    'Student Loan':                     Student_Loan,
    'Not Specified':                    Not_Specified,
    'Debt Consolidation Loan':          Debt_Consolidation_Loan,
    
    'Occupation_Accountant':            Occupation_Accountant,
    'Occupation_Architect':             Occupation_Architect,
    'Occupation_Artist':                Occupation_Artist,
    'Occupation_Cleaner':               Occupation_Cleaner,
    'Occupation_Developer':             Occupation_Developer,
    'Occupation_Doctor':                Occupation_Doctor,
    'Occupation_Engineer':              Occupation_Engineer,
    'Occupation_Entrepreneur':          Occupation_Entrepreneur,
    'Occupation_Farmer':                Occupation_Farmer,
    'Occupation_Journalist':            Occupation_Journalist,
    'Occupation_Lawyer':                Occupation_Lawyer,
    'Occupation_Manager':               Occupation_Manager,
    'Occupation_Mechanic':              Occupation_Mechanic,
    'Occupation_MediaManager':          Occupation_MediaManager,
    'Occupation_Musician':              Occupation_Musician,
    'Occupation_Pension':               Occupation_Pension,
    'Occupation_Scientist':             Occupation_Scientist,
    'Occupation_Student':               Occupation_Student,
    'Occupation_Teacher':               Occupation_Teacher,
    'Occupation_Unemployed':            Occupation_Unemployed,
    'Occupation_Writer':                Occupation_Writer

     
    }, index=[0])






    # Make prediction
    prediction = model.predict(input_df)
    
    # Display the result beautifully
    st.markdown("### Your Predicted Credit Score")
    st.success(f"💳 **{prediction[0]}**")
    
    st.markdown("---")
    st.info(
        """
        **What does this mean?**
        - A higher credit score indicates better creditworthiness.
        - Use this score as a guideline and consult a financial advisor for detailed insights.
        """
    )

st.write("## Disclaimer")
st.write("This is a simulated credit score calculator and should not be used for actual credit decisions. Please consult a financial advisor for accurate credit assessments.")
st.write("## About the Model")
st.write("The model was trained on a dataset of credit scores and uses a Random Forest Classifier to predict the credit score based on the input features. The model is not perfect and may not accurately predict your actual credit score.")


