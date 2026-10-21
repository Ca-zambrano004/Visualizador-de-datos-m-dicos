import medical_data_visualizer

print("Generando gráficos...")

fig_cat = medical_data_visualizer.draw_cat_plot()
fig_cat.savefig(r"C:\Users\WIN10\Desktop\CURSO PYTHON\3\catplot.png")

fig_heat = medical_data_visualizer.draw_heat_map()
fig_heat.savefig(r"C:\Users\WIN10\Desktop\CURSO PYTHON\3\heatmap.png")

print("Gráficos guardados en la carpeta actual.")
