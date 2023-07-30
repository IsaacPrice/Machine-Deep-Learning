from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load iris dataset as an example
iris = load_iris()
X, y = iris.data, iris.target

# Split the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a base classifier (here we use K-Nearest Neighbors)
base_cls = KNeighborsClassifier()

# Instantiate the BaggingClassifier with the base classifier
bagging_cls = BaggingClassifier(base_estimator=base_cls, n_estimators=10, random_state=42)

# Fit the BaggingClassifier to the training data
bagging_cls.fit(X_train, y_train)

# Predict the responses for the test set
y_pred = bagging_cls.predict(X_test)

# Check the accuracy
print('Accuracy:', accuracy_score(y_test, y_pred))