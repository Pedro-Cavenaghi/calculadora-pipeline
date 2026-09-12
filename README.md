# 🧮 Calculadora Pipeline — CI/CD & DevSecOps

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/Pedro-Cavenaghi/calculadora-pipeline/pipeline.yml?branch=main&label=CI%2FCD%20Pipeline&logo=github)
![Dependabot](https://img.shields.io/badge/Dependabot-active-brightgreen?logo=dependabot)
![SonarCloud Quality Gate](https://img.shields.io/sonar/quality_gate/Pedro-Cavenaghi_calculadora-pipeline?server=https%3A%2F%2Fsonarcloud.io&logo=sonarcloud)

Projeto acadêmico focado na implementação de uma esteira completa de **CI/CD e DevSecOps** utilizando Python, GitHub Actions, Dependabot e SonarCloud.

---

## 📌 Arquitetura da Esteira (Pipeline)

A automação do repositório conta com três pilares principais de integração e entrega contínua:

### 1. Testes Automatizados em Matriz (GitHub Actions)
* **Estrutura:** Execução paralela em **3 Sistemas Operacionais** (`ubuntu-latest`, `windows-latest`, `macos-latest`) e **3 Versões do Python** (`3.10`, `3.11`, `3.12`), totalizando 9 combinações de ambiente.
* **Cobertura:** Execução de testes unitários via `pytest` com geração de relatórios de cobertura (`pytest-cov`).

### 2. Gestão de Dependências & Segurança (Dependabot)
* Monitoramento contínuo de vulnerabilidades (CVEs) em bibliotecas declaradas no `requirements.txt`.
* Abertura e atualização automática de Pull Requests para bumps de versão de segurança.

### 3. Análise Estática de Código — SAST (SonarCloud)
* Mapeamento de **Code Smells**, **Bugs** e **Vulnerabilidades/Security Hotspots**.
* Inspeção de trechos de código com riscos de *Code Injection* (ex: `eval()`) e vazamento de credenciais em hardcode (*Hardcoded Secrets*).

---

## 🛠️ Tecnologias e Ferramentas

* **Linguagem:** Python 3.12
* **Testes Unitários:** Pytest & Pytest-Cov
* **Orquestração de CI/CD:** GitHub Actions
* **Análise SAST & Cobertura:** SonarCloud
* **Segurança de Dependências:** GitHub Dependabot

---

## 📂 Estrutura do Repositório

```text
.
├── .github/
│   ├── dependabot.yml           # Configuração de varredura do Dependabot
│   └── workflows/
│       └── pipeline.yml         # Workflow do GitHub Actions (Matriz + SonarCloud)
├── calculadora.py               # Código fonte principal
├── calculadora_test.py          # Suíte de testes unitários
├── requirements.txt             # Dependências do projeto (UTF-8)
├── sonar-project.properties     # Configurações do SonarCloud Scanner
└── README.md                    # Documentação do projeto
