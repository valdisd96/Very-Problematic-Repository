import numpy as np
from collections import Counter

class NearestNeighbors:
    def __init__(self, n_neighbors=3):
        self.n_neighbors = n_neighbors
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return np.array(predictions)

    def _predict(self, x):
        distances = np.linalg.norm(self.X_train - x, axis=1)
        k_indices = np.argsort(distances)[:self.n_neighbors]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

# Example usage:
# if __name__ == "__main__":
#     X_train = np.array([[1, 2], [2, 3], [3, 4], [5, 6]])
#     y_train = np.array([0, 0, 1, 1])
#     model = NearestNeighbors(n_neighbors=3)
#     model.fit(X_train, y_train)
#     X_test = np.array([[1, 2], [4, 5]])
#     predictions = model.predict(X_test)
#     print(predictions)