import pandas as pd
import plotly.express as px

# Đọc dữ liệu
df = pd.read_csv('C:/Users/Admin/Desktop/VGU/Math/phase 4/education_career_success.csv')

# Tính tổng SAT theo ngành học
sat_by_field = df.groupby('Field_of_Study')['SAT_Score'].sum().reset_index()
sat_by_field['Proportion'] = sat_by_field['SAT_Score'] / sat_by_field['SAT_Score'].sum()

# Tạo biểu đồ sunburst
fig = px.sunburst(
    sat_by_field,
    path=['Field_of_Study'],
    values='Proportion',
    title='Proportion of SAT Score by Field of Study',
    color='Proportion',
    color_continuous_scale='Blues'
)

fig.show()
