#!/usr/bin/env /bin/python3
print("Content-Type:text/html")
print()
import cgi
print("<h1> Bienvenu sur le programme test </h1>")
print("<hr>")

dat=cgi.FieldStorage()
nom=dat.getvalue("a")
prenom=dat.getvalue("b")

y2meta.com-Python Database(mysql) connection Using XAMPP with HTML-Form-(1080p)

# print("<p>nom : ",nom,"</p><br>")
# print("<p>Prenom : ",prenom,"</p>")
