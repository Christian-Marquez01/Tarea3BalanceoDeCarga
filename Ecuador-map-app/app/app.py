import os
import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)

def get_provincias():
    conn = mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "localhost"),
        user=os.environ.get("MYSQL_USER", "root"),
        password=os.environ.get("MYSQL_PASSWORD", "zznk"),
        database=os.environ.get("MYSQL_DB", "ecuador")
    )
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, capital, area, poblacion, latitud, longitud FROM provincias")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route("/")
def index():
    provincias = get_provincias()
    return render_template("index.html", provincias=provincias)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
