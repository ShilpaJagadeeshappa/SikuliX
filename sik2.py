match = find("1530103193558.png")  # The actual image here.
z = match.findAll("1530103224337.png")
for icon in z:
    print icon.getTarget()
    click(icon)
    time.sleep(3)