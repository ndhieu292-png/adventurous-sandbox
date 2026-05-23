notes = []
def add_notes():
    Title = input("title: ")
    Content = input("contet: ")
    note = {"title": Title, "content": Content}
    notes.append(note)
def show_notes():
    for index, note in enumerate(notes):
        print(index + 1)
        print(note["title"])
        print(note["content"])
def remove_notes(index):
    notes.pop(index - 1)
menu = ["1. Add notes", "2. Show notes", "3. Remove notes", "4. Search notes", "5. Exit"]
while True:
    for task in menu:
        print(task)
    choice = input("Choose: ")
    if choice == "1":
        while True:
            action = input("1. add note, 2. 0 for quit")
            if action == "1":
                add_notes()
            elif action == "0":
                break
    elif choice == "2":
        show_notes()
    elif choice == "3":
        while True:
            show_notes()
            if len(notes) == 0:
                print("Empty notes")
                break
            index = int(input("Enter number, 0 for quit: "))
            if index == 0:
                break
            elif 0 < index <= len(notes):
                remove_notes(index)
            else:
                print ("Invalid")
    elif choice == "4":
        search = input("Keyword: ")
        found = False
        for index, note in enumerate(notes):    
            if search in note["title"] or search in note["content"]:
                found = True
                print(index + 1)
                print(note["title"])
                print(note["content"])
        if found == False:
            print("Invalid")
    elif choice == "5":
        break
            

            

