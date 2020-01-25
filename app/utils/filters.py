from app import app


@app.template_filter("readify")
def readify(str):
    return str.title()
