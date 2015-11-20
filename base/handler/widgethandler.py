from kivy.uix.widget import Widget


# A safer way to add and remove widgets for Kivy
class WidgetHandler():

    widgetList = []

    def __init__(self):
        pass

    # Safe add
    @staticmethod
    def add_widget(parent, widget: Widget):

        name = type(widget).__name__

        # If its not already in, then add it
        if not WidgetHandler.widgetList.__contains__(name):
            WidgetHandler.widgetList.append(name)
            parent.add_widget(widget)

    # Safe remove
    @staticmethod
    def remove_widget(parent, widget: Widget):

        name = type(widget).__name__

        # If its not in, then do nothing
        if WidgetHandler.widgetList.__contains__(name):
            WidgetHandler.widgetList.remove(name)
            parent.remove_widget(widget)

    # Remove all
    @staticmethod
    def clear_all_widget(parent):
        WidgetHandler.widgetList = []
        parent.clear_widgets()