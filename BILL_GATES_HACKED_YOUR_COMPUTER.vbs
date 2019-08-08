x = msgbox("Your download will begin shortly", 0 + 32, "Thank You")

set x = createobject("internetexplorer.application")
'in code, the colon acts as a line feed
x.navigate2 "about:blank" : x.width = 350 : x.height = 80 : x.toolbar = false : x.menubar = false : x.statusbar = false : x.visible = true

x.document.write "<font color=blue>"
for n = 1 to 100
    x.document.write "|"
    wscript.sleep 50
    x.document.title = n & " %"
next
'close the window
x.quit
set x = nothing

x = msgbox("An ERROR occurred during the installation. Please try again.", 2 + 16, "ERROR")

set x = createobject("internetexplorer.application")
'in code, the colon acts as a line feed
x.navigate2 "about:blank" : x.width = 350 : x.height = 80 : x.toolbar = false : x.menubar = false : x.statusbar = false : x.visible = true

x.document.write "<font color=blue>"
for n = 1 to 100
    x.document.write "|"
    wscript.sleep 50
    x.document.title = n & " %"
next
'close the window
x.quit
set x = nothing

x = msgbox("The installation is complete. Restart your computer for the new changes to take effect.", 0 + 64, "Success!")