from pathlib import Path

def how_many_words_in_file():
    # I got some help from chatGPT to help me come up with this format for opening the file
    # I know the normal with open(file, "r"), but I have never had to open a file from two different directories without hardcoding a path
    homework1_path = Path(__file__).resolve().parent.parent
    file_path = homework1_path / "task6_read_me.txt"

    with open(file_path, "r") as f:
        task6_read = f.read()
    #simple way to return the number of words in a file as .split turns a string into a list of strings on each space
    return len(task6_read.split())

#Also to note I changed the file given slightly to remove spaces inbetween punctuation. 
def main():
    print(how_many_words_in_file())

if __name__ == "__main__":
    main()