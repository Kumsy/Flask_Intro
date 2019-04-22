"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.
                <a href="/hello">Go to hello</a>
              </html>"""


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br> Choose your compliments:
          <input type="radio" name="compliments" value="cool">You're cool!
          <input type="radio" name="compliments" value="great">You're great!<br>
          <input type="submit" value="Submit">
        </form>
        <br>
        <br>

        <form action="/diss">
        What's your name?<input type="text" name="person">
          <br> 
          Choose your compliments:
            <input type="radio" name="diss" value="not good">Not good!
            <input type="radio" name="diss" value="not great!">Not great!
          <br>
            <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route("/diss")
def diss_person():
  """Diss you"""

  player = request.args.get("person")

  diss = request.args.get("diss")

  return f"""
  <!doctype html>
  <html>
    <head>
      <title>We hate you!</title>
    </head>
    <body>
    
      Hi, {player}! I think you're {diss}!
  
    </body>
  </html>
  """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)
    compliment = request.args.get("compliments")


    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
