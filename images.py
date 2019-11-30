import cgi
import pymysql
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

findType = form.getvalue('findType')
minYear = form.getvalue('minYear')
maxYear = form.getvalue('maxYear')
findName = form.getvalue('findName')
findLocation = form.getvalue('findLocation')

delete_detail_id = form.getvalue('delete_detail_id')
delete_image_id = form.getvalue('delete_image_id')


gallery_name = form.getvalue('gallery_name')
gallery_description = form.getvalue('gallery_description')
#gallery_id = form.getvalue('gallery_id')



editTitle = form.getvalue('editTitle')
editLink = form.getvalue('editLink')
#editID = form.getvalue('editID')
editImageID = form.getvalue('editImageID')
editDetailID = form.getvalue('editDetailID')
editYear = form.getvalue('editYear')
editType = form.getvalue('editType')
editWidth = form.getvalue('editWidth')
editHeight = form.getvalue('editHeight')
#editLocation = form.getvalue('editLocation')
editDescription = form.getvalue('editDescription')


title = form.getvalue("title")
link = form.getvalue("link")
gallery_id = form.getvalue("gallery_id")
artist_id = form.getvalue("artist_id")
detail_id = 0
year = form.getvalue("year")
imageType = form.getvalue("type")
width = form.getvalue("width")
height = form.getvalue("height")
location = form.getvalue("location")
description = form.getvalue("description")



db = pymysql.connect('localhost', 'gallery', 'eecs118', 'gallery')
cur = db.cursor()

if (delete_detail_id != None):
  sql = "DELETE FROM image WHERE image_id = %s AND gallery_id = %s"%(delete_image_id, gallery_id)
  cur.execute(sql)
  db.commit()
  sql = "DELETE FROM detail WHERE detail_id = %s AND image_id = %s"%(delete_detail_id, delete_image_id)
  cur.execute(sql)
  db.commit()

if (editTitle != None and editTitle != ""):
  sql = ("UPDATE image SET title = '%s' WHERE gallery_id = '%s' AND image_id = '%s'"%(editTitle, gallery_id, editImageID))
  cur.execute(sql)
  db.commit()
if (editLink != None and editLink != ""):
  sql = ("UPDATE image SET link = '%s' WHERE gallery_id = '%s' AND image_id = '%s'"%(editLink, gallery_id, editImageID))
  cur.execute(sql)
  db.commit()
  sql = ("UPDATE detail SET year =%s, type ='%s', width=%s, height=%s, description='%s' WHERE detail_id =%s"%(editYear, editType, editWidth, editHeight, editDescription, editDetailID))
  cur.execute(sql)
  db.commit()


sql = "SELECT max(detail_id) FROM detail"
cur.execute(sql)
if (title != None):
    for row in cur.fetchall():
        detail_id = row[0] 
    if (detail_id == None):
       detail_id = 0
    else:
      detail_id = detail_id+1


sql = "SELECT max(image_id) FROM image"
cur.execute(sql)
if (title != None):
    for row in cur.fetchall():
        image_id = row[0] 
    if (image_id == None):
       image_id = 0
    else:
        image_id = image_id + 1
    sql = ("""INSERT IGNORE INTO image(image_id, title, link, gallery_id, artist_id, detail_id)
    VALUES("%s", %s, %s, %s, %s, %s)""")
    args = image_id, title, link, gallery_id, artist_id, detail_id
    cur.execute(sql, args)
    db.commit()
    sql = ("""INSERT IGNORE INTO detail(detail_id, image_id, year, type, width, height, location, description)
    VALUES("%s", %s, %s, %s, %s, %s, %a, %s)""")
    args = detail_id, image_id, year, imageType, width, height, location, description
    cur.execute(sql, args)
    db.commit()
     



print("Content-Type: text/html")
print()


print("<html>")
print('''<button onclick="window.location.href = '/test/cgi-bin/gallery.py';">Return to galleries</button>''' )

print('''<form action = "/test/cgi-bin/images.py" method = "get">
    find images by type: <input type = "text" name = "findType"> ''')
print('''<input type = "hidden" name = "gallery_id" value=%s> '''%(gallery_id))

print('''
    <input type = "submit" value = "find" />
    </form>''')

print('''<form action = "/test/cgi-bin/images.py" method = "get">
    minimum year: <input type = "text" name = "minYear"> ''')
print('''<input type = "hidden" name = "gallery_id" value=%s> '''%(gallery_id))
print('''maximum year: <input type = "text" name = "maxYear" /> 
    <input type = "submit" value = "find" /> 
    </form><br />''')

