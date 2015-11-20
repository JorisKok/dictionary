from sqlalchemy import case, literal_column
import regex
from base.dataclass.entry import Entry
from chinese.database import Database
from chinese.model.dictionary import DictionaryModel
from chinese.pinyin import Pinyin


class Search:

    def search_by_input_text(self, input_text: str) -> [Entry]:

        result = []

        # Match English TODO improve...
        r = regex.compile(r"[a-zA-Z]")
        if r.match(input_text):

            # match pinyin
            if Pinyin().is_pinyin(input_text):
                pass
            else:
                # it's in English
                records = Database().session.query(DictionaryModel).filter(DictionaryModel.english.ilike("%" + input_text + "%"))
                i = 0
                for record in records:
                    entry = Entry(i, record.traditional, record.english,
                                  pinyin=record.pinyin, traditional=record.traditional,
                                  simplified=record.simplified)
                    result.append(entry)
                    i += 1

        else:
            # 我是荷蘭人
            records = self.look_up_chinese(input_text)

            # Put the records in entries for display
            i = 0
            for record in records:
                for r in record:
                    entry = Entry(i, r.traditional, r.english,
                                  pinyin=r.pinyin,
                                  simplified=r.simplified, traditional=r.traditional)  # TODO add pinyin and simplified
                    result.append(entry)
                    i += 1

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

    @staticmethod
    def look_up_chinese(input_text):

        result = []
        found, found2 = False, False
        new_character = input_text[0]

        for i, character in enumerate(input_text):
            # Look up one
            if i + 1 < len(input_text):
                new_character = new_character + input_text[i+1]
                t_record = Database().session.query(DictionaryModel).filter(DictionaryModel.traditional.ilike(new_character))

                # Hmm, t_record is a query type but you can loop it over...?
                for r in t_record:
                    # Something found, so continue with another look ahead
                    found = True

                if found:
                    found = False
                    found2 = True
                    continue

                # If the previous lookup was found, and this one is not, then find the previous one
                if found2:
                    record = Database().session.query(DictionaryModel).filter(DictionaryModel.traditional.ilike(new_character[0:-1]))
                    result.append(record)
                    found2 = False
                    continue

                # Nothing found, so cancel and just look up the character
                new_character = input_text[i+1]
                found = False
                record = Database().session.query(DictionaryModel).filter(DictionaryModel.traditional.ilike(character))
                result.append(record)
            else:
                record = Database().session.query(DictionaryModel).filter(DictionaryModel.traditional.ilike(character))
                result.append(record)

        return result
