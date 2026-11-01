#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Suíte de Testes Automatizados para a Calculadora Cyberdeck v2.1
Compatível com unittest (biblioteca padrão) e pytest.
"""

import unittest
from calculadora import (
    somar,
    subtrair,
    multiplicar,
    dividir,
    calcular_porcentagem,
)


class TestCalculadoraCyberdeck(unittest.TestCase):
    """Testes unitários validando todas as operações matemáticas da calculadora."""

    def test_somar(self):
        """Valida a operação de adição com positivos, negativos e decimais."""
        self.assertEqual(somar(10, 5), 15)
        self.assertEqual(somar(-10, 5), -5)
        self.assertEqual(somar(-4, -6), -10)
        self.assertAlmostEqual(somar(2.5, 3.75), 6.25)

    def test_subtrair(self):
        """Valida a operação de subtração."""
        self.assertEqual(subtrair(20, 8), 12)
        self.assertEqual(subtrair(5, 15), -10)
        self.assertEqual(subtrair(-5, -5), 0)
        self.assertAlmostEqual(subtrair(10.5, 0.25), 10.25)

    def test_multiplicar(self):
        """Valida a operação de multiplicação, incluindo por zero e negativos."""
        self.assertEqual(multiplicar(7, 6), 42)
        self.assertEqual(multiplicar(999, 0), 0)
        self.assertEqual(multiplicar(-4, 5), -20)
        self.assertEqual(multiplicar(-3, -3), 9)
        self.assertAlmostEqual(multiplicar(2.5, 4.0), 10.0)

    def test_dividir_valores_validos(self):
        """Valida a operação de divisão com divisores diferentes de zero."""
        self.assertEqual(dividir(20, 4), 5.0)
        self.assertEqual(dividir(-15, 3), -5.0)
        self.assertAlmostEqual(dividir(7, 2), 3.5)
        self.assertEqual(dividir(0, 10), 0.0)

    def test_dividir_por_zero_lanca_excecao(self):
        """Garante que dividir por zero lança um ValueError explícito."""
        with self.assertRaises(ValueError) as contexto:
            dividir(2077, 0)
        self.assertIn("Divisão por zero", str(contexto.exception))

    def test_calcular_porcentagem(self):
        """Valida o cálculo de porcentagem sobre diversos valores base."""
        self.assertEqual(calcular_porcentagem(200, 15), 30.0)
        self.assertEqual(calcular_porcentagem(1000, 50), 500.0)
        self.assertEqual(calcular_porcentagem(500, 0), 0.0)
        self.assertAlmostEqual(calcular_porcentagem(80, 12.5), 10.0)
        self.assertAlmostEqual(calcular_porcentagem(250, 100), 250.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
