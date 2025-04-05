from fastapi import FastAPI, Query
from 

app = FastAPI()

@app.get("/items")
def get_items():
    return 0

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
