from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://food-lottery-git-main-bilet-13s-projects.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "food lottery backend!"}

@app.get("/weekend_food")
def get_weekend_food():      

    return {'result': ['飯糰', '鬆餅', '韓式炸雞', '炒飯', '八方雲集', '雲南香', '滷味']}
