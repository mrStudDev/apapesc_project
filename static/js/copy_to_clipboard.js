// Função para copiar texto para a área de transferência
function copyToClipboard(elementId) {
  // Seleciona o texto do elemento usando o ID
  var text = document.getElementById(elementId).textContent;

  // Usa a API de área de transferência para copiar o texto
  navigator.clipboard.writeText(text).then(function() {
    alert("Texto copiado: " + text); // Feedback opcional
  }).catch(function(err) {
    console.error("Erro ao copiar: ", err);
    alert("Erro ao copiar o texto."); // Alerta em caso de erro
  });
}
