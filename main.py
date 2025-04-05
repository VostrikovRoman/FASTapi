from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

items = [
    {'name': 'Шоколад Алёнка', 'price': '100', 'description':'Молочный шоколад Алёнка'},
    {'name':'Snickers', 'price':'150', 'description':'Шоколадный батончик Snickers с арахисом'},
    {'name':'Молоко Молочная благодать', 'price':'84', 'description':'Молоко свежее пастеризованное Молочная благодать 0,9л'},
    {'name':'Pulpy апельсин', 'price':'109', 'description':'Напиток сокосодержащий из апельсина с мякотью'},
    {'name':'Flash оригинальный 1л', 'price':'132', 'description':'Напиток безалкогольный сильногазированный Флэш ап макс'},
    {'name':'Grand Desert белый шоколад с клубничным муссом', 'price':'154', 'description':'Пудинг молочный ультрапастеризованный с белым шоколадом и сливочно-клубничным муссом'},
]

@app.get("/items")
def get_items(name: Annotated[str|None, Query(min_length=2)] = None, min_price: Annotated[int|None, Query(gt = 0)] = None, max_price:Annotated[int|None, Query(gt=0)]=None):
    result_items = []
    
    if min_price>max_price:
        return 'Ошибка!'
    for i in items:
        if name in i.get('name'):
            result_items.append(i)
    return result_items

# @app.post("/t_square")
# def t_square(a: Annotated[int, Query(ge=0)], b: Annotated[int, Query(ge=0)], c:Annotated[int, Query(ge=0)]):
#     p = a+b+c
#     if (a+b>c) and (b+c>a) and (a+c>b):
#         h_p = p/2
#         s = (h_p*(h_p-a)*(h_p-b)*(h_p-c))**(1/2)
#         return {
#             'perimetr' : p,
#             'square': s
#         }
#     else:
#         return 'Треугольника с указанными сторонами не существует'
