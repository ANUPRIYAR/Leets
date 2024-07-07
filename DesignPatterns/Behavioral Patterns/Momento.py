# Momento
class GameSave:
    def __init__(self, level, score, inventory):
        self.level = level
        self.score = score
        self.inventory = inventory

class Game:
    def __init__(self):
        self.level = 0
        self.score = 0
        self.inventory = []
        self.saves = []

    def play(self, level_increment, score_increment, new_items):
        self.level += level_increment
        self.score += score_increment
        self.inventory.extend(new_items)
        self.saves.append(GameSave(self.level, self.score, self.inventory))

    def undo_last_play(self):
        if self.saves:
            last_save = self.saves.pop()
            self.level = last_save.level
            self.score = last_save.score
            self.inventory = last_save.inventory

    def print_status(self):
        print(f"Level : {self.level}  Score :{self.score} Inventory: {self.inventory}")



# Client code
game = Game()
game.play(1, 100, ['Sword', 'Shield'])
game.print_status()

game.play(2, 200, ["Bow", "Arrow"])
game.print_status()

game.undo_last_play()
game.print_status()



# Level : 1  Score :100 Inventory: ['Sword', 'Shield']
# Level : 3  Score :300 Inventory: ['Sword', 'Shield', 'Bow', 'Arrow']
# Level : 3  Score :300 Inventory: ['Sword', 'Shield', 'Bow', 'Arrow']

