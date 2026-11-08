class Vehicle:
    """Parent class representing a general vehicle."""

    def __init__(self, name, capacity):
        """Initialize vehicle name and seating capacity."""
        self.name = name
        self.capacity = capacity

    def seating_capacity(self, capacity):
        """Return the seating capacity of the vehicle."""
        return f"{self.name} seating capacity is: {capacity}"


class Bus(Vehicle):
    """Child class representing a bus."""

    def seating_capacity(self, capacity=50):
        """Override parent method with a default capacity of 50."""
        return super().seating_capacity(capacity)


# Create a Bus object
bus = Bus("School Bus", 120)

# Display seating capacity
print(bus.seating_capacity())