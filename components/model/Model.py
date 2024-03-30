from tf_keras.models import Sequential
from tf_keras.layers import Dense


class Model:
    def __init__(self) -> None:
        self.model = Sequential()
        self.model.add(Dense(64, activation='relu', input_dim=4))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(1, activation='linear'))
        self.model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

    def getModel(self) -> Sequential:
        return self.model
