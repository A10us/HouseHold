from models.household import Household
from views.consoleview import ConsoleView


class HouseholdController:
    def __init__(self):
        self.model = Household()
        self.view = ConsoleView(self)

    def main(self):
        self.view.main()

