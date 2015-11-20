from chinese.database import Database
from chinese.model.review import ReviewModel
from chinese.dataclass.flashcard import FlashCard


class Review:

    @staticmethod
    def get_cards():

        records = Database().session.query(ReviewModel).order_by("review_time").limit(20)

        result = []
        for record in records:
            result.append(FlashCard(
                key=record.id,
                traditional=record.traditional,
                simplified=record.simplified,
                pinyin=record.pinyin,
                english=record.english,
                sentence_traditional=record.sentence_traditional,
                sentence_simplified=record.sentence_simplified,
                sentence_pinyin=record.sentence_pinyin,
                sentence_english=record.sentence_english,
                review_time=record.review_time

            ))

        return result
