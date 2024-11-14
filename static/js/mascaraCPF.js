function mascaraCPF(input) {
  let valor = input.value.replace(/\D/g, ''); // Remove não-números
  if (valor.length > 11) valor = valor.slice(0, 11);

  if (valor.length > 9) {
    input.value = `${valor.slice(0, 3)}.${valor.slice(3, 6)}.${valor.slice(6, 9)}-${valor.slice(9, 11)}`;
  } else if (valor.length > 6) {
    input.value = `${valor.slice(0, 3)}.${valor.slice(3, 6)}.${valor.slice(6)}`;
  } else if (valor.length > 3) {
    input.value = `${valor.slice(0, 3)}.${valor.slice(3)}`;
  } else {
    input.value = valor;
  }
}
