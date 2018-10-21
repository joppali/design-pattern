from iterator_interface import Iterator

class PremierLeagueIterator(Iterator):
    def __init__(self, premier_league):
        self.index = 0
        self.premier_league = premier_league

    def has_next(self) -> bool:
        return self.index < self.premier_league.get_length()

    def next(self) -> str:
        club = self.premier_league.get_club_at(self.index)
        self.index += 1
        return club
