from fastapi import FastAPI, Query
from typing import Annotated
from random import randint

app = FastAPI()

@app.get("/about")
def about():
    return {
        'surname': 'Востриков',
        'name': 'Роман',
        'lastname': 'Андреевич',
        'institute': 'Нижнетагильский технологический институт (НТИ)',
        'group': 'Т-323901-ИСиТ',
        'age': '20',
        'hobbies': [
            'Музыка', 'Рисование', 'Разработка игр'
        ]
    }

@app.get("/rnd")
def random():
    return(randint(0, 10))

@app.post("/t_square")
def t_square(a: Annotated[int, Query(ge=0)], b: Annotated[int, Query(ge=0)], c:Annotated[int, Query(ge=0)]):
    p = a+b+c
    if (a+b>c) and (b+c>a) and (a+c>b):
        h_p = p/2
        s = (h_p*(h_p-a)*(h_p-b)*(h_p-c))**(1/2)
        return {
            'perimetr' : p,
            'square': s
        }
    else:
        return 'Треугольника с указанными сторонами не существует'
    

