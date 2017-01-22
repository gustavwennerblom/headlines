import feedparser
from flask import Flask


app=Flask(__name__)

ABSB_FEED="http://www.aftonbladet.se/sportbladet/rss.xml"

@app.route("/")
def get_news():
    feed=feedparser.parse(ABSB_FEED)
    first_article=feed['entries'][0]
    return """<html>
      <body>
        <h1> Sportbladet Headlines </h1>
        <b>{0} </b><br/>
        <i>{1] </i><br/>
      </body>
    </html>""".format(firstarticle.get("title"), firstarticle.get("pubDate")

if __name__=='__main__':
    app.run(port=5000, debug=True)

