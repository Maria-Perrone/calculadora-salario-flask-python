"""
Calculadora de Salário Líquido com Flask
Autora: Maria Perrone
Descrição: Aplicação web em Python utilizando Flask para cálculo de salário líquido
com regras de dedução de INSS, IR e bônus por dependentes.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


def calcular_salario_liquido(salario_bruto: float, dependentes: int):
    """
    Regras de cálculo:
    - INSS: 8% do salário bruto.
    - IR: 15% do salário bruto somente quando salário for superior a R$ 2.500,00.
    - Dependentes: Cada dependente acrescenta R$ 200,00 ao resultado final.
    - Fórmula: salário líquido = salário bruto - INSS - IR + (dependentes * 200)
    """
    inss = salario_bruto * 0.08

    if salario_bruto > 2500.0:
        ir = salario_bruto * 0.15
    else:
        ir = 0.0

    bonus_dependentes = dependentes * 200.0
    salario_liquido = salario_bruto - inss - ir + bonus_dependentes

    return {
        "salario_bruto": salario_bruto,
        "inss": inss,
        "ir": ir,
        "dependentes": dependentes,
        "bonus_dependentes": bonus_dependentes,
        "salario_liquido": salario_liquido,
    }


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    erro = None

    if request.method == "POST":
        salario_str = request.form.get("salario_bruto", "").strip().replace(",", ".")
        dependentes_str = request.form.get("dependentes", "").strip()

        try:
            salario_bruto = float(salario_str)
            dependentes = int(dependentes_str)

            if salario_bruto <= 0:
                erro = "O salário bruto deve ser um valor numérico positivo maior que zero."
            elif dependentes < 0:
                erro = "O número de dependentes não pode ser negativo."
            else:
                resultado = calcular_salario_liquido(salario_bruto, dependentes)

        except ValueError:
            erro = "Por favor, insira valores numéricos válidos para salário e dependentes."

    return render_template("index.html", resultado=resultado, erro=erro)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
