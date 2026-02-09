# Make the list of books
books = ["To Kill a Mockingbird by Harper Lee", "Of Mice and Men by John Steinbeck", "Frankenstein by Mary Shelley", "Fahrenheit 451 by Ray Bradbury", "Animal Farm by George Orwell"]
# A student dictonary. The formatting was based off of the formatting shown on this site https://www.w3schools.com/python/python_dictionaries.asp
students = {
  "student1" : {
    "name" : "John Johnson",
    "IDnumber" : 1111
  },
  "student2" : {
    "name" : "Amy Vyper",
    "IDnumber" : 1112
  },
  "student3" : {
    "name" : "Jack Jackson",
    "IDnumber" : 1113
  }
}

# A funct to print the first 3 books in a list (This is lacking control if the list is less than 3 from what I can tell)
def print_first_3_books():
    number_printed = 0
    for book in books[:3]:
        print(book)
    return

#driver code
def main():
    print_first_3_books()

if __name__ == "__main__":
    main()
