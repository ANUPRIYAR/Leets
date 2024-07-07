class Command:
    def execute(self):
        pass


class Light:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")

class TurnOnLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class TurnOffLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

class RemoteControl:
    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()


# Client Code
if __name__ == "__main__":
    light = Light()
    turn_on = TurnOnLightCommand(light)
    turn_off = TurnOffLightCommand(light)

    remote = RemoteControl()
    remote.set_command(turn_on)
    remote.press_button()

    remote.set_command(turn_off)
    remote.press_button()



# Light is on
# Light is off