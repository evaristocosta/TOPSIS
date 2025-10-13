import pandas as pd
from topsis.main import TOPSIS

def test_topsis():
    # Create a sample decision matrix
    data = {
        'Alternatives': ['A1', 'A2', 'A3', 'A4'],
        'C1': [10, 12, 15, 8],
        'C2': [8, 9, 11, 10],
        'C3': [7, 10, 8, 9]
    }
    decision_matrix = pd.DataFrame(data).set_index('Alternatives')

    # Define the weights and attribute types
    weights = [0.4, 0.3, 0.3]
    attribute_types = [1, 1, 0] # 1 for profit, 0 for cost

    # Run the TOPSIS algorithm
    topsis_result = TOPSIS(decision_matrix, weights, attribute_types)

    # Display the results
    print(topsis_result)

    assert topsis_result is not None
