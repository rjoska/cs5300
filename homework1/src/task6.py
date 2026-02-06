from pathlib import Path

def how_many_words_in_file():
    # I got some help from chatGPT to help me come up with this format for opening the file
    # I know the normal with open stuff, but I have never had to open a file from two different files without hardcoding a path
    homework1_path = Path(__file__).resolve().parent.parent
    file_path = homework1_path / "task6_read_me.txt"

    with open(file_path, "r") as f:
        task6_read = f.read()

    return len(task6_read.split())

def main():
    print(how_many_words_in_file())

if __name__ == "__main__":
    main()