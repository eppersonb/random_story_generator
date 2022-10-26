import random


def story_generator():
   bookTitle = ["Darkness..", "Something Creative", "STROONG", "High Time Flying", "Fight Club part 69"]
   starting_point = ["About a hundred years ago ", "In the beginning ", "In a small town called Pirn ", "In a small town bordering Ostania and Westalis "]
   occupation = ["there was once a farmer named ", "there was an assassin named ", "there was a peasent named ", "there was a spy named ", "there was a mercenary named ","there was a warrior named "]
   mainCharacter = ["Fiora", "Loid", "Anya", "Yor", "Franky", "Bryan"]
   currentCharacter = random.choice(mainCharacter)
   time = [". One day ", ". On one fateful night ", ". On an afternoon ",". On a unspecified time of day "]
   plot = [" recieved a random message from a carrier pigeon that read ", " was tasked with ", " was requested by the lord of the land ", " recieved a cipher that detailed "]
   message = ["to reclaim the legendary sword of Asornak.", "to repel enemy attackers.", "to stop a nuclear launch", "to assassinate a traitorus villian", "to infiltrate the palace"]

   print("The book title: " + random.choice(bookTitle))
   print(currentCharacter)

   print(random.choice(starting_point) + random.choice(occupation) + currentCharacter + random.choice(time) + currentCharacter + random.choice(plot) + random.choice(message) )


def main():
   story_generator()

main()
