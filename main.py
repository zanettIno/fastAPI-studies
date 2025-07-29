from fastapi import FastAPI, UploadFile, File, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import os
import requests
import json

# raise HTTPException(status_code = <erro>, detail="<mensagem>")

app = FastAPI()
template = Jinja2Templates(directory="template")

def IA(param : str):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer <API-KEY>",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
            "messages": [{
                "role": "user",
                "content": f'Fale apenas em PT-BR e analise as informacoes a seguir, me de uma analise direta ao ponto: {param}'
            }],
        })
    )

    data = response.json()
    return data['choices'][0]['message']['content']

# curl -X GET http://127.0.0.1:8000/ 
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@app.post("/insercao/")
async def insercaoArquivo(arquivo: UploadFile = File(...)):
    
    tipoArq, nomeArq = arquivo.content_type, arquivo.filename
    print(f'Arquivo recebido de nome: {nomeArq} e tipo: {tipoArq}')

    conteudo = await arquivo.read()
    
    match tipoArq:
       
        # Trabalhando com chaves pré-estabelecidas pelo contexto do estudo
        case "application/json":
            dict = json.loads(conteudo)
            proc = f"texto1: {dict['texto1']}; texto2:{dict['texto2']}"
    
            result = str(IA(proc))

            result = result.replace("*", "")
            newResult = result.replace("\n", "")

            return newResult

        case _:    
            proc = str(conteudo.decode())
            result = str(IA(proc))

            result = result.replace("*", "")
            newResult = result.replace("\n", "")
            
            return newResult
    
    arquivo.close()