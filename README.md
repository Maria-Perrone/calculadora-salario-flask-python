# 💰 Calculadora de Salário Líquido com Flask & Python

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Bootstrap 5](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Tests](https://img.shields.io/badge/Pytest-Automated%20Tests-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)

Aplicação web desenvolvida em **Python** utilizando o microframework **Flask**, criada para simular e automatizar o cálculo do salário líquido a partir do salário bruto e da quantidade de dependentes legais, aplicando regras trabalhistas e tributárias.

---

## 🧮 Regras de Negócio e Cálculos

A aplicação segue as especificações acadêmicas de folha de pagamento:

1. **INSS:** Desconto fixo de **8%** sobre o salário bruto.
2. **Imposto de Renda (IR):**
   - Isento para salários brutos até **R$ 2.500,00**.
   - Desconto de **15%** sobre o salário bruto quando este for estritamente superior a **R$ 2.500,00**.
3. **Dedução / Bônus por Dependentes:**
   - Cada dependente cadastrado adiciona **R$ 200,00** ao saldo final do trabalhador.
4. **Fórmula Geral:**
   $$\text{Salário Líquido} = \text{Salário Bruto} - \text{INSS} - \text{IR} + (\text{Dependentes} \times 200,00)$$

---

## 📊 Matriz de Casos de Teste Homologados

| Salário Bruto | Dependentes | INSS (8%) | IR (15%) | Bônus Dependentes | Salário Líquido Final |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **R$ 3.000,00** | 2 | R$ 240,00 | R$ 450,00 | + R$ 400,00 | **R$ 2.710,00** |
| **R$ 2.000,00** | 1 | R$ 160,00 | R$ 0,00 (Isento) | + R$ 200,00 | **R$ 2.040,00** |
| **R$ 1.000,00** | 0 | R$ 80,00 | R$ 0,00 (Isento) | R$ 0,00 | **R$ 920,00** |

---

## 🛡️ Validações e Tratamento de Erros

A aplicação implementa validações robustas no backend:
- Bloqueia e informa mensagens amigáveis em caso de salários menores ou iguais a zero.
- Rejeita valores negativos de dependentes.
- Trata caracteres não-numéricos ou formatações inconsistentes (aceita vírgula ou ponto decimal).

---

## 🚀 Como Executar Localmente

### Pré-requisitos
- Python 3.10 ou superior instalado.

### 1. Clonar o repositório
```bash
git clone https://github.com/Maria-Perrone/calculadora-salario-flask-python.git
cd calculadora-salario-flask-python
```

### 2. Criar e ativar ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
# No Windows PowerShell:
.\venv\Scripts\Activate.ps1
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Executar os testes automatizados
```bash
pytest tests/
```

### 5. Iniciar a aplicação Flask
```bash
python app.py
```
Acesse no seu navegador: **`http://127.0.0.1:5000`**

---

## 👩‍💻 Autora

Desenvolvido por **Maria Perrone**.
- Curso: Análise e Desenvolvimento de Sistemas — Faculdade Anhanguera
- GitHub: [@Maria-Perrone](https://github.com/Maria-Perrone)
- E-mail: Perronem808@gmail.com
