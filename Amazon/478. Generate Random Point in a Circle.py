class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        r = sqrt(random.random()) * self.r
        angle = random.uniform(0, 2*pi)
        return [self.x + r * math.cos(angle), self.y + r *math.sin(angle)]