#Task 1 under Question 1
songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[1])

#Task 1 under Question 2
print(songs[0], songs[2])
#or
print(songs[0])
print(songs[2])
#Task 2 under Question 2
print(songs[1:3])

#Task 1 under Question 3
songs[2] = "Wheels On The Bus"
print(songs)

#Task 1 under Question 4
songs.append("Godzilla")
songs.insert(1,"Fallen")
songs.extend(["Without me"])
print(songs)

#Task 2 under Question 4
del songs[2]
print(songs)

#Question 5 answered within Tutorial

#Task 1 under Question 6
animals = ["Cat", "Dog", "Bird"]
#Task 2 under Question 6
animals.append("Turtle")
#Task 3 under Question 6
print(animals[2])
#Task 4 under Question 6
del animals[0]
#Task 5 under Question 6
for i in range(len(animals)):
    print(animals[i])
