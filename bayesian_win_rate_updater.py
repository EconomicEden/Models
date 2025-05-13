import time

class BayesianSignal:    
    def __init__(self):
        self.alpha = 1
        self.beta  = 1 
    
    def update(self, result):        
        self.alpha, self.beta = (self.alpha + 1, self.beta) if result else (self.alpha, self.beta + 1)        
        mean = self.alpha / (self.alpha + self.beta)        
        variance = (self.alpha * self.beta) / ((self.alpha + self.beta) ** 2 * (self.alpha + self.beta + 1))        
        print(f"S/F: {self.alpha - 1} / {self.beta - 1}, T: {round(mean * 100 ,2 )}% (U: {round(variance * 100 ,2)}%)")

signal = BayesianSignal()

while True:     
    current_second = int(time.time()) % 60    
    result = (current_second % 3 ==0 )            
    signal.update(result)
    time.sleep(4)
