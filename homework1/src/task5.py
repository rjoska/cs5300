books = ["To Kill a Mockingbird by Harper Lee", "Of Mice and Men by John Steinbeck", "Frankenstein by Mary Shelley", "Fahrenheit 451 by Ray Bradbury", "Animal Farm by George Orwell"]
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

def print_first_3_books():
    number_printed = 0
    for book in books[:3]:
        print(book)
    return

def main():
    print_first_3_books()

if __name__ == "__main__":
    main()
