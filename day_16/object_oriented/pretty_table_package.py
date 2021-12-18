import prettytable

table = prettytable.PrettyTable()
table.add_column("Name", ["Satyam", "Shivam", "Roshni"])
table.add_column("Class", ["BCA", "12th", "9th"])
table.align = "l"

print(table)
