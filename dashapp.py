from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

#--------------------------------------------------------#
#ASSIGN EXTERNAL STYLESHEET                              #
#--------------------------------------------------------#
external_stylesheets = [dbc.themes.BOOTSTRAP]

app = Dash(__name__, 
           suppress_callback_exceptions=True, 
           external_stylesheets=external_stylesheets)
#--------------------------------------------------------#


#--------------------------------------------------------#
#IMPORT DATA                                             #
#--------------------------------------------------------#
weights = pd.read_csv('weights.csv')
colors = (weights['MAE'] > 0.8)
#--------------------------------------------------------#


#--------------------------------------------------------#
#GRAPHS AND FIGURES                                      #
#--------------------------------------------------------#
fig = px.scatter(weights,
                 x="observation_time",
                 y="MAE",
                 title="Error Over Time",
                 color=colors)
fig.add_hline(y=0.8,
              line_color='green',
              line_dash='dash')
              
#--------------------------------------------------------#
#DEFINE HOMEPAGE LAYOUTS                                 #
#--------------------------------------------------------#
home_page = html.Div([dbc.Row([
                        dbc.Col(
                            html.Div([
                                        dcc.Link('Go to Page 1', href='/motivation'),
                                        html.Br(),
                                        dcc.Link('Go to Page 2', href='/motivation'),
                                        html.Br(),
                                        dcc.Link('Go to Page 3', href='/motivation')
                                    ]), 
                                    width=2),
                        dbc.Col(
                            html.Div([
                                        dcc.Graph(figure=fig),
                                        dcc.Slider(0,4,1,value=2,id='my-slider')
                                    ]), 
                                    width=10)
                        ])
                     ])
#--------------------------------------------------------#
#DEFINE OTHER PAGE LAYOUTS                               #
#--------------------------------------------------------#
motivation = html.Div([
                        html.H1('Motivation')
                     ])


bearing_dashboard = html.Div([
                                html.H1('Motivation')
                            ])

page_404_layout = html.Div([
    html.H1('404 Page Not Found'),
])




#--------------------------------------------------------#
#DEFINE APP LAYOUT                                       #
#--------------------------------------------------------#
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
#--------------------------------------------------------#


#--------------------------------------------------------#
#SITE MAP                                                #
#--------------------------------------------------------#
def display_page(pathname):
    if pathname == '/':
        return home_page
    if pathname == '/motivation':
        return motivation
    elif pathname == '/dashboard':
        return bearing_dashboard
    else:
        return page_404_layout
#--------------------------------------------------------#


#--------------------------------------------------------#
#RUN APP                                                 #
#--------------------------------------------------------#
if __name__ == '__main__':
    app.run_server(debug=True)
#--------------------------------------------------------#