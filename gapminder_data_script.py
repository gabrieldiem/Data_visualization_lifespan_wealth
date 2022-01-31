import plotly.express

gapminder_dataframe = plotly.express.data.gapminder()

plotly.express.scatter(data_frame=gapminder_dataframe, x="gdpPercap", y="lifeExp", size="pop", color="continent", title="Life Span and Wealth", labels={"gdpPercap": "Wealth", "lifeExp": "Life Span"}, log_x=True, range_y=[25,95], hover_name="country", animation_frame="year", height=600, size_max=100).show()