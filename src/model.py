# src/model.py
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class WineModel:
    def __init__(self, n_estimators=100, random_state=42):
        self.n_estimators = n_estimators
        self.random_state = random_state
        self.model = RandomForestClassifier(
            n_estimators=self.n_estimators,
            random_state=self.random_state
        )
        self._load_data()

    def _load_data(self):
        data = load_wine()
        self.X = data.data
        self.y = data.target
        self.feature_names = data.feature_names

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=self.random_state
        )

    def train(self):
        self.model.fit(self.X_train, self.y_train)
        return self.model

    def evaluate(self):
        preds = self.model.predict(self.X_test)
        return accuracy_score(self.y_test, preds)
