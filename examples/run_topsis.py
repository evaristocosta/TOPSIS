import pandas as pd
from topsis import TOPSIS

# Load the data from the sample file
path = "examples/"
name= "Sample.xlsx"

Data = pd.read_excel(path + name)
Data.index = Data['Alternatives']
Data = Data.iloc[:, 1:]

# Define the weights and attribute types
weights = [0.2, 0.2, 0.2, 0.2, 0.2]
PC = [1, 1, 1, 1, 1] # 1 for profit, 0 for cost

# Run the TOPSIS algorithm
Output = TOPSIS(Data, weights, PC)

# Display the results
Scores=pd.DataFrame(Output[1])
Normalized_Weighted_Decision_Matrix = Output[0]
df=pd.concat([Normalized_Weighted_Decision_Matrix, Scores], axis=1)
print(df)