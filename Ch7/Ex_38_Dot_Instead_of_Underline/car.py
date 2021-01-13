class Car():
    """Class represents a car
    Data properties:
        .model
        .make
        .year
    Behavirors/Operations:
      .drive
      .parallelpark


    """
    yr = 2020

    def __init__(self, model, make, year):
        """Initialize model, make, and year variables."""
        self.model = model
        self.make = make
        self.year = year

    def drive(self):
        """Move the car."""
        print(self.model.title() + " is now moving.")

    def parallelpark(self):
        """Parallel park the car."""
        print(self.model.title() + " is now parking.")


