from kivy.uix.screenmanager import Screen, ScreenManager


# A safer way to add and remove screens for Kivy
class ScreenHandler():

    screenList = []

    def __init__(self):
        pass

    # Safe add
    @staticmethod
    def add_screen(parent: ScreenManager, screen: Screen):

        name = type(screen).__name__

        # If its not already in, then add it
        if not ScreenHandler.screenList.__contains__(name):
            ScreenHandler.screenList.append(name)
            parent.add_widget(screen)
            parent.current = name

    # Safe remove
    @staticmethod
    def remove_screen(parent: ScreenManager, screen: Screen):

        name = type(screen).__name__

        # If its not in, then do nothing
        if ScreenHandler.screenList.__contains__(name):
            ScreenHandler.screenList.remove(name)
            parent.remove_widget(screen)

    # Remove all
    @staticmethod
    def clear_all_screens(parent: ScreenManager):
        ScreenHandler.screenList = []
        parent.clear_widgets()