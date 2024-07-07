from abc import ABC, abstractmethod

# State Interface
class State(ABC):
    @abstractmethod
    def publish(self, document):
        pass
    @abstractmethod
    def approve(self, document):
        pass

# Concrete States
class Draft(State):
    def publish(self, document):
        print("Publishing draft, moving to moderation")
        document.state = Moderation()

    def approve(self, document):
        print("Draft cannot be approved directly")

class Moderation(State):
    def publish(self, document):
        print("Cannot publish from Moderation without approval")

    def approve(self, document):
        print("Approving moderation, moving to published")
        document.state = Published()


class Published(State):
    def publish(self, document):
        print("Already published")

    def approve(self, document):
        print("Already approved")


# Context class
class Document:
    def __init__(self):
        self.state = Draft()

    def publish(self):
        self.state.publish(self)

    def approve(self):
        self.state.approve(self)


# Usage
doc = Document()
doc.publish()
doc.approve()


# Publishsing draft, moving to moderation
# Approving moderation, moving to published