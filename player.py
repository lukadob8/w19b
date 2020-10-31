class Player:
    def __init__(self, initalRow, initialColumn):
        self.rowPosition = initalRow
        self.columnPosition = initialColumn

    # TODO
    # def moveUp(self):
    def moveUp(self):
        self.rowPosition = self.rowPosition - 1

    # TODO
    # def moveDown(self):
    def moveDown(self):
        self.rowPosition = self.rowPosition + 1

    # TODO
    # def moveLeft(self):
    def moveLeft(self):
        self.columnPosition = self.columnPosition - 1

    # TODO
    # def moveRight(self):
    def moveRight(self):
        self.columnPosition = self.columnPosition + 1
