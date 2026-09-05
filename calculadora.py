import os
import pickle

# SIMULAÇÃO DE VULNERABILIDADE 1: Hardcoded Secret / Key (Security Hotspot)
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE_SECRET_KEY_EXPOSED"
DATABASE_PASSWORD = "admin_password_12345"

def login_inseguro(usuario, senha):
    # SIMULAÇÃO DE VULNERABILIDADE 2: Hardcoded Credential Check
    if usuario == "admin" and senha == "Admin@123456":
        return True
    return False

def executar_comando_perigoso(entrada_usuario):
    # SIMULAÇÃO DE VULNERABILIDADE 3: Uso de eval() (Code Injection Risk)
    # O SonarCloud marca como Vulnerabilidade de Alta Gravidade
    return eval(entrada_usuario)

def carregar_dados_pickle(dados_bytes):
    # SIMULAÇÃO DE VULNERABILIDADE 4: Deserialização insegura de dados
    return pickle.loads(dados_bytes)

def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    if b == 0:
        raise ValueError("Divisão por zero não permitida")
    else:
        return a / b

