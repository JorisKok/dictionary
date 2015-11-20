from korean.database import Database
from korean.model.dictionary import Dictionary
from base.dataclass.entry import Entry
from sqlalchemy import case, literal_column
import regex


class Search:

    def search_by_input_text(self, input_text: str) -> [Entry]:
        # TODO make it possible to search on english text as well

        # Check whether the string is Korean or English/Phonetic
        r = regex.compile(r"[a-zA-Z]")
        if r.match(input_text):
            # If the input is in English
            print("Searching on English")

            # Used for sorting depending on how we search on it
            xpr = case([
                (
                    Dictionary.english.ilike(input_text),
                    literal_column("1")
                ),
                (
                    Dictionary.english.ilike(input_text+"%"),
                    literal_column("2")
                ),
                (
                    Dictionary.english.ilike("%"+input_text),
                    literal_column("3")
                ),
                (
                    Dictionary.english.ilike("%"+input_text+"%"),
                    literal_column("4")
                )
            ])
            records = Database().session.query(Dictionary, xpr).filter(Dictionary.english.ilike("%"+input_text+"%")).order_by("anon_1").__all()  # Anon1 is the default name
        else:
            # If the input is in Korean
            print("Searching on Korean")

            # Used for sorting depending on how we search on it
            xpr = case([
                (
                    Dictionary.korean.ilike(input_text),
                    literal_column("1")
                ),
                (
                    Dictionary.korean.ilike(input_text+"%"),
                    literal_column("2")
                ),
                (
                    Dictionary.korean.ilike("%"+input_text),
                    literal_column("3")
                ),
                (
                    Dictionary.korean.ilike("%"+input_text+"%"),
                    literal_column("4")
                )
            ])
            records = Database().session.query(Dictionary, xpr).filter(Dictionary.korean.ilike("%"+input_text+"%")).order_by("anon_1").__all()  # Anon1 is the default name

        result = []
        for record in records:
            entry = Entry(record[0].id, record[0].korean, record[0].english, root=record[0].root)
            result.append(entry)

        # No results
        if not result:
            return self.no_result_text()

        # Set the length inside the extra label maybe
        print("Length: %s" % len(result))

        return result[0:20]  # TODO remove the max length

    @staticmethod
    def default_text() -> Entry:

        return Entry(
            0,
            "Welcome!",
            "Please use the search box above")

    @staticmethod
    def no_result_text() -> Entry:

        return [Entry(
            0,
            "No results found",
            "Please use the search box above")]

