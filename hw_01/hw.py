name = input("enter your name: ")
surname= input("enter your surname: ")
group_name = input("enter your group name: ")
university = input("enter your university: ")
mark = int(input("enter your average mark: "))

name = name[0].upper()+name[1:].lower()
surname = surname[0].upper()+surname[1:].lower()
university = university.upper()

text = "I am {name} {surname}, I am studying at the {university} with {group_name}, my average mark is {mark}.".format(name = name, surname = surname, university = university, group_name = group_name, mark = mark)

print(text)