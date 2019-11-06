while True(1) # repeat the body forever
    wait(, 10) # wait max 10 seconds for image1 to get visible, otherwise die
    click("button1.png") # click the button given by image button1
    if exists("image2.png"): # wait max 3 seconds for image2 to get visible, return True or False
       doSomething() # in case True execute function doSomething (defined somewhere else)
    else:
       break # in case False get out of the loop, which ends the workflow
    # start all over with the line after the while
# the end of the workflow