import pandas as pd
from snsql import *

pums = pd.read_csv("https://raw.githubusercontent.com/opendifferentialprivacy/dp-test-datasets/master/data/PUMS_california_demographics_1000/data.csv")

print(pums)


# Adopted from https://github.com/opendp/smartnoise-sdk/blob/main/datasets/PUMS.yaml
metadata = {
  "PUMS": {
    "PUMS": {
      "PUMS": {
        "row_privacy": True,
        "rows": 1000,
        "age": {
          "type": "int",
          "lower": 0,
          "upper": 100
        },
        "sex": {
          "type": "string"
        },
        "educ": {
          "type": "string"
        },
        "race": {
          "type": "string"
        },
        "income": {
          "type": "int",
          "lower": 0,
          "upper": 500000
        },
        "married": {
          "type": "string"
        }
      }
    }
  }
}

private_reader = from_connection(
    pums, metadata=metadata,
    privacy=Privacy(epsilon=1.0, delta=1/1000)
)

query = 'SELECT married, COUNT(*) AS n FROM PUMS.PUMS GROUP BY married'

result_dp = private_reader.execute_df(query)
print(result_dp)