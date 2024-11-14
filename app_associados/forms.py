
from django.core.exceptions import ValidationError
from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import AssociadoModel, MunicipiosCircusnscricaoModel, ReparticaoModel

class AssociadoForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorWidget(attrs={
            'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500',
        }),
        required=False,
        label="Anotações"
    )
    class Meta:
        model = AssociadoModel
        fields = '__all__'
        widgets = {
            # Informações Pessoais
            'nome_completo': forms.TextInput(attrs={
                'placeholder': 'Digite o nome completo',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
            'cpf': forms.TextInput(attrs={
                'id': 'id_cpf',
                'placeholder': '000.000.000-00',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'oninput': 'mascaraCPF(this)',  # Chama a função de máscara para CPF
            }),
            'celular': forms.TextInput(attrs={
                'placeholder': '(48)99999-9999',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'oninput': 'mascaraTelefone(this)',  # Chama a função de máscara para celular
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'exemplo@email.com',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'foto': forms.FileInput(attrs={
                'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-md cursor-pointer focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'data_nascimento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }, format='%Y-%m-%d'),
            'sexo_biologico': forms.Select(attrs={
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'nome_mae': forms.TextInput(attrs={
                'placeholder': 'Nome da Mãe',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'nome_pai': forms.TextInput(attrs={
                'placeholder': 'Nome da Pai',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),

            # Documento RG
            'rg_numero': forms.TextInput(attrs={
                'placeholder': 'Digite somente números 0123456789',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'rg_orgao': forms.Select(attrs={
                'placeholder': 'SSP/UF',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'rg_data_emissao': forms.DateInput(attrs={
                'type': 'date',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }, format='%Y-%m-%d'),
            'naturalidade': forms.TextInput(attrs={
                'placeholder': 'Local de nascimento',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),

            # Documentos/Números Cidadão INSS/NIT/PIS/TITULO
            'nit': forms.TextInput(attrs={
                'placeholder': 'Digite somente números 0123456789',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'pis': forms.TextInput(attrs={
                'placeholder': 'Digite somente números 0123456789',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'titulo_eleitor': forms.TextInput(attrs={
                'placeholder': 'Digite somente números 0123456789',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            # Documentação Profissional
            'rgp': forms.TextInput(attrs={
                'placeholder': 'SCH00000000',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'rgp_data_emissao': forms.DateInput(attrs={
                'type': 'date',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }, format='%Y-%m-%d'),
            'primeiro_registro': forms.DateInput(attrs={
                'type': 'date',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }, format='%Y-%m-%d'),
            'rgp_mpa': forms.TextInput(attrs={
                'placeholder': 'EX: MPA',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            # Documentação de Trabalho
            'ctps': forms.TextInput(attrs={
                'placeholder': 'Digite somente números 0123456789',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'ctps_serie': forms.TextInput(attrs={
                'placeholder': '',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'ctps_data_emissao': forms.DateInput(attrs={
                'type': 'date',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }, format='%Y-%m-%d'),
            'ctps_uf': forms.Select(attrs={
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            # Documentação de Hanbilitação
            'cnh': forms.TextInput(attrs={
                'placeholder': 'Digite somente números 00000000',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'cnh_data_emissao': forms.DateInput(attrs={
                'type': 'date',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }, format='%Y-%m-%d'),
            # Endereço residencial
            'logradouro': forms.TextInput(attrs={
                'placeholder': 'Rua / Servidão / Avenida',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'bairro': forms.TextInput(attrs={
                'placeholder': 'Bévili-Rios / Vila Joana / Jardim das Flores',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'numero': forms.TextInput(attrs={
                'placeholder': '0123456789',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'complemento': forms.TextInput(attrs={
                'placeholder': 'Casa / Apto 71 / Quarto 10',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'cep': forms.TextInput(attrs={
                'placeholder': '00000-000',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'oninput': 'mascaraCEP(this)'  # Chama a função de máscara para CEP
            }),
            'municipio': forms.TextInput(attrs={
                'placeholder': 'Nome da cidade',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'uf': forms.Select(attrs={
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            # Acesso ao Governo
            'user_gov': forms.TextInput(attrs={
                'id': 'id_user_gov',
                'placeholder': 'CPF - automático',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'senha_gov': forms.TextInput(attrs={
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            # Dados da Filiação
            'municipio_circunscricao': forms.Select(attrs={
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'reparticao': forms.Select(attrs={
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),


            'data_cadastro': forms.DateInput(attrs={
                'type': 'date',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }, format='%Y-%m-%d'),
            'status': forms.Select(attrs={
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'data_atualizacao': forms.DateInput(attrs={
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }, format='%Y-%m-%d'),
        }



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pré-popula user_gov com cpf caso user_gov esteja vazio
        if self.instance and self.instance.cpf and not self.instance.user_gov:
            self.fields['user_gov'].initial = self.instance.cpf

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        # Remove tudo que não for número
        numeros = ''.join(c for c in cpf if c.isdigit())
        # Valida se o CPF tem exatamente 11 dígitos
        if len(numeros) != 11:
            raise ValidationError("CPF deve conter exatamente 11 dígitos.")
        return numeros

    def clean(self):
        cleaned_data = super().clean()
        cpf = cleaned_data.get("cpf")
        user_gov = cleaned_data.get("user_gov")
        # Caso senha_gov esteja vazio, preenchê-lo com o valor do CPF validado
        if cpf and not user_gov:
            cleaned_data["senha_gov"] = cpf
        return cleaned_data

    def clean(self):
        cleaned_data = super().clean()
        cpf = cleaned_data.get("cpf")
        user_gov = cleaned_data.get("user_gov")

        # Caso senha_gov esteja vazio, preenchê-lo com o valor do CPF validado
        if cpf and not user_gov:
            cleaned_data["user_gov"] = cpf

        return cleaned_data


    def clean_cep(self):
        cep = self.cleaned_data.get('cep')

        # Se o CEP não for preenchido, retorna None ou string vazia
        if not cep:
            return cep  # Retorna o valor original sem validar

        # Remove o hífen e valida se o valor tem apenas dígitos
        numeros = ''.join(c for c in cep if c.isdigit())

        if len(numeros) != 8:
            raise ValidationError("O CEP deve conter exatamente 8 dígitos.")

        return numeros  # Retorna apenas os números

    def clean_celular(self):
        celular = self.cleaned_data.get('celular')

        # Remove caracteres não numéricos da string, como parênteses, hífens e espaços
        numeros = ''.join(c for c in celular if c.isdigit())

        # Verifique se o número tem 10 ou 11 dígitos
        if len(numeros) < 10 or len(numeros) > 11:
            raise ValidationError("O celular deve conter 10 ou 11 dígitos.")

        # Se você desejar, pode formatar o celular de volta ao formato desejado:
        celular_formatado = f"({numeros[:2]}){numeros[2:7]}-{numeros[7:]}"

        return celular_formatado
# Retorna apenas os números


# forms.py
from django import forms

class AssociadoSearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        label="Buscar Associado",
        widget=forms.TextInput(attrs={
            'placeholder': 'Nome, CPF ou Celular',
            'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500',
        })
    )



class MunicipioForm(forms.ModelForm):
    class Meta:
        model = MunicipiosCircusnscricaoModel
        fields = '__all__'
        widgets = {
            'municipio': forms.TextInput(attrs={
                'placeholder': 'Digite o nome do município',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
        }

class ReparticaoForm(forms.ModelForm):
    novo_municipio_sede = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': '...',
            'placeholder': 'Digite o novo município',
        })
    )

    municipio_sede = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={
            'class': '...',
            'id': 'id_municipio_sede',
        })
    )

    class Meta:
        model = ReparticaoModel
        fields = [
            'nome_reparticao',
            'municipio_sede',
            'delegado_responsavel',
            'email_delegado',
            'celular_delegado',
            'municipios_circunscricao',
            'novo_municipio_sede',  # Inclua aqui o campo adicional
        ]
        widgets = {
            'nome_reparticao': forms.TextInput(attrs={
                'placeholder': 'Digite o nome da repartição',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700',
            }),
            'municipio_sede': forms.Select(attrs={
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700',
                'id': 'id_municipio_sede',
            }),

            'delegado_responsavel': forms.TextInput(attrs={
                'placeholder': 'Nome do delegado responsável',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
            'email_delegado': forms.EmailInput(attrs={
                'placeholder': 'exemplo@email.com',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'celular_delegado': forms.TextInput(attrs={
                'placeholder': '(48)99999-9999',
                'class': 'appearance-none border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'oninput': 'mascaraTelefone(this)',
            }),
            'municipios_circunscricao': forms.SelectMultiple(attrs={
                 'class': 'h-40 overflow-y-auto border border-gray-300 rounded-md w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        MUNICIPIO_OUTRO_ID = '-1'
        choices = list(MunicipiosCircusnscricaoModel.objects.order_by('municipio').values_list('id', 'municipio'))
        # Converter IDs para strings
        choices = [(str(id), nome) for id, nome in choices]
        # Adicionar a opção "Adicionar Novo Município sede" no topo da lista
        choices.insert(0, (MUNICIPIO_OUTRO_ID, 'Selecionar Município Existente'))
        self.fields['municipio_sede'].choices = choices

    def clean_municipio_sede(self):
        value = self.cleaned_data['municipio_sede']
        if value == '-1':
            return None  # Indica que o usuário quer adicionar um novo município
        else:
            try:
                municipio_sede = MunicipiosCircusnscricaoModel.objects.get(id=value)
                return municipio_sede
            except MunicipiosCircusnscricaoModel.DoesNotExist:
                raise forms.ValidationError('Faça uma escolha válida. Sua escolha não é uma das disponíveis.')

    def clean(self):
        cleaned_data = super().clean()
        municipio_sede = cleaned_data.get('municipio_sede')
        novo_municipio_sede = cleaned_data.get('novo_municipio_sede')

        if municipio_sede is None:
            # O usuário selecionou "Adicionar Novo Município sede"
            if not novo_municipio_sede:
                self.add_error('novo_municipio_sede', 'Por favor, informe o novo município.')
            else:
                # Cria ou obtém o novo município
                novo_municipio, created = MunicipiosCircusnscricaoModel.objects.get_or_create(
                    municipio=novo_municipio_sede)
                cleaned_data['municipio_sede'] = novo_municipio
        else:
            # O usuário selecionou um município existente
            cleaned_data['municipio_sede'] = municipio_sede

        return cleaned_data