from task1 import main

def test_task1_output(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"