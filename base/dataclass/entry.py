from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.uix.widget import Widget
# An object used for having the dictionary refer to the same type of fields


class Entry(Widget):

    key = NumericProperty()  # Id in the db
    list_key = NumericProperty()  # Index in the list
    definition = StringProperty()
    list_text = StringProperty()

    # Chinese specific
    traditional = StringProperty()
    simplified = StringProperty()
    pinyin = StringProperty()

    # Korean specific
    # ...

    # TODO implement this:
    root = None  # Used for the result within the word
    parent = ObjectProperty()  # The parent object of the root result

    @property
    def id_as_string(self):
        return StringProperty(self.key)

    @id_as_string.setter
    def id_as_string(self, key: str):
        return NumericProperty(key)

    @property
    def title(self):
        return "%s" % self.word

    @property
    def character(self):
        result = []
        if self.traditional:
            result.append(self.traditional)
        if self.simplified:
            result.append(self.simplified)

        return "/".join(result)

    @property
    def list_text(self):
        # Capitalize the definition
        definition = self.definition.capitalize()
        if len(definition) > 60:
            definition = definition[0:60] + "..."

        # If pinyin available
        if self.pinyin:
            definition += self.pinyin

        result = "[size=18]%s[/size] \n[size=14]%s[/size]" % (self.word, definition)

        # Replace all the | with a comma and a space
        return result.replace("|", ", ")

    def __init__(self, key: int, word: str, definition: str, **kwargs):
        super(Entry, self).__init__(**kwargs)
        self.key = key
        self.word = word
        self.definition = definition
