class Movies:
  def __init__(self, name):
    self.name = name
    self.genre = []

  def add_genre(self, genre):
    self.genre.append(genre)
    print(f"\n Added: {genre}")
    print("\n")

  def remove_genre(self, genre):
    if song in self.genre:
      self.genre.remove(genre)
      print(f"Removed: {genre}")

  def show_genre(self):
    print(f"Movies '{self.name}':")
    for genre in self.genre:
      print(f"- {genre}")

my_movies = Movies ('Best of the day')
my_movies.add_genre("\n Horror- Conjuring")
my_movies.add_genre("\n Romance- Titanic")
my_movies.add_genre("\n Thriller- Frankenstein")
my_movies.add_genre("\n Comedy- Home Alone")
my_movies.show_genre()
