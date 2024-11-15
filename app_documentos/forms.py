from django import forms
from .models import Documento
from app_associados.models import AssociadoModel


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            'tipo_doc',
            'arquivo',
            'descricao',
            'nome',  # Incluído aqui
        ]
        widgets = {
            'tipo_doc': forms.Select(attrs={
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700',
                'onchange': 'exibirCampoNome(this.value)',
            }),
            'arquivo': forms.FileInput(attrs={
                'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-md cursor-pointer',
            }),
            'descricao': forms.Textarea(attrs={
                'placeholder': 'Descrição do documento / Anotação / Observação',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700',
                'rows': 4,
            }),
            'nome': forms.TextInput(attrs={
                'placeholder': 'Digite o nome do documento',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700',
                'style': 'display:none;',  # Oculta o campo `nome` inicialmente
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Label customizada para `tipo_doc`
        self.fields['tipo_doc'].label = "Tipo do Documento"