movies = ["Star Wars","Ghandi","Casablanca","Shawshank Redemption","Toy Story","Ghostbusters","Raiders of the Lost Ark","Groundhog Day",
"Terminator","Back to The Future","Aliens","Frozen","Pirates","Zootopia","Good Will Hunting"]

#list with tuples 
moviesWithYear = [("Titanic",1997),("Jurassic Park",1993),("Ghost", 1990),("Avatar",2009),("Shrek 2",2004),("Finding Nemo",2003),("Joker",2019),("Skyfall",2012)]


def forLoopEx():
    gmovies = []
    for title in movies:
        if title.startswith("G"):
            gmovies.append(title)

    print(gmovies)



#forLoopEx()

#Comprehension
gmovies = [title for title in movies if title.startswith("G")]
print(gmovies)

#Comprehension with if clause
pre2k = [title for (title, year) in moviesWithYear if year < 2000]
print(pre2k)