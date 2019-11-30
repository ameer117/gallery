import cgi
import pymysql
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
gallery_id = form.getvalue('gallery_id')
name = form.getvalue('name')
description = form.getvalue('description')





print("Content-Type: text/html")
print()


print('''<form action = "/test/cgi-bin/gallery.py?editID=%s" method = "get  ">
Name: <input type = "text" name = "editName" value=%s>  <br />'''%(gallery_id,name))

print('''<input type = "hidden" name = "editID" value=%s> <br />'''%(gallery_id))


print('''DESCRIPTION: <input type = "text" Name = "editDescription" value=%s />
<input type = "submit" value = "Submit" />
</form'''%(description))





