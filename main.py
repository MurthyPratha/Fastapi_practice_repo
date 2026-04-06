from fastapi import FastAPI








app = FastAPI()

@app.get("/")
def greet():
    return 'Hello bhai'


@app.get("/books")
def get_all_books():
    return 'All books are given'