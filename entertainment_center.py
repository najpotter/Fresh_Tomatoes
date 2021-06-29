#https://classroom.udacity.com/courses/ud036
import media
import fresh_tomatoes

the_tinmine = media.Movie("The TinMine",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/th/6/67/The_Tin_Mine_film.jpg",
                        "https://www.youtube.com/watch?v=wrFGBdjL7pY")

print(the_tinmine.storyline)

the_terminal = media.Movie("The Terminal",
                     "The film is partially inspired by the true story of the 18-year stay of Mehran Karimi Nasseri in Terminal 1 of Paris-Charles de Gaulle Airport",
                     "https://upload.wikimedia.org/wikipedia/en/8/86/Movie_poster_the_terminal.jpg",
                     "https://www.youtube.com/watch?v=iZqQRmhRvyg")

print(the_terminal.storyline)

The_Dark_Knight  = media.Movie("The Dark Knight ", 
                             "Based on the DC Comics character Batman",
                             "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                             "https://www.youtube.com/watch?v=TQfATDZY5Y4")

print(The_Dark_Knight.storyline)

The_Blind_Side  = media.Movie("The Blind Side ",
                          "The Blind Side is a 2009 American biographical sports drama film written and directed by John Lee Hancock",
                          "https://upload.wikimedia.org/wikipedia/en/6/60/Blind_side_poster.jpg",
                          "https://www.youtube.com/watch?v=gvqj_Tk_kuM")

print(The_Blind_Side.storyline)

Inception = media.Movie("Inception",
                                "Dom Cobb is a skilled thief, the absolute best in the dangerous art of extraction, stealing valuable secrets from deep within the subconscious during the dream state, when the mind is at its most vulnerable",
                                "https://upload.wikimedia.org/wikipedia/th/c/cb/%E0%B8%88%E0%B8%B4%E0%B8%95%E0%B8%9E%E0%B8%B4%E0%B8%86%E0%B8%B2%E0%B8%95%E0%B9%82%E0%B8%A5%E0%B8%81.jpg",
                                "https://www.youtube.com/watch?v=YoHD9XEInc0")

print(Inception.storyline)

Zack_Snyder_Justice_League = media.Movie("Zack Snyder's Justice League",
                           "Zack Snyder's Justice League, often referred to as the Snyder Cut, is the 2021 director's cut of the 2017 American superhero film",
                           "https://upload.wikimedia.org/wikipedia/en/6/60/Zack_Snyder%27s_Justice_League.png",
                           "https://www.youtube.com/watch?v=vM-Bja2Gy04")   

print(Zack_Snyder_Justice_League.storyline)

movies = [the_tinmine, the_terminal, The_Blind_Side, Inception, The_Dark_Knight, Zack_Snyder_Justice_League]
fresh_tomatoes.open_movies_page(movies)