print('''<form action = "/test/cgi-bin/images.py" method = "get">
    find images by artist name: <input type = "text" name = "findName"> ''')
print('''<input type = "hidden" name = "gallery_id" value=%s> '''%(gallery_id))
print('''
    <input type = "submit" value = "find" /> 
    </form><br />''')

print('''<form action = "/test/cgi-bin/images.py" method = "get">
    find images by location: <input type = "text" name = "findLocation"> ''')
print('''<input type = "hidden" name = "gallery_id" value=%s> '''%(gallery_id))
print('''
    <input type = "submit" value = "find" /> 
    </form><br />''')




sql = "SELECT COUNT(image_id) FROM image WHERE gallery_id = %s"
cur.execute(sql, gallery_id)
print("<h3>There are currently %s images in this gallery</h3>" % (cur.fetchone()[0]))
print("<h1>Helloo world!</h1>")
print("<ul>")

if (findType != None and findType != ""):
  sql = ("SELECT detail_id FROM detail WHERE type = '%s'"%(findType))
  cur.execute(sql)
  z = "("
  for row in cur.fetchall():
    z = z + str(row[0]) + ","
  z = z[:-1]
  z += ")"
  
  sql = "SELECT * FROM image WHERE detail_id IN %s"%z
if (minYear != None and maxYear != None and minYear != "" and maxYear != ""):
  sql = "SELECT detail_id FROM detail WHERE year > %s AND year < %s"%(minYear, maxYear)
  cur.execute(sql)
  z = "("
  for row in cur.fetchall():
    z = z + str(row[0]) + ","
  
  z = z[:-1]
  z += ")"
  sql = "SELECT * FROM image WHERE detail_id IN %s"%z
if(findName != None and findName != ""):
  sql = ("SELECT detail_id FROM detail WHERE name = '%s'"%(findName))
  cur.execute(sql)
  z = "("
  for row in cur.fetchall():
    z = z + str(row[0]) + ","
  z = z[:-1]
  z += ")"
  
  sql = "SELECT * FROM image WHERE detail_id IN %s"%z
if(findLocation != None and findLocation != ""):
  sql = ("SELECT detail_id FROM detail WHERE location = '%s'"%(findLocation))
  cur.execute(sql)
  z = "("
  for row in cur.fetchall():
    z = z + str(row[0]) + ","
  z = z[:-1]
  z += ")"
  
  sql = "SELECT * FROM image WHERE detail_id IN %s"%z
else:
  sql = ("SELECT * FROM image WHERE gallery_id = %s"%(gallery_id))
cur.execute(sql)
for row in cur.fetchall():
    sql = ("SELECT * FROM detail WHERE detail_id = %s"%(row[5]))
    cur.execute(sql)
    z = cur.fetchall()[0]
    #print(z)
    #print('''<button onclick="window.location.href = '/test/cgi-bin/editImage.py?image_id=%s&gallery_id=%s&title=%s&link=%s&detail_id=%s&year=%s&imageType=%s&width=%s&height=%s&location=%s&description=%s';">Edit Image</button><br />'''%(row[0],gallery_id,row[1],row[2],z[0],z[2], z[3],z[4], z[5], z[6], z[7]))
    print('''<button onclick="window.location.href = '/test/cgi-bin/editImage.py?image_id=%s&gallery_id=%s&title=%s&link=%s&detail_id=%s&year=%s&imageType=%s&width=%s&height=%s&description=%s';">Edit Image</button><br />'''%(row[0],gallery_id,row[1],row[2],z[0],z[2], z[3],z[4], z[5],z[7]))
    print('''<button onclick="window.location.href = '/test/cgi-bin/images.py?gallery_id=%s&delete_image_id=%s&delete_detail_id=%s';">Delete Image</button><br />'''%(gallery_id,row[0],row[5]))
    print('''<li><a href="/test/cgi-bin/artist.py?artist_id=%s&gallery_id=%s">
    <h1>%s</h1><br />
    <img src="%s" alt="" height="%s" width="%s"><br />
    <p>Year: %s</p><br />
    <p>Type: %s</p><br />
    <p>Location: %s</p><br />
    <p>Description: %s</p><br />
    </a></li>''' % (row[4],gallery_id,row[1],row[2], z[5], z[4], z[2], z[3], z[6], z[7]))
    
    
print("</ul>")
print('''<button onclick="window.location.href = '/test/cgi-bin/addImage.py?gallery_id=%s';">add an image</button>'''%(gallery_id))
print('''
<style>
body {
  background-color: lightblue;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  width: 800px;
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
</style>
''')
    




print("</html>")

