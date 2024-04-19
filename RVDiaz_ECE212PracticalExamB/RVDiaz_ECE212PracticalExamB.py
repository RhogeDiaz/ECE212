#Rhoge Vhir A. Diaz
#ECE 2A

import pandas as pd
import numpy as np

def matrixSum():
    # Load spreadsheet
    xl = pd.read_excel('matrices.xlsx', header=None)

    # hardcoding each cell
    m1_cells = [(2,1), (3,1), (4,1), (2,2), (3,2), (4,2), (2,3), (3,3), (4,3)]
    m2_cells = [(6,1), (7,1), (8,1), (6,2), (7,2), (8,2), (6,3), (7,3), (8,3)]

    # fetching each cell in a list
    m1_data = [xl.iloc[cell] for cell in m1_cells]
    m2_data = [xl.iloc[cell] for cell in m2_cells]

    # transforming to 3x3
    m1 = np.array(m1_data).reshape(3, 3)
    m2 = np.array(m2_data).reshape(3, 3)

    m_sum = m1 + m2

    return(m_sum)

if __name__ == "__main__":
    print(matrixSum())