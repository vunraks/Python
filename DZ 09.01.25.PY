

#Task 1
import math

class Circle:
    def __init__(self, radius,):
        if radius <0:
            raise ValueError("radius ne mozhet bit` oticatel`nim")
        self.radius = radius
        

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented
    
    def __lt__ (self, other):
        if isinstance(other, Circle):
            return self.circumference() < other.circumference()
        return NotImplemented
        
    def __le__(self, other):
        if isinstance(other, Circle):
            return self.circumference() <= other.circumference()
        
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.circumference() > other.circumference()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.circumference() >= other.circumference()
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, (int, float)) and value > 0:
            return Circle(self.radius + value)
        return NotImplemented

    def __sub__(self, value):
        if isinstance(value, (int, float)) and 0 < value <= self.radius:
            return Circle(self.radius - value)
        return NotImplemented

    def __iadd__(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.radius += value
            return self
        return NotImplemented

    def __isub__(self, value):
        if isinstance(value, (int, float)) and 0 < value <= self.radius:
            self.radius -= value
            return self
        return NotImplemented

    def circumference(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"Circle(radius={self.radius})"


circle1 = Circle(5)
circle2 = Circle(7)

print(circle1 == circle2)  


print(circle1 < circle2) 
print(circle1 >= circle2) 


circle1 += 2
print(circle1)

circle2 -= 3
print(circle2)

      

      
#Task 2
class Airplane:
    def __init__(self, airplane_type, max_passengers, current_passengers=0):
        self.airplane_type = airplane_type
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.airplane_type == other.airplane_type
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers
        return NotImplemented

    def __add__(self, passengers):
        if isinstance(passengers, int) and passengers > 0:
            new_passengers = self.current_passengers + passengers
            if new_passengers <= self.max_passengers:
                return Airplane(self.airplane_type, self.max_passengers, new_passengers)
            else:
                raise ValueError("Exceeding maximum passenger capacity")
        return NotImplemented

    def __sub__(self, passengers):
        if isinstance(passengers, int) and passengers > 0:
            new_passengers = self.current_passengers - passengers
            if new_passengers >= 0:
                return Airplane(self.airplane_type, self.max_passengers, new_passengers)
            else:
                raise ValueError("Number of passengers cannot be negative")
        return NotImplemented

    def __iadd__(self, passengers):
        if isinstance(passengers, int) and passengers > 0:
            if self.current_passengers + passengers <= self.max_passengers:
                self.current_passengers += passengers
                return self
            else:
                raise ValueError("Exceeding maximum passenger capacity")
        return NotImplemented

    def __isub__(self, passengers):
        if isinstance(passengers, int) and passengers > 0:
            if self.current_passengers - passengers >= 0:
                self.current_passengers -= passengers
                return self
            else:
                raise ValueError("Number of passengers cannot be negative")
        return NotImplemented

    def __repr__(self):
        return (f"Airplane(type={self.airplane_type}, max_passengers={self.max_passengers}, "
                f"current_passengers={self.current_passengers})")


plane1 = Airplane("Boeing 747", 400, 100)
plane2 = Airplane("Airbus A320", 180, 50)

print(plane1 == plane2)

print(plane1 > plane2)
print(plane1 <= plane2)

plane1 += 50
print(plane1)

plane2 -= 30
print(plane2) 

try:
    plane1 += 300
except ValueError as e:
    print(e) 



        