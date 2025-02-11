class RatingError(Exception):
    pass


class Rating:
    def __init__(self, max_rating):
        assert max_rating > 0, f"Invalid {max_rating=}"
        self.max_rating = max_rating
        self.ratings = []

    def rate(self, rating):
        assert 0 < rating <= self.max_rating, f"Invalid {rating=}"
        self.ratings.append(rating)


movie = Rating(5)
movie.rate(5)
movie.rate(7)
