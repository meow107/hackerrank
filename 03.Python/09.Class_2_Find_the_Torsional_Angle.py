class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(no.x - self.x, no.y - self.y, no.z - self.z)

    def dot(self, no):
        return (self.x * no.x + self.y * no.y + self.z * no.z)

    def cross(self, no):
        x_ = self.y * no.z - self.z * no.y
        y_ = self.z * no.x - self.x * no.z
        z_ = self.x * no.y - self.y * no.x
        return Points(x_, y_, z_)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)