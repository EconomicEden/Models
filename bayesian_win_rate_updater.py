import time

class BayesianSignal:    
    def __init__(self):
        self.alpha = 1
        self.beta  = 1 
    
    def update(self, result):         
        if result in (3, -3):
            self.alpha += 1
        elif result in (4, -4):
            self.beta += 1
        
        mean = self.alpha / (self.alpha + self.beta)        
        variance = (self.alpha * self.beta) / ((self.alpha + self.beta) ** 2 * (self.alpha + self.beta + 1))        
        print(f"S/F: {self.alpha - 1} / {self.beta - 1}, T: {round(mean * 100 ,2 )}% (U: {round(variance * 100 ,2)}%)")

signal = BayesianSignal()

while True:     
    current_second = int(time.time()) % 60    
    result = (current_second % 3 ==0 )            
    signal.update(result)
    time.sleep(4)



'''
current_state = 0 

# 0 means no condition detected. 
# 1 means Lsignal detected
# 2 means Lsignal activated
# 3 means Lsignal success
# 4 means Lsignal failed
# -1 means SSignal detected
# -2 means SSignal activated
# -3 means SSignal success
# -4 means SSignal failed 

if cp < TL and CS == 0  

results_list = [ 3, 4, -3, -4]

if current_state in results_list:
    signal.update(result) 
    current_state = 0 
    
if current_state == 0 and 
    if current_price < bottom_line:
        current_state = 1
   
if current_state == 1:
    if current_price > bottom_line:
        current_state = 2
        long_fail_line = min(close_price[-5:-1]
        long_success_line = middle_line

if current_state == 2:
    if current_price > long_success_line:
        current_state = 3

    if current_price < long_fail_line:
        current_state = 4

    # signal.update(result)
    # result에 대응하는 코드 필요. 
    # self.alpha, self.beta = (self.alpha + 1, self.beta) if result else (self.alpha, self.beta + 1)  
    # 이 부분을 3, 4, -3, -4로 나눌 필요가 있네. 
    # 3, 4까지 결정되면 나머지는 분류기에 태워서 success or fail에 따라 업데이트 하고
    # current_state 자체는 0으로 설정
    








'''
