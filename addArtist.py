import cgi
form = cgi.FieldStorage()

print("Content-Type: text/html")
print()

print('''<form action = "/test/cgi-bin/artist.py" method = "get">
Artist ID: <input type = "text" name = "artist_id"> <br />''')

print('''name: <input type = "text" name = "artist_name"> <br />''')

print('''Birth Year: <input type = "text" name = "artist_birth_year"> <br />''')

print('''Country: <input type = "text" name = "artist_country"> <br />''')

print('''description: <input type = "text" name = "artist_description" />
<input type = "submit" value = "Submit" />
</form''')





