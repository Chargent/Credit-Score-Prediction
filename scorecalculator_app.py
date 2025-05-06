import streamlit as st
import pandas as pd
import joblib

st.write("# Welcome to Credit Score Calculator")
joblib_file = "rf_model.pkl"
model = joblib.load(joblib_file)
st.write("## Please fill in the following details to calculate your credit score:")
st.write("### Personal Information")

Month=st.selectbox("Month", ["January", "February", "March", "April", "May", "June", "July", "August"])

Occupation= st.selectbox("Occupation",['Manager' ,'Teacher' ,'Developer', 'Architect', 'Journalist', 'Scientist',
                                       'MediaManager' ,'Unemployed' ,'Lawyer' ,'Cleaner' ,'Farmer', 'Artist',
                                       'Accountant', 'Writer' ,'Engineer' ,'Entrepreneur', 'Doctor' ,'Musician',
                                       'Mechanic' ,'Student' ,'Pension'])

Annual_Income = st.number_input("Annual Income", min_value=0.0, value=0.0)

Monthly_Inhand_Salary = st.number_input("Monthly In-hand Salary", min_value=0.0, value=0.0)

Num_of_Bank_Accounts = st.number_input("Number of Bank Accounts", min_value=0, value=0)

Num_of_Credit_Card = st.number_input("Number of Credit Cards", min_value=0, value=0)

Interest_Rate = st.number_input("Interest Rate (%)", min_value=0.0, value=0.0)

Num_of_Loan = st.number_input("Number of Loans", min_value=0, value=0)

Delay_from_due_date = st.number_input("Delay From Due Date (days)", min_value=0, value=0)

Num_of_Delayed_Payment = st.number_input("Number of Delayed Payments", value=0)

Changed_Credit_Limit = st.number_input("Changed Credit Limit", min_value=0.0, value=0.0)

Num_Credit_Inquiries = st.number_input("Number of Credit Inquiries", min_value=0, value=0)

Outstanding_Debt = st.number_input("Outstanding Debt", min_value=0.0, value=0.0)

Credit_Utilization_Ratio = st.number_input("Credit Utilization Ratio", min_value=0.0, value=0.0)

Credit_History_Age_ = st.number_input("Credit History Age (months)", min_value=0, value=0)

Payment_of_Min_Amount = st.selectbox("Payment of Minimum Amount", ["Yes", "No"])

Amount_invested_monthly = st.number_input("Amount Invested Monthly", min_value=0.0, value=0.0)

Payday_Loan = st.number_input("Payday Loan", min_value=0.0, value=0.0)
Home_Equity_Loan = st.number_input("Home Equity Loan", min_value=0.0, value=0.0)
Personal_Loan = st.number_input("Personal Loan", min_value=0.0, value=0.0)
Credit_Builder_Loan = st.number_input("Credit Builder Loan", min_value=0.0, value=0.0)
Debt_Consolidation_Loan = st.number_input("Debt Consolidation Loan", min_value=0.0, value=0.0)
Student_Loan = st.number_input("Student Loan", min_value=0.0, value=0.0)
Auto_Loan = st.number_input("Auto Loan", min_value=0.0, value=0.0)
Mortgage_Loan = st.number_input("Mortgage Loan", min_value=0.0, value=0.0)
Not_Specified = st.number_input("Not Specified", min_value=0.0, value=0.0)
No_Loan = st.number_input("No Loan", min_value=0.0, value=0.0)


Credit_Mix = st.selectbox( "Credit Mix", ["Good", "Standard", "Bad"])




# Run the model
if st.button("Calculate Credit Score"):
    # Convert categorical variables to numerical
    credit_mix_mapping = {"Good": 0, "Standard": 1, "Bad": 2}
    month_mapping = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8}

    occupation_mapping = {'Accountant': 0,'Architect': 1,'Artist': 2, 'Cleaner': 3,'Developer': 4, 'Doctor': 5,
                                          'Engineer': 6, 'Entrepreneur': 7, 'Farmer': 8, 'Journalist': 9, 'Lawyer': 10,
                                            'Manager': 11, 'Mechanic': 12, 'MediaManager': 13, 'Musician': 14, 'Pension': 15,
                                              'Scientist': 16, 'Student': 17, 'Teacher': 18, 'Unemployed': 19,'Writer': 20}
    

    Payment_of_Min_Amount_mapping = {"Yes": 1, "No": 0}


    Credit_Mix_Bad=(1 if Credit_Mix == "Bad" else 0)
    Credit_Mix_Good=(1 if Credit_Mix == "Good" else 0)
    Credit_Mix_Standard=(1 if Credit_Mix == "Standard" else 0)




#input the data in the empty dataframe
    input_df = pd.DataFrame({
        'Month': month_mapping[Month],
        'Occupation': occupation_mapping[Occupation],
        'Annual_Income': Annual_Income,
        'Monthly_Inhand_Salary': Monthly_Inhand_Salary,
        'Num_Bank_Accounts': Num_of_Bank_Accounts,
        'Num_Credit_Card': Num_of_Credit_Card,
        'Interest_Rate': Interest_Rate,
        'Num_of_Loan': Num_of_Loan,
        'Delay_from_due_date': Delay_from_due_date,
        'Num_of_Delayed_Payment': Num_of_Delayed_Payment,
        'Changed_Credit_Limit': Changed_Credit_Limit,
        'Num_Credit_Inquiries': Num_Credit_Inquiries,
        'Outstanding_Debt': Outstanding_Debt,
        'Credit_Utilization_Ratio': Credit_Utilization_Ratio,
        'Credit_History_Age': Credit_History_Age_,
        'Payment_of_Min_Amount': Payment_of_Min_Amount_mapping[Payment_of_Min_Amount],
        'Amount_invested_monthly': Amount_invested_monthly,
        'Payday Loan': Payday_Loan,
        'Home Equity Loan': Home_Equity_Loan,
        'Personal Loan': Personal_Loan,
        'Credit-Builder Loan': Credit_Builder_Loan,
        'Debt Consolidation Loan': Debt_Consolidation_Loan,
        'Student Loan': Student_Loan,
        'Auto Loan': Auto_Loan,
        'Mortgage Loan': Mortgage_Loan,
        'Not Specified': Not_Specified,
        'No Loan': No_Loan,
        'Credit_Mix_Bad': Credit_Mix_Bad,
        'Credit_Mix_Good': Credit_Mix_Good,
        'Credit_Mix_Standard': Credit_Mix_Standard
    }, index=[0])






    # Make prediction
    prediction = model.predict(input_df)
    st.write(f"Your predicted credit score is: {prediction[0]}")
st.write("## Model Information")
st.write("This model is a Random Forest Classifier trained on a dataset of credit scores. It takes into account various factors such as age, outstanding debt, credit mix, and number of credit cards to predict your credit score.")
st.write("## Disclaimer")
st.write("This is a simulated credit score calculator and should not be used for actual credit decisions. Please consult a financial advisor for accurate credit assessments.")
st.write("## About the Model")
st.write("The model was trained on a dataset of credit scores and uses a Random Forest Classifier to predict the credit score based on the input features. The model is not perfect and may not accurately predict your actual credit score.")


