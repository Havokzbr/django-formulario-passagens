from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classes_viagem import tipos_de_classes
from passagens.validation import *
from passagens.models import Passagem, ClasseViagem, Pessoa


class PassagemForms(forms.ModelForm):
    """Formulário para passagem"""
    data_pesquisa = forms.DateField(label='Data da pesquisa:', disabled=True, initial=datetime.today())

    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {
            'data_pesquisa': 'Data da pesquisa:',
            'origem': 'Origem:',
            'destino': 'Destino:',
            'data_ida': 'Data de ida:',
            'data_volta': 'Data de volta:',
            'qtd_adultos': 'Quantidade de adultos:',
            'qtd_criancas': 'Quantidade de crianças:',
            'classes_viagem': 'Classe do Voo:',
            'informacoes': 'Informações:'
        }
        widgets = {
            'data_ida': DatePicker(
                options={
                    'minDate': datetime.now().strftime('%Y-%m-%d'),
                    'useCurrent': True,
                    'collapse': False,
                    'locale': 'pt-br',
                    'format': 'DD/MM/YYYY',
                }
            ),
            'data_volta': DatePicker(
                options={
                    'minDate': datetime.now().strftime('%Y-%m-%d'),
                    'useCurrent': True,
                    'collapse': False,
                    'locale': 'pt-br',
                    'format': 'DD/MM/YYYY',
                }
            ),
        }

    def clean(self):
        """Dados dos campos origem e destino, retornando uma lista de erros"""
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        lista_de_erros = {}

        """Dados dos campos de origem e destino se possui algum digito númerico"""
        campo_tem_algum_numero(origem, 'origem', lista_de_erros)
        campo_tem_algum_numero(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)

        """Dados dos campos data ida e volta"""
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_ida_maior_data_volta(data_ida, data_volta, lista_de_erros)

        """Dados dos campos data ida e data pesquisa"""
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        data_ida_menor_data_pesquisa(data_ida, data_pesquisa, lista_de_erros)

        """Lógica para verificar se há campos inválidos, retorna mensagem de erro"""
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_de_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_de_erro)
        return self.cleaned_data


class PessoaForms(forms.ModelForm):
    """Formulário para pessoa"""

    class Meta:
        model = Pessoa
        exclude = ['nome']  # Trazer todos campos, exceto campo marcado como exclude
