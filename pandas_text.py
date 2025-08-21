import pandas as pd

# Create a simple Series
s = pd.Series([10, 20, 30, 40, 50])
print(s)

print(s.dtype)
print(s.values)
print(s.index)

s.name="calories"
print(s)

print(s[0:2])
print(s[1:3])

print(s.iloc[[1,3,4]]) #iloc-> location based indexing


index=["apple", "banana", "orange", "kiwi", "mango"]
s.index=index
print(s)

#grams of protein 
fruit_protein ={
    "Avocado": 2.0,       
    "Guava": 2.6,
    "Blackberries": 2.0,
    "Oranges": 0.9,
    "Banana": 1.1,
    "Apples": 0.3,
    "Kiwi": 1.1,
    "Pomegranate": 1.7,
    "Mango": 0.8,
    "Cherries": 1.0
}

s_protein = pd.Series(fruit_protein, name="protein")
print(s_protein)

print([s_protein>2])
# Conditional Selection


print(s_protein[s_protein > 2])
print(s_protein[(s_protein>0.5 )|(s_protein<=2.0)])


s_protein["mango"] = 3.2  # Example: updating it to 3.2 grams
print(s_protein)

# DataFrame:

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "Age": [25, 30, 35,44, 29, 25],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 70000, 62000, 56000, 50000]

}

df=pd.DataFrame(data)
print(df)

print(df.head(2) )# Display the first two rows
print(df.tail(2))  # Display the last two rows
print(df.shape)  # Get the shape of the DataFrame
print(df.describe)  # Get a summary of the DataFrame
df["Promoted Salary"] = df["Salary"] * 10
print(df)

#joins and merges
department_info = {
    "Dept": ["HR", "IT", "Finance"],
    "Location": ["New York", "San Francisco", "Chicago"],
    "Manager": ["Laura", "Steve", "Nina"]
}

df2 = pd.DataFrame(department_info)
print(df2)


#contect of the merge
print(pd.concat([df, df2]))

print(pd.concat([df, df2],axis=1))  # Concatenate along columns

# data = pd.read_csv("data.csv")     #import file
# print(data.head())  # Display the first few rows of the DataFrame