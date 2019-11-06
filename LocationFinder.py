from guide import*
match = find("1531994934723.png")  # The actual image here.
a = match.findAll("1531994944449.png")
for icon in a:
    print icon.getTarget()
    click(icon)
    time.sleep(3)

  