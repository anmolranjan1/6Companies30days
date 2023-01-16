from sortedcontainers import SortedList
class StockPrice:

    def __init__(self):     
      self.current_stamp = -1
      self.records = {}
      self.prices = SortedList()
         
    def update(self, timestamp: int, price: int) -> None:    
        if timestamp in self.records:
          self.prices.remove(self.records[timestamp])        
        self.records[timestamp] = price
        self.prices.add(price)
        self.current_stamp = max(self.current_stamp, timestamp)
      
    def current(self) -> int:
        return self.records[self.current_stamp]

    def maximum(self) -> int:
        return self.prices[-1]

    def minimum(self) -> int:
        return self.prices[0]