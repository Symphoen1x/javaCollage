import pandas as pd


mytest = {
    'men': [0.2, 0.4, "true"],
    'women': ["sui", " ", ]}
outs = pd.DataFrame(mytest)
print(outs)
