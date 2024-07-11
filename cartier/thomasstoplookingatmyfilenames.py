class Movie:
    def __init__(self, title, director, year):
        self.title=title
        self.director=director
        self.year=year

tlk=Movie("The Lion King","Roger Allers and Rob Minkoff",1994)
frozone=Movie("Frozen","Chris Buck and Jennifer Lee",2013)
down=Movie("Up","Pete Docter and Bob Peterson",2009)

print(f"{tlk.title} directed by {tlk.director} was released in {tlk.year}.")
print(f"{frozone.title} directed by {frozone.director} was released in {frozone.year}.")
print(f"{down.title} directed by {down.director} was released in {down.year}.")