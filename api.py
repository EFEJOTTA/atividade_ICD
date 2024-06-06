import openai

def escolher_palavra_da_api(numero_letras, dificuldade, idioma):
    openai.api_key = 'sk-proj-YK4xMQw9C5mm2gq5z4xbT3BlbkFJ1lzwdxu2uuvp8b7wVUGd'
    
    prompt = f"Escolha uma palavra em {idioma} com {numero_letras} letras e dificuldade {dificuldade}."
    
    response = openai.Completion.create(
        model = "gpt-3.5-turbo-0125",
        prompt=prompt,
        max_tokens=10
    )
    
    palavra = response.choices[0].text.strip()
    return palavra
