import cgi
form = cgi.FieldStorage()
gallery_id = form.getvalue('gallery_id')

print("Content-Type: text/html")
print()

print('''<form action = "/test/cgi-bin/images.py" method = "get">
Image title: <input type = "text" name = "title"> <br />''')

print('''Image link: <input type = "text" name = "link"> <br />''')

print('''<input type = "hidden" name = "gallery_id" value=%s>'''%(gallery_id))

print('''artist id: <input type = "text" name = "artist_id"> <br />''')

print('''year <input type = "text" name = "year" > <br />''')

print('''type <input type = "text" name = "type" > <br />''')

print('''width <input type = "text" name = "width" > <br />''')

print('''height <input type = "text" name = "height" > <br />''')

print('''location <input type = "text" name = "location" > <br />''')

print('''description: <input type = "text" name = "description" />
<input type = "submit" value = "Submit" />
</form''')





