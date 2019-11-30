import cgi

<style>
input[type=text] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}
</style>

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