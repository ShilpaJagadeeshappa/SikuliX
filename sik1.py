from guide import*

m = find(Pattern("1530891923892.png").similar(0.49))

# the red frame will blink for about 7 - 8 seconds
for i in range(2):
        m.highlight(1)
        wait(0.050)

n = find(Pattern("P3.PNG").similar(0.55) )
# the red frame will blink for about 7 - 8 seconds
for i in range(2):
        n.highlight(1)
        wait(0.050)
o = find(Pattern("1530883620577.png").similar(0.17))
# the red frame will blink for about 7 - 8 seconds
for i in range(2):
        o.highlight(1)
        wait(0.050)
o = find("1530885319211.png")
# the red frame will blink for about 7 - 8 seconds
for i in range(2):
        o.highlight(1)
        wait(0.050)



s = find(Pattern("P6.PNG").similar(0.30) )
# the red frame will blink for about 7 - 8 seconds
for i in range(2):
        s.highlight(1)
        wait(0.050)
        



text( Pattern("P2-1.PNG").similar(0.54),"Press Table")
text( Pattern("P3-1.PNG").similar(0.14),"Floor Court Side")
text( Pattern("P4-1.PNG").similar(0.24).targetOffset(-110,-9),"Floor Court Logo")
text( "1530885319211.png","Floor Court Logo")

text( Pattern("P6-1.PNG").similar(0.13),"Chair Covers")
show(5)

