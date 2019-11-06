from guide import*
image = "D:\shilpa\2018\Sikuli_Project\Project_Applications\Sikuli_Project\Images\P1.PNG"
r = "r.png"
pimage = Pattern(image).exact()
a = find("1532526610026.png").text()
print a


if r.exists(pimage, 5):
   print "Screen matches 3D_Reciprocating_Saw_Gold, test passed"
   r.highlight(2)
else:
   print "Screen failed match of 3D_Reciprocating_Saw_Gold, test FAILED"