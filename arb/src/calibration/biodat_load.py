
import pandas as pd
from sklearn.model_selection import train_test_split

# KAGGLE bioresponse https://www.kaggle.com/c/bioresponse#Evaluation

train_url = 'https://raw.githubusercontent.com/quinn-dougherty/DS-Unit-3-Sprint-3-Big-Data/master/Bio-Response-Kaggle/data/train.csv'
# ignoring-- it doesn't have 'Activity'
test_url = 'https://raw.githubusercontent.com/quinn-dougherty/DS-Unit-3-Sprint-3-Big-Data/master/Bio-Response-Kaggle/data/test.csv'

df_ = pd.read_csv(train_url)
df_test = pd.read_csv(test_url)  # doesn't have 'Activity'
assert all([x == 0 for x in df_.isna().sum().values])
assert all([pd.api.types.is_numeric_dtype(df_[feat]) for feat in df_.columns])
dependent = 'Activity'

X_train, X_test, y_train, y_test = train_test_split(
    df_.drop(dependent, axis=1), df_[dependent], train_size=0.8, test_size=0.2)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

X = df_.drop(dependent, axis=1)
y = df_[dependent]
