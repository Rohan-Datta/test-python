from bokeh import plotting as plt
import functions_part1 as fp1


def plot_series(data,col):
    plot = plt.figure(
    width=800, height=600,
    x_axis_type="datetime",
    title='{} Closing Prices'.format(data['Symbol']),
    tools="pan,wheel_zoom,box_zoom,reset",
    toolbar_location="above",
    )
    mov_52 = fp1.get_moving_avg(data,col,52)
    grad = mov_52.diff()
    data['Grad'] = grad
    #color_mapper = LinearColorMapper(palette='Blues9',low=min(grad),high=max(grad))
    plot.line(x=data.index,y=data[col])
    
    return plot