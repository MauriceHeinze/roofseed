from app import app, api
from flask import render_template, request, abort


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/gsi/status")
def gsi_status():
    return


@app.route("/find-tree")
def find_view():
    return render_template("find.html")


@app.route("/map")
def map_view():
    print([key for key in request.args.keys()])
    if "plz" not in request.args.keys() and \
       "location" not in request.args.keys():
        return abort(400)
    elif "plz" in request.args.keys():
        long, lat = api.get_plz(request.args.get("plz", type=int))
        trees = api.find_nearby(long, lat)
        return render_template("map.html", trees=trees,
                               location=request.args.get("plz", type=int))
    elif "location" in request.args.keys():
        trees = api.bound_box((), ())
        return render_template("map.html",
                               locals=request.args.get("location"),
                               trees=trees)
