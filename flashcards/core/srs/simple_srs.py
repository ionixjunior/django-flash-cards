from datetime import timedelta


class SimpleSRS:
    def calculate_next_review_date(self, today, feedback):
        if feedback == 'hard':
            return today + timedelta(days=1)

        return None