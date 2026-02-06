import task5
from task5 import print_first_3_books

def test_task5_list_type():
    assert isinstance(task5.books, list)

def test_task5_dict_type():
    assert isinstance(task5.students, dict)

def test_print_three_books(capsys):
    print_first_3_books()
    captured = capsys.readouterr()
    assert captured.out == "To Kill a Mockingbird by Harper Lee\nOf Mice and Men by John Steinbeck\nFrankenstein by Mary Shelley\n"