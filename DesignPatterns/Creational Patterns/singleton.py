"""
The Singleton pattern ensures that a class has only one instance and provides a global point of access to it. In the provided Python code, the SingletonObject class is correctly implemented as a Singleton class.  When you call SingletonObject(), it doesn't create a new instance every time. Instead, it returns the same instance that was created the first time SingletonObject() was called. This is because of the __new__ method in the SingletonObject class, which overrides the default behavior of creating a new instance every time the class is called.

In the SingletonDemo class, when you call SingletonObject() twice to get instance and obj, you are actually getting two references to the same instance, not two different instances.  Therefore, when you call obj.show_message() and instance.show_message(), you are calling the show_message method on the same instance, not on two different instances.  This is the expected behavior of the Singleton pattern. If you want to create a new instance every time you call SingletonObject(), then the Singleton pattern is not appropriate for your use case.
"""

class SingletonObject:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonObject, cls).__new__(cls)
        return cls._instance

    def show_message(self):
        print("Hello from Singleton Pattern")



# Test the singleton pattern
class SingletonDemo:
    @staticmethod
    def main():
        instance = SingletonObject()

        obj = SingletonObject()

        # Check if instance and obj are the same instance
        if instance is obj:
            print("instance and obj are the same instance")
        else:
            print("instance and obj are not the same instance")

        # show the message
        obj.show_message()
        instance.show_message()

if __name__ == "__main__":
    SingletonDemo.main()

