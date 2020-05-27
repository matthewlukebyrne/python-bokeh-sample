from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues8
from bokeh.embed import components
import pandas

# A cmap is essentially a feature from Bokeh that does a color grade (from light to dark)
# Blues8 is simply a hex color of blue

# Two array lists with sample data (old data)
# x = [1,2,3,4,5]
# y = [4,6,2,4,3]

# Instead read from CSV file with cars.csv
# df = dataframe
df = pandas.read_csv('cars.csv')

# Create ColumnDataSource from Data Frame
source = ColumnDataSource(df)

# Output file to html!
output_file('index.html')

# Car List (Create a varible for the carlist)
car_list = source.data['Car'].tolist()

# Add plot to display on page
p = figure(
  y_range=car_list,
  plot_width=800,
  plot_height=600,
  title='Carz 2k20',
  x_axis_label='Horsepower',
  tools= 'pan,box_select,zoom_in,zoom_out,save,reset'
)

# Render glyph
p.hbar(
  y='Car',
  right='Horsepower',
  left=0,
  height=0.4,
  fill_alpha=0.9,
  fill_color=factor_cmap(
    'Car',
    palette=Blues8,
    factors=car_list
  ),
  source=source
)


# Add ToolTips
# Adds further info on hover when you go over bars in html
hover = HoverTool()
hover.tooltips = """
  <div>
    <h3>@Car</h3>
    <div><strong>Price:</strong> @Price</div>
    <div><strong>Horsepower:</strong> @Horsepower</div>
    <div><img src="@Image" alt="" width="200" /></div>
  </div>

"""

# Add tooltip to render
p.add_tools(hover)

# Show our results!
show(p)

# Print out div and script file tthat you can then insert into the DOM for JS if you need it!
# script, div = components(p)
# print(div)
# print(script)

# Extra docs for anything above
# https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/hbar.html
# https://pandas.pydata.org/ - csv data you can use in this file extension
# https://docs.bokeh.org/en/latest/index.html
