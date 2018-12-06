import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input
import numpy as np
from scipy.optimize import linprog
from numpy.linalg import solve

if __name__ == '__main__':

    listaCusto = []
    listaResultado = []
    listaRestricao = []
    tabelaRestricoes = []
    vetorCusto = np.array([])
    vetorResultado = np.array([])
    vetorRestricoes = np.array([])

    app = dash.Dash()

    app.layout = html.Div([
        dcc.Input(id='custo', value='Initial Value', type='text'),
        html.Button(id='add-custo-button', type='submit', children='Add Custo'),
        html.Div(id='custo_div'),
        dcc.Input(id='resultado', value='Initial Value', type='text'),
        html.Button(id='add-resultado-button', type='submit', children='Add Resultado'),
        html.Div(id='resultado_div'),
        dcc.Input(id='restricao', value='Initial Value', type='text'),
        html.Button(id='add-restricao-button', type='submit', children='Add Restricao'),
        html.Div(id='restricao_div'),
        html.Button(id='add-linhaRestricao-button', type='submit', children='Add Linha Restricao'),
        html.Div(id='linhaRestricao_div'),
        html.Button(id='calcular-button', type='submit', children='Calcular'),
        html.Div(id='calcular_div')
    ])


    @app.callback(Output('calcular_div', 'children'),
            [Input('calcular-button', 'n_clicks')],
        )
    def calcular(clicks):
        if clicks is not None:
            try:
                matrizRestricoes = np.array(tabelaRestricoes)
                vetorResultado = np.array(listaResultado)
                vetorCusto = np.array(listaCusto)
                res = linprog(vetorCusto, A_eq=matrizRestricoes, b_eq=vetorResultado, bounds=(0, None))
                return 'Optimal value:' + str(res.fun) + '\nX:' + str(res.x)
            except ValueError:
                return 'O texto não pode ficar em branco'


# --> Restrições

    @app.callback(Output('restricao_div', 'children'),
            [Input('add-restricao-button', 'n_clicks')],
            [State('restricao', 'value')],
        )
    def update_restricao(clicks, restricao):
        if clicks is not None and restricao is not '':
            try:
                restricao = int(restricao)
                listaRestricao.append(restricao)
                return 'Restrição ' + str(listaRestricao)
            except ValueError:
                return 'O texto não pode ficar em branco'


    @app.callback(Output('linhaRestricao_div', 'children'),
            [Input('add-linhaRestricao-button', 'n_clicks')],
        )
    def update_linhaRestricao(clicks):
        if clicks is not None: 
            try:
                print(tabelaRestricoes)
                tabelaRestricoes.append(listaRestricao.copy())
                listaRestricao.clear()
                return 'Tabela de restrições ' + str(tabelaRestricoes)
            except ValueError:
                return 'O texto não pode ficar em branco'

# --> Custo

    @app.callback(Output('custo_div', 'children'),
            [Input('add-custo-button', 'n_clicks')],
            [State('custo', 'value')],
        )
    def update_custo(clicks, custo):
        if clicks is not None and custo is not '':
            try:
                custo = int(custo)
                listaCusto.append(custo)
                return 'Custo ' + str(listaCusto)
            except ValueError:
                return 'O texto não pode ficar em branco'

# --> Resultado 
    @app.callback(Output('resultado_div', 'children'),
            [Input('add-resultado-button', 'n_clicks')],
            [State('resultado', 'value')],
        )
    def update_resultado(clicks, resultado):
        if clicks is not None and resultado is not '':
            try:
                resultado = int(resultado)
                listaResultado.append(resultado)
                return 'Resultado ' + str(listaResultado)
            except ValueError:
                return 'O texto não pode ficar em branco'

    app.run_server(host='0.0.0.0')