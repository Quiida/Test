#%%
import xarray as xr
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


x = np.linspace(0,1500,16)
y = np.random.random((1,1,1,1,1,6,len(x)))
y2 = np.random.random((1,1,1,1,1,6,len(x)))
y3 = np.random.random((1,1,1,1,1,6,len(x)))

da = xr.DataArray(y, dims=('Machine','Year','Month','Compensation','Axis','SensorNo','Pos'),
                    coords={'Machine':['MC_A'],'Year':['2020'],'Month':['Aug'],'Compensation':['Yes'],
                            'Axis':['X'],'SensorNo':range(6),'Pos':x},
                    name='var1')

da2 = xr.DataArray(y2, dims=('Machine','Year','Month','Compensation','Axis','SensorNo','Pos'),
                    coords={'Machine':['MC_B'],'Year':['2020'],'Month':['Aug'],'Compensation':['Yes'],
                            'Axis':['X'],'SensorNo':range(6),'Pos':x},
                    name='var1')

da3 = xr.DataArray(y3, dims=('Machine','Year','Month','Compensation','Axis','SensorNo','Pos'),
                    coords={'Machine':['MC_C'],'Year':['2020'],'Month':['Aug'],'Compensation':['Yes'],
                            'Axis':['X'],'SensorNo':range(6),'Pos':x},
                    name='var1')

da = xr.merge([da,da2,da3])
# print(da)
df = da.to_dataframe()

# df.reorder_levels(['Machine','Year','Month','Compensation','Axis','Errors','Pos'])
print(ds)
# foo=df.loc[df.index.get_level_values('Machine') == 'MC9A','var1']
yy=df.loc[('X','Yes','MC_A','Aug',x,0,'2020'),'var1']
# print(df.index.get_level_values('Pos').unique())

# #%%
fig = go.Figure()
fs=20
i=0
for index in df.index.unique(level='Machine'):
    fig.add_trace(
        go.Scatter(
            x = df.index.get_level_values('Pos').unique(),
            y = df.loc[('X','Yes',index,'Aug',x,0,'2020'),'var1'],
            name=index,
            line=dict(color=px.colors.qualitative.Plotly[i])
            )
        )
    i=i+1

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list(
            [dict(label = 'All',
                  method = 'update',
                  args = [{'visible': [True, True, True]},
                          {'title': 'All',
                           'showlegend':True}]),
             dict(label = 'MC_A',
                  method = 'update',
                  args = [{'visible': [True, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'MC_A',
                           'showlegend':True}]),
             dict(label = 'MC_B',
                  method = 'update',
                  args = [{'visible': [False, True, False]},
                          {'title': 'MC_B',
                           'showlegend':True}]),
             dict(label = 'MC_C',
                  method = 'update',
                  args = [{'visible': [False, False, True]},
                          {'title': 'MC_C',
                           'showlegend':True}]),
            ])
        )
    ])

fig.update_xaxes(title_text='Position [mm]',
                title_font_family="Arial",title_font_size=fs,
                tickfont=dict(family='Arial',size=fs),
                )
fig.update_yaxes(title_text='Deviation [um]',
                title_font_family="Arial",title_font_size=fs,
                tickfont=dict(family='Arial',size=fs),
                range=[-2,2])
fig.show()

# for index in df.index.unique(level='Machine'):
#     fig.add_trace(
#         go.Scatter(
#             x = df.index.get_level_values('Pos').unique(),
#             y = df.columns,
#             name = column
#         )
#     )
    
# fig.update_layout(
#     updatemenus=[go.layout.Updatemenu(
#         active=0,
#         buttons=list(
#             [dict(label = 'All',
#                   method = 'update',
#                   args = [{'visible': [True, True, True, True]},
#                           {'title': 'All',
#                            'showlegend':True}]),
#              dict(label = 'MSFT',
#                   method = 'update',
#                   args = [{'visible': [True, False, False, False]}, # the index of True aligns with the indices of plot traces
#                           {'title': 'MSFT',
#                            'showlegend':True}]),
#              dict(label = 'AAPL',
#                   method = 'update',
#                   args = [{'visible': [False, True, False, False]},
#                           {'title': 'AAPL',
#                            'showlegend':True}]),
#              dict(label = 'AMZN',
#                   method = 'update',
#                   args = [{'visible': [False, False, True, False]},
#                           {'title': 'AMZN',
#                            'showlegend':True}]),
#              dict(label = 'GOOGL',
#                   method = 'update',
#                   args = [{'visible': [False, False, False, True]},
#                           {'title': 'GOOGL',
#                            'showlegend':True}]),
#             ])
#         )
#     ])

# # fig.show()