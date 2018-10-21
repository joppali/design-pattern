from premier_league import PremierLeague

premier_league = PremierLeague()

premier_league.append_club("Tottenham")
premier_league.append_club("Liverpool")
premier_league.append_club("Chelsea")
premier_league.append_club("Everton")

itr = premier_league.iterator()

if __name__ == "__main__":
    while(itr.has_next()):
        print(itr.next())
