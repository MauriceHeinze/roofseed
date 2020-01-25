from app import app, api
from app.models import PLZ
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
    use_pages = ("pages" in request.args.keys())
    if "plz" not in request.args.keys() and \
       "location" not in request.args.keys():
        return abort(400)
    elif "plz" in request.args.keys():
        plz = PLZ.query.filter_by(plz=request.args.get("plz", type=int)).first_or_404()
        long, lat = plz.long, plz.lat
        if use_pages:
            trees = api.find_nearby(long, lat,
                                    pages=request.args.get("pages", type=int))
        else:
            trees = api.find_nearby(long, lat)
        return render_template("map.html", trees=trees, long=long, lat=lat,
                               location=request.args.get("plz", type=int))
    elif "location" in request.args.keys():
        trees = api.bound_box((), ())
        return render_template("map.html",
                               locals=request.args.get("location"),
                               trees=trees)


@app.route("/about")
def about_view():
    return render_template("about.html")
