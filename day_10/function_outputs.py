def format_name(f_name,l_name,format):
    if format=="lower":
        f_name = f_name.lower()
        l_name = l_name.lower()
    elif format=="upper":
        f_name = f_name.upper()
        l_name = l_name.upper()
    elif format=="title":
        f_name = f_name.title()
        l_name = l_name.title()
    name = f_name + " " + l_name
    return name

f_name = input("Enter first name : \n")
l_name = input("Enter last name : \n")
format = input("Enter formatting method : \n 'lower' for lower case \n 'upper' for upper case \n 'title' for title case  \n").lower()
formated_name = format_name(f_name=f_name,l_name=l_name,format = format)

print(f"Your {format} case name is {formated_name}")