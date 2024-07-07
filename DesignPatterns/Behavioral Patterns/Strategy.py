from abc import ABC, abstractmethod

# Strategy Interface
class TransportationStrategy(ABC):
    @abstractmethod
    def travel_plan(self):
        pass

class AccomodationStrategy(ABC):
    @abstractmethod
    def stay_plan(self):
        pass

class ActivityStrategy(ABC):
    @abstractmethod
    def activity_plan(self):
        pass


# Concrete Strategies
class AirTravel(TransportationStrategy):
    def travel_plan(self):
        return "Travel by air: Fast and convenient for long distances"

class HotelStay(AccomodationStrategy):
    def stay_plan(self):
        return "Stay in Hotel: Enjoy Comfort and luxury services"

class AdventureSports(ActivityStrategy):
    def activity_plan(self):
        return "Enrage in adventure sports"


# Context class: Travel Plan
class TravelPlan:
    def __init__(self):
        self.transportation_strategy = None
        self.accomodation_strategy = None
        self.activity_strategy = None

    def set_transportation_strategy(self, strategy):
        self.transportation_strategy = strategy

    def set_accomodation_strategy(self, strategy):
        self.accomodation_strategy = strategy

    def set_activity_strategy(self, strategy):
        self.activity_strategy = strategy

    def generate_plan(self):
        plan = ""
        if self.transportation_strategy:
            plan += self.transportation_strategy.travel_plan() + "\n"
        if self.accomodation_strategy:
            plan += self.accomodation_strategy.stay_plan() + "\n"
        if self.activity_strategy:
            plan += self.activity_strategy.activity_plan() + "\n"

        return plan

# Usage Example
travel_plan = TravelPlan()
travel_plan.set_transportation_strategy(AirTravel())
travel_plan.set_accomodation_strategy(HotelStay())
travel_plan.set_activity_strategy(AdventureSports())
print(travel_plan.generate_plan())

# Travel by air: Fast and convenient for long distances
# Stay in Hotel: Enjoy Comfort and luxury services
# Enrage in adventure sports
