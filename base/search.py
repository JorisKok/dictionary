import os
from kivy.adapters.dictadapter import DictAdapter
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen
from base.dataclass.entry import Entry

view = Builder.load_file(os.path.dirname(__file__) + "/view/search.kv")


class Search(Screen):

    # The dictionary base
    dictionary = ObjectProperty(None)

    # Layout content used for the scroll view
    layout_content = ObjectProperty(None)

    # The list of search results
    search_result = []

    # The fonts
    font = StringProperty(None)
    font_awesome = StringProperty(None)

    previous_search = None

    def __init__(self, **kwargs):
        super(Search, self).__init__(**kwargs)

        # Needed for the scroll view
        # self.layout_content.bind(minimum_height=self.layout_content.setter("height"))

        # Add the label
        self.add_label("NonSelectableListItem", self.entry_to_ctx(self.dictionary.app.search.default_text()))

    def search_button_clicked(self):
        input_text = self.ids.search_input.text

        # Do the actual search
        # Also check if input is same do nothing
        if input_text is not None:
            if self.previous_search is not input_text:
                self.previous_search = input_text
                # Search by Text
                self.search_by_input_text(input_text)
                return

        # Show the nothing found
        self.add_label("NonSelectableListItem", self.entry_to_ctx(self.dictionary.app.search.no_result_text()))

    def search_by_input_text(self, input_text: str):
        # Clear the data
        self.ids.scroll_view_content.clear_widgets()

        # Use it here, but also pass the data to the Dictionary
        self.search_result = result = self.dictionary.app.search.search_by_input_text(input_text)

        for i, value in enumerate(result):
            value.list_key = i
            print(value.list_key)
            widget = self.add_label("SelectableListItem", self.entry_to_ctx(value))
            widget.bind(on_press=self.item_clicked)

    def item_clicked(self, item, **ctx):
        if item:
            # Pass the data into the dictionary for the Word class to use
            self.dictionary.search_result = self.search_result[item.list_key]

            # Switch to the word screen
            # Set the direction of the screen to change
            # Needed because it remembers transition direction from last time
            self.manager.transition.direction = "left"
            self.dictionary.current = self.dictionary.word.name

    # Add the widget to the scroll view
    def add_label(self, template: str, ctx):
        # Add the widget
        widget = Builder.template(template, **ctx)
        self.ids.scroll_view_content.add_widget(widget)

        return widget

    # Convert the Entry to a ctx
    def entry_to_ctx(self, entry: Entry):
        if not entry.list_key:
            entry.list_key = 0

        ctx = {
            "list_key": entry.list_key,
            "id_as_string": entry.id_as_string,
            "list_text": entry.list_text,
            "font": self.font
        }

        return ctx
