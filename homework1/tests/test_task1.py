from task1 import main
# I used an AI (ChatGPT) to help me make this basic test case and to see how to format the Pytests
# I also found Pytest examples online and will reference them if I usem, but for the most part they are examples to learn from
# Also it is good to learn how to read output to terminal
def test_task1_output(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"