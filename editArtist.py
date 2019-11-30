import cgi
import pymysql
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
artist_id = form.getvalue('artist_id')
name = form.getvalue('name')
birth_year = form.getvalue('birth_year')
country = form.getvalue('country')
description = form.getvalue('description')

print("Content-Type: text/html")
print()


print('''<form action = "/test/cgi-bin/artist.py" method = "get  ">
Title: <input type = "text" name = "edit_artist_name" value=%s>  <br />'''%(name))

print('''<input type = "hidden" name = "artist_id" value=%s> '''%(artist_id))
print('''birth year: <input type = "text" name = "edit_artist_birth_year" value=%s> <br />'''%(birth_year))
print('''country: <input type = "text" name = "edit_artist_country" value=%s> <br />'''%(country))





print('''description: <input type = "text" name = "edit_artist_description" value=%s />
<input type = "submit" value = "Submit Edits" />
</form'''%(description))