from datasets import load_housing_data
from datasets import fetch_housing_data
from sklearn.model_selection import train_test_split


housing = load_housing_data()
train_set, test_set = train_test_split(housing, test_size=0.2,random_state=42)