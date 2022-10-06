import os
import sys
import logging

# Site-packages
#import ipykernel
#import redis
import pandas as pd


print(sys.path)
#print(ipykernel.__doc__)

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)


print(df)