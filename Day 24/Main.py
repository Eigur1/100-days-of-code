placeholder = "[Name]"

with open("./Input/Names/names.txt", "r") as name:
    names = name.read()
    name_list = [y for y in (x.strip() for x in names.splitlines()) if y]

with open("./Input/Letters/template.txt", "r") as template:
    template_local = template.read()
    for name in name_list:
        local_letter = template_local.replace(placeholder, name)
        with open(f"./Output/Letter for {name}", "w") as final_letter:
            final_letter.write(local_letter)


