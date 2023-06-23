books_csv = []
chapters =[]
books = []
min_number = 0
highest_book = ''
with open(r'C:\Users\Spread\Documents\Eze Code\CSE 110 Programming Building Blocks\12_week\books_and_chapters.txt') as books_csv: 
    for line in books_csv:
        print(line.strip().split(':'))
        clean_line = line.strip().split(':') 
        chapter = int(clean_line[1])
        book = clean_line[2]
        chapters.append(chapter)
        books.append(book)
        if chapter > min_number:
            min_number = chapter
            highest_book = clean_line[2]
        
print(max(chapters))
#print(books)
print(highest_book)