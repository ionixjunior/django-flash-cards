from datetime import timedelta


# pylint: disable=too-few-public-methods
class SimpleSRS:
    INTERVALS = {
        'again': timedelta(minutes=1),
        'hard': timedelta(days=1),
        'good': timedelta(days=3),
        'easy': timedelta(days=7),
    }

    def calculate_next_review_date(self, today, feedback):
        try:
            interval = self.INTERVALS[feedback]
            next_date = today + interval
            return next_date
        except KeyError:
            return today
