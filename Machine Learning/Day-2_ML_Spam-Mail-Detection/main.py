# Import libraries
import numpy as np
import pandas as pd
import os

# # Explore input directory (Kaggle setup)
# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

# Load dataset
data = pd.read_csv('data.csv')

# Inspect dataset
print(data.info())
print(data.isna().sum())

# Add binary spam column
data['Spam'] = data['Category'].apply(lambda x: 1 if x == 'spam' else 0)
print(data.head(5))

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    data.Message, data.Spam, test_size=0.25
)

# Vectorizer + Naive Bayes pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

clf = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])

# Train model
clf.fit(X_train, y_train)

# # Test predictions
# emails = [
#     'Sounds great! Are you home now?',
#     'Will u meet ur dream partner soon? Is ur career off 2 a flyng start? 2 find out free, txt HORO followed by ur star sign, e. g. HORO ARIES'
# ]

# print(clf.predict(emails))

# # Model accuracy
# print("Accuracy:", clf.score(X_test, y_test))


message = input("Enter a message: ")

prediction = clf.predict([message])

if prediction[0] == 1:
    print("Spam")
else:
    print("Not Spam")