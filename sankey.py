import pandas as pd
import plotly.graph_objects as go

file_path = "sankey_assignment.csv"
data = pd.read_csv(file_path)

source_columns = ['PS', 'OMP', 'CNP', 'NRP', 'NMCCC', 'PEC', 'NCDM', 'RGS']
target_columns = ['Reg', 'Aca', 'Oth']

sankey_data = []

for label in data['LABEL']:
    for src in source_columns:
        value = data.loc[data['LABEL'] == label, src].values[0]
        if value > 0:  # only add non-zero connections
            sankey_data.append({"Source": src, "Target": label, "Value": value})

for label in data['LABEL']:
    for tgt in target_columns:
        value = data.loc[data['LABEL'] == label, tgt].values[0]
        if value > 0:  # only add non-zero connections
            sankey_data.append({"Source": label, "Target": tgt, "Value": value})

sankey_df = pd.DataFrame(sankey_data)

labels = list(pd.unique(sankey_df[['Source', 'Target']].values.ravel()))
label_map = {label: i for i, label in enumerate(labels)}

sankey_df['Source'] = sankey_df['Source'].map(label_map)
sankey_df['Target'] = sankey_df['Target'].map(label_map)

node_colors = [
    '#ffa07a',  # PS
    '#87cefa',  # S
    '#20b2aa',  # OMP
    '#ff8c00',  # CNP
    '#ff6ab4',  # NRP
    '#ffd701',  # NCDM
    '#ba55d3',  # RGS
    '#4782b4',  # F
    '#8fbc8f',  # NMCC
    '#5f9ea0',  # D
    '#6395ec',  # N
    '#02ced1',  # PEC
    '#00bfff',  # I
] + ['#3cb371', '#97fb98', '#90ee8f'] 

source_color_map = {
    'PS': '#ffa07a', 
    'OMP': '#20b2aa',
    'CNP': '#ff8c00',
    'NRP': '#ff6ab4', 
    'NMCCC': '#8fbc8f',
    'PEC': '#02ced1',
    'NCDM': '#ffd701', 
    'RGS': '#ba55d3',
    'S': '#87cefa',
    'I': '#00bfff',
    'D': '#5f9ea0',
    'F': '#4782b4',
    'N': '#6395ec'
}

link_colors = [
    source_color_map[labels[src]] for src in sankey_df['Source']
]

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=20,
        thickness=30,
        line=dict(color="black", width=0.5),
        label=labels,
        color=node_colors
    ),
    link=dict(
        source=sankey_df['Source'],
        target=sankey_df['Target'],
        value=sankey_df['Value'],
        color=link_colors
    )
)])

fig.update_layout(
    title_text="Sankey Diagram",
    font=dict(size=12, family="Arial"),
    title_font=dict(size=16, family="Arial", color="black"),
    plot_bgcolor='white'
)

fig.show()
