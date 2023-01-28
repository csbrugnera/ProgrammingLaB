
class Model():
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato') 
      
    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    def predict(self, data): 
        prev_value = None
        differenza = 0
        
        for item in data[1:len(data)]: #voglio partire dal secondp elemento pos [1]
            differenza = differenza + (item - prev_value);
            prev_value = item
            #dovrebbe essere differenza = 10
        print(differenza)        
    return prediction