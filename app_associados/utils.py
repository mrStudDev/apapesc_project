
#Função Produção Anual
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def validar_quantidade(valor):
    """
    Valida e converte uma string no formato brasileiro (ex.: 1.234,56) para float.
    """
    if valor:
        # Remove separadores de milhares e substitui vírgula por ponto
        valor = valor.replace('.', '').replace(',', '.')
        try:
            valor = float(valor)
            if valor < 0:
                raise ValueError("A quantidade não pode ser negativa.")
        except ValueError:
            raise ValueError("Digite um número válido no formato 000.000,00.")
    return valor

def formatar_valor_brasileiro(valor):
    """
    Formata um número para o padrão brasileiro: 1.234,56.
    """
    try:
        valor = float(valor)
        return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return valor