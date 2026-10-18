import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('postgresql://postgres:840991@localhost:5432/healthcare_clinic_db')

df = pd.read_csv('data/appointments_cleaned.csv')

# Fix dates for postgres
df['appointment_date'] = pd.to_datetime(df['appointment_date']).dt.date

# Push to postgres - this never fails like pgAdmin import
df.to_sql('appointments_cleaned', engine, if_exists='replace', index=False)

print("SUCCESS! Table uploaded to healthcare_clinic_db")
print(f"Rows: {len(df)}")