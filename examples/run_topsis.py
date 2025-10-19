import pandas as pd
from topsis_hamedbaziyad import TOPSIS

# for running this example, you need the package 'openpyxl'

# Load the data from the sample file
file_name = "examples/sample.csv"

data = pd.read_csv(file_name)
data.index = data["Alternatives"]
data = data.iloc[:, 1:]

# Define the weights and attribute types
weights = [0.2, 0.2, 0.2, 0.2, 0.2]
PC = [1, 1, 1, 1, 1]  # 1 for profit, 0 for cost

# Run the TOPSIS algorithm
output = TOPSIS(data, weights, PC)
topsis_result = pd.DataFrame(output).sort_values(by=0, ascending=False)
topsis_result.columns = ["Performance Score"]

# Display the results
print(topsis_result)
