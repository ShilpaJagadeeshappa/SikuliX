dir_xlrd = "absolute path to the xlrd directory"
if not dir_xlrd in sys.path: sys.path.append(dir_xlrd)
import xlrd
type(Key.HOME, KeyModifier.CTRL) #takes you to cell A1
type("a", KeyModifier.CTRL) #select all
type("c", KeyModifier.CTRL) #copy to clipboard
fromExcel = Env.GetClipboard().strip() #get clipboard contents into Sikuli, without leading or trailing white space
cells = fromExcel.split("/n") #split each cell into list on newline

#go to the destination app, maybe using App.open("nameOfYourApp") if it's not open yet, or App.focus("nameOfYourApp") if it is already open

for cell in cells: #use python to iterate through your list
    #navigate to the line or cell where you want to paste
    paste(cell) 