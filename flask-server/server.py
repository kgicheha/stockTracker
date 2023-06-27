from flask import Flask

app = Flask(__name__)


# DISPLAY ALL ITEMS IN THE WATCHLIST
@app.route("/watchlist")
def watch_list():
    return {
        "stocks": [
            "Apple",
            "Google",
            "Microsoft"
        ]
    }

# ADDING ITEMS TO WATCH LIST

# REMOVING ITEM FROM WATCH LIST

# UPDATING ITEM PRICE IN THE WATCH LIST

# DELETING ITEM FROM WATCH LIST



if __name__ == "__main__":
    app.run(debug=True)


