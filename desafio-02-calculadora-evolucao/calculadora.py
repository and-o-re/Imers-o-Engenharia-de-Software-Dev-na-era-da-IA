#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Desafio 02: Evolução da Calculadora com Porcentagem e Testes Automatizados
Tema: CYBERDECK CALC // NIGHT CITY OS v2.1 PATCH UPDATE (Homenagem a Cyberpunk 2077)
"""

# Códigos ANSI para estética Cyberpunk 2077 no terminal
AMARELO_NEON = "\033[93m"
CIANO_CYBER = "\033[96m"
VERMELHO_GLITCH = "\033[91m"
VERDE_MATRIX = "\033[92m"
MAGENTA_EDGERUNNER = "\033[95m"
NEGRITO = "\033[1m"
RESET = "\033[0m"


def somar(a: float, b: float) -> float:
    """Realiza a adição entre dois números."""
    return a + b


def subtrair(a: float, b: float) -> float:
    """Realiza a subtração entre dois números."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Realiza a multiplicação entre dois números."""
    return a * b


def dividir(a: float, b: float) -> float:
    """
    Realiza a divisão entre dois números.
    Lança ValueError caso o divisor (b) seja zero.
    """
    if b == 0:
        raise ValueError("ERRO CRÍTICO DE ICE: Divisão por zero detectada no Cyberdeck!")
    return a / b


def calcular_porcentagem(valor_base: float, percentual: float) -> float:
    """
    Calcula quanto representa 'percentual'% de 'valor_base'.
    Exemplo: calcular_porcentagem(200, 15) -> 30.0 (15% de 200).
    """
    return (valor_base * percentual) / 100.0


def exibir_painel() -> None:
    """Exibe o cabeçalho e o menu interativo no estilo HUD de Cyberpunk 2077 v2.1."""
    print(f"\n{AMARELO_NEON}{NEGRITO}╔══════════════════════════════════════════════════════════╗{RESET}")
    print(f"{AMARELO_NEON}{NEGRITO}║   ⚡ ARASAKA CYBERDECK // CALCULADORA TERMINAL v2.1 ⚡   ║{RESET}")
    print(f"{AMARELO_NEON}{NEGRITO}║     [PATCH 2.1 - MÓDULO DE PORCENTAGEM & TELEMETRIA]     ║{RESET}")
    print(f"{AMARELO_NEON}{NEGRITO}╠══════════════════════════════════════════════════════════╣{RESET}")
    print(f"{CIANO_CYBER}║  [1] ➕ Adição (+)                                       ║{RESET}")
    print(f"{CIANO_CYBER}║  [2] ➖ Subtração (-)                                    ║{RESET}")
    print(f"{CIANO_CYBER}║  [3] ✖️  Multiplicação (*)                                ║{RESET}")
    print(f"{CIANO_CYBER}║  [4] ➗ Divisão (/)                                      ║{RESET}")
    print(f"{VERDE_MATRIX}║  [5] 📊 Porcentagem (% de um valor)   [NOVO PATCH]       ║{RESET}")
    print(f"{MAGENTA_EDGERUNNER}║  [0] 🔌 Desconectar do Cyberdeck (Sair)                  ║{RESET}")
    print(f"{AMARELO_NEON}{NEGRITO}╚══════════════════════════════════════════════════════════╝{RESET}")


def ler_numero(mensagem: str) -> float:
    """Lê e valida um número de ponto flutuante digitado pelo usuário."""
    while True:
        entrada = input(f"{CIANO_CYBER}{mensagem}{RESET}").strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print(
                f"{VERMELHO_GLITCH}[FALHA DE SINAL] Entrada inválida ('{entrada}'). "
                f"Digite um valor numérico válido.{RESET}"
            )


def executar_calculadora() -> None:
    """Loop principal de execução interativa da calculadora v2.1."""
    operacoes = {
        "1": ("+", somar, "ADIÇÃO"),
        "2": ("-", subtrair, "SUBTRAÇÃO"),
        "3": ("*", multiplicar, "MULTIPLICAÇÃO"),
        "4": ("/", dividir, "DIVISÃO"),
        "5": ("%", calcular_porcentagem, "PORCENTAGEM"),
    }

    while True:
        exibir_painel()
        opcao = input(f"{AMARELO_NEON}>> Selecione o protocolo de operação [0-5]: {RESET}").strip()

        if opcao == "0":
            print(f"\n{MAGENTA_EDGERUNNER}[SISTEMA] Desconectando da rede de Night City... See ya, Choom!{RESET}\n")
            break

        if opcao not in operacoes:
            print(f"{VERMELHO_GLITCH}[ALERTA] Protocolo '{opcao}' inexistente! Escolha entre 0 e 5.{RESET}")
            continue

        simbolo, funcao, nome_operacao = operacoes[opcao]
        print(f"\n{AMARELO_NEON}--- [ MÓDULO ATIVO: {nome_operacao} ] ---{RESET}")

        if opcao == "5":
            valor_base = ler_numero("Digite o valor base (ex: 250): ")
            percentual = ler_numero("Digite a porcentagem desejada (ex: 20 para 20%): ")
            resultado = funcao(valor_base, percentual)
            print(
                f"\n{VERDE_MATRIX}{NEGRITO}[TELEMETRIA OK] Resultado: "
                f"{percentual:g}% de {valor_base:g} = {resultado:g}{RESET}"
            )
        else:
            num1 = ler_numero("Digite o primeiro operando: ")
            num2 = ler_numero("Digite o segundo operando: ")

            try:
                resultado = funcao(num1, num2)
                print(
                    f"\n{VERDE_MATRIX}{NEGRITO}[TELEMETRIA OK] Resultado: "
                    f"{num1:g} {simbolo} {num2:g} = {resultado:g}{RESET}"
                )
            except ValueError as erro:
                print(f"\n{VERMELHO_GLITCH}{NEGRITO}[FALHA DE EXECUÇÃO] {erro}{RESET}")


if __name__ == "__main__":
    executar_calculadora()
