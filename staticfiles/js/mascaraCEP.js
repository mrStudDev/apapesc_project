function mascaraCEP(input) {
  let valor = input.value.replace(/\D/g, ''); // Remove não-números
  if (valor.length > 8) valor = valor.slice(0, 8);

  if (valor.length > 5) {
    input.value = `${valor.slice(0, 5)}-${valor.slice(5)}`;
  } else {
    input.value = valor;
  }
}

