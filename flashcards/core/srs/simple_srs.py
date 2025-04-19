from datetime import timedelta


class SimpleSRS:
    def calculate_next_review_date(self, today, feedback):
        if feedback == 'again':
            return today + timedelta(days=0)

        if feedback == 'hard':
            return today + timedelta(days=1)

        if feedback == 'good':
            return today + timedelta(days=3)

        if feedback == 'easy':
            return today + timedelta(days=7)

        return today + timedelta(days=0)
