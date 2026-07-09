class AIModel:
    def __init__(self, model_name, accuracy):
        self.model_name = model_name
        self.accuracy = accuracy
        
    def train(self):
        return f"{self.model_name} Training completed"
    
    def predict(self, input_data):
        return f"{self.model_name} is making predictions"
    
    def show_accuracy(self):
        return f"Accuracy {self.accuracy}%."
    
# Example usage
model = AIModel("Neural Network", 92)
print("model: " + model.train())  # Training the model
print("predictions: " + model.predict("sample input data"))  # Making predictions
print("accuracy: " + model.show_accuracy())  # Showing model accuracy
