import fresh_tomatoes
import media

# Creates several Movie instances and then add all of them to a list
blade_runner_2049 = media.Movie(
    "Blade Runner 2049",
    "Thirty years after the events of the first film, a new blade runner, "
    "LAPD Officer K (Ryan Gosling), unearths a long-buried secret that has "
    "the potential to plunge what's left of society into chaos. K's "
    "discovery leads him on a quest to find Rick Deckard (Harrison Ford).",
    "https://lh3.googleusercontent.com/BxPa8EexNqCEXhkdM9tQY7GPnpOCxjtDaySEAPx9-ym1bDVAwYl8eQms-sW_dTKmiRjCCQ=w400-h600",  # noqa
    "https://www.youtube.com/watch?v=gCcx85zbxz4")

guardians_galaxy_2 = media.Movie(
    "Guardians of the Galaxy Vol. 2",
    "The Guardians must fight to keep their newfound family together as they "
    "unravel the mystery of Peter Quill's true parentage.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg2MzI1MTg3OF5BMl5BanBnXkFtZTgwNTU3NDA2MTI@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=jQFIu9InG7Q")

civil_war = media.Movie(
    "Captain America: Civil War",
    "Political involvement in the Avengers' activities causes a rift "
    "between Captain America and Iron Man.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQ0MTgyNjAxMV5BMl5BanBnXkFtZTgwNjUzMDkyODE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=dKrVegVI0Us")

star_wars_last_jedi = media.Movie(
    "Star Wars: Episode VIII - The Last Jedi",
    "Rey develops her newly discovered abilities with the guidance of "
    "Luke Skywalker, who is unsettled by the strength of her powers. "
    "Meanwhile, the Resistance prepares for battle with the First Order.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQ1MzcxNjg4N15BMl5BanBnXkFtZTgwNzgwMjY4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=Q0CbN8sfihY")

thor_ragnarok = media.Movie(
    "Thor: Ragnarok",
    "Thor is imprisoned on the other side of the universe and finds "
    "himself in a race against time to get back to Asgard to stop Ragnarok, "
    "the destruction of his homeworld and the end of Asgardian civilization,"
    " at the hands of an all-powerful new threat, the ruthless Hela.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=ue80QwXMRHg")

# Creates a list with all my movies
movies = [blade_runner_2049, guardians_galaxy_2, civil_war,
          star_wars_last_jedi, thor_ragnarok]

# Calls the method that renders and displays the website
fresh_tomatoes.open_movies_page(movies)
