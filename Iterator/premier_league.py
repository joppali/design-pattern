from aggregate_interface import Aggregate
from iterator_interface import Iterator
from premier_league_iterator import PremierLeagueIterator

class PremierLeague(Aggregate):
    def __init__(self):
        self._clubs = []
        self._champion = "City"

    def get_length(self) -> int:
        return len(self._clubs)

    def get_club_at(self, index) -> str:
        return self._clubs[index]
 
    def append_club(self, club):
        self._clubs.append(club)

    def get_champion(self) -> str:
        return self.champion

    def iterator(self) -> Iterator:
        # return LeagueIterator(self)
        return PremierLeagueIterator(self)
