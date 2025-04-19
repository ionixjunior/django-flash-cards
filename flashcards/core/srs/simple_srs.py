from datetime import timedelta


# pylint: disable=too-few-public-methods
class SimpleSRS:
    FEEDBACK_LEVELS = {
        'again': 0,
        'hard': 1,
        'good': 2,
        'easy': 3,
    }

    INTERVALS = {
        0: timedelta(minutes=1),
        1: timedelta(days=1),
        2: timedelta(days=3),
        3: timedelta(days=7),
    }

    def calculate_next_review_date(self, today, feedback):
        try:
            level = self.FEEDBACK_LEVELS[feedback]
            interval = self.INTERVALS[level]
            next_date = today + interval
            return next_date
        except KeyError:
            return today
