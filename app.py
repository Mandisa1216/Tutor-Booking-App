from app import create_app

app = create_app()
# Fixes
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")




