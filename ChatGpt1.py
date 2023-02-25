# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 23:38:07 2023

@author: SISTRAM4
"""
import openai
#import os
import speech_recognition as sr
import pyttsx3

# Cria um reconhecedor de voz
r = sr.Recognizer()

# Abre o microfone para capturar o áudio
with sr.Microphone() as source:
    print("Fale algo...")
    audio = r.listen(source)

# Utiliza a API do Google Speech-to-Text para converter o áudio em texto
try:
    text = r.recognize_google(audio, language="pt-BR")
    print("Você disse: ", text)
    #chama o chat gpt
    # Define a chave de API
    openai.api_key = "xxxxxxxx"

    # Define o modelo a ser usado (pode ser um dos modelos disponíveis na plataforma OpenAI)
    model_engine = "text-davinci-002"
    #model_engine = "text-curie-001"
    #model_engine = "text-babbage-001"
    #model_engine = "text-ada-001"

    # Define a entrada de texto
    prompt = text

    # Define as configurações da chamada da API
    completion = openai.Completion.create(       
        
        engine=model_engine,
        prompt=prompt,
        max_tokens=300
        )

    # Extrai o texto gerado pela API
    output = completion.choices[0].text

    # Exibe o texto gerado
    print(output)
    # initialize the text-to-speech engine
    engine = pyttsx3.init()

    # convert text to speech
    engine.say(output)
    engine.runAndWait()
    
    #fim chamada chat gpt
    
    
    
except sr.UnknownValueError:
    print("Não foi possível entender o que você disse.")
except sr.RequestError as e:
    print("Não foi possível conectar-se com o serviço de reconhecimento de voz do Google. Erro: {0}".format(e))