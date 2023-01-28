class Model():
    def __init__(self, finestra):
        self.finestra = finestra #finestra è num di dati x predizione
        
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')


class IncrementModel(Model):

    def evaluate(self, test_data): 
        
        
    def predict(self, test_data):
        prev_value = None
        increment = None

        for item in test_data:
            if item != prev_value:
                increment = item - prev_value
            increment += increment
            prev_value = item
            
        prediction = increment/len(data)
        return prediction
