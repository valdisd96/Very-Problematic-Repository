# Complete implementation code for issue #5

class AIModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.trained = False

    def train(self, training_data):
        # Simulate training process
        print(f"Training {self.model_name} with provided data...")
        self.trained = True
        print(f"{self.model_name} training complete.")

    def predict(self, input_data):
        if not self.trained:
            raise Exception("Model must be trained before making predictions.")
        # Simulate prediction process
        print(f"Making predictions with {self.model_name}...")
        return [f"Prediction for {data}" for data in input_data]

# Example usage
if __name__ == "__main__":
    model = AIModel("SampleModel")
    training_data = ["data1", "data2", "data3"]
    model.train(training_data)

    input_data = ["input1", "input2"]
    predictions = model.predict(input_data)
    print(predictions)