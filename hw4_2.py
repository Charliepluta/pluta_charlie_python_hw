class Car:
    def __init__(self, color, speed, max_passengers, current_passengers):
        self.color = color
        self.speed = speed
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers
        
    def get_color(self):
        return self.color
    
    def get_distance_traveled(self, time):
        return self.speed * time
    
    def add_passenger(self):
        if self.current_passengers < self.max_passengers:
            self.current_passengers += 1
        else:
            print("Error: Vehicle is at maximum capacity")
    
    def remove_passenger(self):
        if self.current_passengers > 0:
            self.current_passengers -= 1
        else:
            print("Error: No passengers to remove")
