import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Display first rows
print(df.head())

# Total customers
print("Total Customers:", df.shape[0])

# -----------------------------
# 1. Customer Churn Count
# -----------------------------
df['Churn'].value_counts().plot(kind='bar')
plt.title('Customer Churn Count')
plt.xlabel('Churn')
plt.ylabel('Count')
plt.savefig('images/churn_count.png')
plt.show()

# -----------------------------
# 2. Gender Distribution
# -----------------------------
df['gender'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title('Gender Distribution')
plt.ylabel('')
plt.savefig('images/gender_distribution.png')
plt.show()

# -----------------------------
# 3. Contract Type Analysis
# -----------------------------
df['Contract'].value_counts().plot(kind='bar')

plt.title('Contract Type Distribution')
plt.xlabel('Contract Type')
plt.ylabel('Count')
plt.savefig('images/contract_type_analysis.png')
plt.show()

# -----------------------------
# 4. Internet Service Analysis
# -----------------------------
df['InternetService'].value_counts().plot(kind='bar')

plt.title('Internet Service Distribution')
plt.xlabel('Internet Service')
plt.ylabel('Count')
plt.savefig('images/internet_service_analysis.png')
plt.show()

# -----------------------------
# 5. Payment Method Analysis
# -----------------------------
df['PaymentMethod'].value_counts().plot(kind='bar')

plt.title('Payment Method Distribution')
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.savefig('images/payment_method_analysis.png')
plt.show()

# -----------------------------
# 6. Monthly Charges Histogram
# -----------------------------

df['MonthlyCharges'].plot(kind='hist', bins=20)

plt.title('Monthly Charges Distribution')
plt.xlabel('Monthly Charges')
plt.savefig('images/monthly_charges_distribution.png')
plt.show()

# -----------------------------
# 7. Tenure Analysis
# -----------------------------
df.groupby('tenure')['MonthlyCharges'].mean().plot(kind='line')

plt.title('Monthly Charges by Tenure')
plt.xlabel('Tenure')
plt.ylabel('Average Monthly Charges')
plt.savefig('images/monthly_charges_tenure.png')
plt.show()

print("All charts generated successfully!")