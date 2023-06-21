books_file = []

with open(r"C:\Users\Spread\Documents\Eze Code\CSE 110 Programming Building Blocks\11_week\books.txt") as books_file:
    for line in books_file:
        print(line.strip())