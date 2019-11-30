import cgi
import pymysql
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
artist_id = form.getvalue('artist_id')
artist_name = form.getvalue('artist_name')
artist_birth_year = form.getvalue('artist_birth_year')
artist_country = form.getvalue('artist_country')
artist_description = form.getvalue('artist_description')
gallery_id = form.getvalue('gallery_id')

#edit_artist_id = form.getvalue('edit_artist_id')
edit_artist_name = form.getvalue('edit_artist_name')
edit_artist_birth_year = form.getvalue('edit_artist_birth_year')
edit_artist_country = form.getvalue('edit_artist_country')
edit_artist_description = form.getvalue('edit_artist_description')

db = pymysql.connect('localhost', 'gallery', 'eecs118', 'gallery')
cur = db.cursor()

if (edit_artist_name != None):
    sql = "UPDATE artist SET name=%s,birth_year=%s,country=%s,description=%s WHERE artist_id=%s"%(edit_artist_name,edit_artist_birth_year,edit_artist_country, edit_artist_description, artist_id)
    cur.execute(sql)
    db.commit()
if (artist_name != None):
    sql = ("""INSERT IGNORE INTO artist(artist_id, name, birth_year, country, description)
    VALUES("%s", %s, %s, %s, %s)""")
    args = artist_id, artist_name, artist_birth_year, artist_country, artist_description
    cur.execute(sql, args)
    db.commit()
    print("HELLO")

sql = "SELECT * FROM artist WHERE artist_id = %s"%(artist_id)
cur.execute(sql)
print("Content-Type: text/html")
print()


print("<html>")
if (gallery_id != None and gallery_id != ""):
    print('''<button onclick="window.location.href = '/test/cgi-bin/images.py?gallery_id=%s';">Return to Images</button>'''%(gallery_id))
print('''<button onclick="window.location.href = '/test/cgi-bin/gallery.py';">Return to Galleries</button>''')

#print(cur.fetchall()[0])
    
for row in cur.fetchall():
    print('''<li>
    
    <p>name: %s</p><br />
    <p>birth year: %s</p><br />
    <p>country: %s</p><br />
    <p>description: %s</p><br />
    </li>'''%(row[1],row[2],row[3],row[4]))
    print('''<button onclick="window.location.href = '/test/cgi-bin/editArtist.py?artist_id=%s&name=%s&birth_year=%s&country=%s&description=%s';">Edit Image</button><br />'''%(artist_id,row[1],row[2],row[3],row[4]))

    


print('''<button onclick="window.location.href = '/test/cgi-bin/addArtist.py';">add an artist</button>''')
print("</html>")