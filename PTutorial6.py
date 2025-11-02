# Q1.1
import pandas as pd
print(pd.__version__)

# Q1.2
data = {'Name': ['x', 'Y', 'Z'], 'Age': [25, 30, 35], 'City': ['A', 'B', 'C']}
df = pd.DataFrame(data)
print(df)

# Q2.1
S1 = pd.Series([100, 200, 300, 400, 500])
print(S1)

# Q2.2
print(S1[1])
print(S1[3])

# Q2.3
S2 = pd.Series([10, 20, 30, 40, 50])
print(S1 + S2)

# Q3.1
print(df[['Name', 'City']])

# Q3.2
df['Salary'] = [50000, 60000, 70000]
print(df)

# Q3.3
print(df['Age'].mean())
print(df['Salary'].sum())

# Q4.1
print(df[df['Age'] > 28])

# Q4.2
df = df.set_index('Name')
print(df)
df = df.reset_index()
print(df)

# Q5.1
emp = pd.read_csv('employees.csv')
print(emp)

# Q5.2
filtered = emp[emp['Salary'] > 55000]
print(filtered[['Name', 'Department']])

# Q6.1
print(emp.groupby('Department')['Salary'].mean())

# Q6.2
print(emp.groupby('Department')['Salary'].agg(['min', 'max']))

# Q7.1
df1 = pd.DataFrame({'Name': ['John', 'Jane', 'Emily'], 'Department': ['Sales', 'Marketing', 'HR']})
df2 = pd.DataFrame({'Name': ['John', 'Jane', 'Emily'], 'Experience (Years)': [5, 7, 3]})
merged = pd.merge(df1, df2, on='Name')
print(merged)

# Q8.1
print(merged.sort_values(by='Experience (Years)', ascending=False))
