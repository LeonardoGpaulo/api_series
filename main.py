from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Mensagem": "Óla, mundo!"}

@app.get("/itens/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/soma/{num1}/{num2}")
async def soma(num1: int, num2: int):
    return {"soma": num1 + num2} 

@app.get("/subtracao/{num1}/{num2}")
async def sub(num1: int, num2: int):
    return {"subtração": num1 - num2}

@app.get("/multiplicacao/{num1}/{num2}")
async def mult(num1: int, num2: int):
    return {"Multiplicação": num1 * num2}

@app.get("/divisao/{num1}/{num2}")
async def div(num1: int, num2: int):
    return {"divisão": num1 // num2}

@app.get("/resto/{num1}/{num2}")
async def resto(num1: int, num2: int):
    return {"resto": num1 % num2}

@app.get("/IMC/{peso}/{altura}")
async def IMC(peso: int, altura: float):
    return {"IMC": peso / (altura * 2)}

@app.get("/impopar/{num}")
async def impopar(num: int):
    if num % 2 == 0:
        return {"par"}
    else:
        return {"impar"}

#Crie uma rota que retorne a soma de dois números passados por caminho(path de url)

#Extra:melhore a tipagem do código usando tipos de módulo typing onde for  necessário