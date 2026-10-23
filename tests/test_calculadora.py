"""
Testes automatizados das regras de negócio do cálculo de salário líquido.
Casos de teste validados com base no Relatório de Atividade Prática.
"""

from app import calcular_salario_liquido


def test_caso_1_salario_3000_dois_dependentes():
    """
    R$ 3.000,00 e 2 dependentes:
    - INSS = R$ 240,00 (8%)
    - IR = R$ 450,00 (15% pois > 2.500)
    - Dependentes = R$ 400,00 (2 x 200)
    - Resultado = 3000 - 240 - 450 + 400 = R$ 2.710,00
    """
    res = calcular_salario_liquido(3000.0, 2)
    assert res["inss"] == 240.0
    assert res["ir"] == 450.0
    assert res["bonus_dependentes"] == 400.0
    assert res["salario_liquido"] == 2710.0


def test_caso_2_salario_2000_um_dependente():
    """
    R$ 2.000,00 e 1 dependente:
    - INSS = R$ 160,00 (8%)
    - IR = R$ 0,00 (isento pois <= 2.500)
    - Dependentes = R$ 200,00 (1 x 200)
    - Resultado = 2000 - 160 + 200 = R$ 2.040,00
    """
    res = calcular_salario_liquido(2000.0, 1)
    assert res["inss"] == 160.0
    assert res["ir"] == 0.0
    assert res["bonus_dependentes"] == 200.0
    assert res["salario_liquido"] == 2040.0


def test_caso_3_salario_1000_zero_dependentes():
    """
    R$ 1.000,00 e 0 dependentes:
    - INSS = R$ 80,00 (8%)
    - IR = R$ 0,00
    - Dependentes = R$ 0,00
    - Resultado = 1000 - 80 = R$ 920,00
    """
    res = calcular_salario_liquido(1000.0, 0)
    assert res["inss"] == 80.0
    assert res["ir"] == 0.0
    assert res["bonus_dependentes"] == 0.0
    assert res["salario_liquido"] == 920.0
