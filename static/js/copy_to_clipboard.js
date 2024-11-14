// static/js/copy_to_clipboard.js

// Função para copiar texto para a área de transferência
function copyToClipboard(elementId) {
  var text = document.querySelector(elementId).textContent;
  navigator.clipboard.writeText(text).then(function() {
    alert("Texto copiado: " + text); // Opcional: você pode remover o alert e adicionar um feedback visual.
  }).catch(function(err) {
    alert("Erro ao copiar: " + err);
  });
}
