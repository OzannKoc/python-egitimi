from flask import Blueprint, render_template, request, redirect
from utils.Db import Db

anasayfa = Blueprint('anasayfa',__name__,
                 url_prefix="/anasayfa")

def sort(val):
    return val[3]

@anasayfa.route("/")
def index():
    databse = Db()
    sql = """ select * from "BlogYazisi" """
    data = databse.read_data(sql)
    data.sort(key = sort, reverse = True)
    return render_template("anasayfa/index.html", data=data)

@anasayfa.route("/<string:id>")
def tekIndexGoster(id):
    database = Db()
    sql = """ select * from "BlogYazisi" where "Id" = %s """
    data = database.read_data(sql, (id,))
    sql2 = """ select * from "Yorum" where "BlogId" = %s """
    data2 = database.read_data(sql2,(id,))
    return render_template("anasayfa/indexDetay.html", data=data, iki=data2)

@anasayfa.route("/yorum/save", methods=["POST"])
def save():
    blogId = request.form.get("BlogId")
    ekleyen = request.form.get("Ekleyen")
    yorum = request.form.get("Yorum")

    database = Db()

    sql = """ insert into "Yorum" ("BlogId","Yorum","Ekleyen") values (%s,%s,%s) """
    database.execute(sql, (blogId, yorum, ekleyen))
    #return render_template("anasayfa/indexDetay.html")
    return redirect("/anasayfa")