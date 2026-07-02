hours = [1, 2, 3, 4, 5]
marks = [25, 35, 45, 55, 65]

X = [[1], [2], [3], [4], [5]]
y = [25, 35, 45, 55, 65]

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)
print("Model trained!")

z=[[6]]

print(model.predict(z))