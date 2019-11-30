import cgi
import pymysql
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

gallery_name = form.getvalue('gallery_name')
gallery_description = form.getvalue('gallery_description')

artist_name = form.getvalue('artist_name')
artist_birth_year = form.getvalue('artist_birth_year')
artist_country = form.getvalue('artist_country')
artist_description = form.getvalue('artist_description')

editName = form.getvalue('editName')
editDescription = form.getvalue('editDescription')
editID = form.getvalue('editID')

db = pymysql.connect('localhost', 'gallery', 'eecs118', 'gallery')
cur = db.cursor()

if (editName != None and editName != ""):
  sql = ("UPDATE gallery SET name = '%s' WHERE gallery_id = '%s'"%(editName, editID))
  cur.execute(sql)
  db.commit()
if (editDescription != None and editDescription != ""):
  sql = ("UPDATE gallery SET description = '%s' WHERE gallery_id = '%s'"%(editDescription, editID))
  cur.execute(sql)
  db.commit()



if (gallery_name != None):
    sql = "SELECT max(gallery_id) FROM gallery"
    cur.execute(sql)
    for row in cur.fetchall():
        gallery_id = row[0]
    if (gallery_id == None):
        gallery_id = 0
    else:
        gallery_id = gallery_id + 1

    sql = ("""INSERT IGNORE INTO gallery(gallery_id, name, description)
    VALUES("%s", %s, %s)""")
    args = gallery_id, gallery_name, gallery_description
    cur.execute(sql, args)
    db.commit()

if (artist_name != None):
    sql = "SELECT max(artist_id) FROM artist"
    cur.execute(sql)
    for row in cur.fetchall():
        artist_id = row[0] 
    if (artist_id == None):
       artist_id = 0
    else:
        artist_id = artist_id + 1

    sql = ("""INSERT IGNORE INTO artist(artist_id, name, birth_year, country, description)
    VALUES("%s", %s, %s, %s, %s)""")
    args = artist_id, artist_name, artist_birth_year, artist_country, artist_description
    cur.execute(sql, args)
    db.commit()

sql = "SELECT * FROM gallery"
cur.execute(sql)

print("Content-Type: text/html")
print()

print("<html>")
print('''<label id="lblGreetings"></label>''')
print("<ul>")
for row in cur.fetchall():
    gallery_id = row[0]
    name = row[1]
    description = row[2]
    #print("<div>")
    #print('''<button onclick="window.location.href = '/test/cgi-bin/hello_get.py';">Gallery: %s</button>''' % (name))
    print('''<button onclick="window.location.href = '/test/cgi-bin/editGallery.py?gallery_id=%s&name=%s&description=%s';">Edit Gallery</button><br />'''%(gallery_id,name,description))
    print('''<li><a href="/test/cgi-bin/images.py?gallery_id=%s">Gallery: %s Description: %s</a></li> ''' %(gallery_id, name, description))

    
    #print("<div>")
    
    
    #print('''<p>Description: %s </p>''' % (description))
print("</ul>")
print('''
<script>
    var myDate = new Date();
    var hrs = myDate.getHours();

    var greet;

    if (hrs < 12)
        greet = 'Good Morning';
    else if (hrs >= 12 && hrs <= 17)
        greet = 'Good Afternoon';
    else if (hrs >= 17 && hrs <= 24)
        greet = 'Good Evening';

    document.getElementById('lblGreetings').innerHTML =
        '<b>' + greet + '</b> and welcome to my gallery!';
</script> 

<style>
.test {
    float: left;
}
body {
  background-color: lightblue;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  width: 200px;
  background-color: #f1f1f1;
  border: 1px solid #555;
}

li a {
  display: block;
  color: #000;
  padding: 8px 16px;
  text-decoration: none;
}

li {
  text-align: center;
  border-bottom: 1px solid #555;
}
li:last-child {
  border-bottom: none;
}


li a:hover {
  background-color: #555;
  color: white;
}

h2 {
  color: white;
  text-align: center;
}

p {
  font-family: verdana;
  font-size: 20px;
}
input[type=text] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}
</style>
''')
    

#for i in range(5):
 #   print('''<h2>TESTING </h2>''')


print('''<form action = "/test/cgi-bin/hello.py" method = "get">
    gallery name: <input type = "text" name = "gallery_name"> <br />''')

print('''gallery_description: <input type = "text" name = "gallery_description" />
    <input type = "submit" value = "add gallery" />
    </form''')



print('''<form action = "/test/cgi-bin/hw1.py" method = "get">
    artist_name: <input type = "text" name = "artist_name"> <br />''')

print('''artist_birth_year: <input type = "text" name = "artist_birth_year"> <br />''')

print('''artist_country: <input type = "text" name = "artist_country"> <br />''')

print('''artist_description: <input type = "text" name = "artist_description" />
    <input type = "submit" value = "add artist" />
    </form''')


print("</html>")

