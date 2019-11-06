import org.sikuli.script.FindFailed;
Screen screen = new Screen();
try{
    if(screen.exists("1531994403700.png") != null || screen.exists("img2.png") != null){
        //DO YOUR ACTIONS
        screen.click("img1.png");
        }
    }
catch(FindFailed e){
    e.getStackTrace();
}