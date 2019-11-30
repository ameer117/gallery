import cgi
import pymysql
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
image_id = form.getvalue('image_id')
gallery_id = form.getvalue('gallery_id')
title = form.getvalue('title')
link = form.getvalue('link')
detail_id = form.getvalue('detail_id')
year = form.getvalue('year')
imageType = form.getvalue('imageType')
width = form.getvalue('width')
height = form.getvalue('height')
#location = form.getvalue('location')
description = form.getvalue('description')





print("Content-Type: text/html")
print()


print('''<form action = "/test/cgi-bin/images.py" method = "get  ">
Title: <input type = "text" name = "editTitle" value=%s>  <br />'''%(title))

print('''<input type = "hidden" name = "gallery_id" value=%s> '''%(gallery_id))
print('''<input type = "hidden" name = "editImageID" value=%s> <br />'''%(image_id))
print('''<input type = "hidden" name = "editDetailID" value=%s> <br />'''%(detail_id))
print('''year: <input type = "text" name = "editYear" value=%s> <br />'''%(year))
print('''type: <input type = "text" name = "editType" value=%s> <br />'''%(imageType))
print('''width: <input type = "text" name = "editWidth" value=%s> <br />'''%(width))
print('''height: <input type = "text" name = "editHeight" value=%s> <br />'''%(height))
#print('''location: <input type = "text" name = "editLocation" value=%s> <br />'''%(location))
print('''description<input type = "text" name = "editDescription" value=%s> <br />'''%(description))





print('''link: <input type = "text" Name = "editLink" value=%s />
<input type = "submit" value = "Submit Edits" />
</form'''%(link))





