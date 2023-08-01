import pandas as pd

dataf = pd.read_csv("Squirrel_data.csv")
# fur_color_series = pd.Series(dataf["Primary Fur Color"])

# ngray = 0
# nblack = 0
# ncinnamon = 0

# for i in range(0, len(fur_color_series)):
#     local_color = fur_color_series[i]
#     if local_color == "Gray":
#         ngray += 1
#     if local_color == "Black":
#         nblack += 1
#     if local_color == "Cinnamon":
#         ncinnamon += 1
ngray = len(dataf[dataf["Primary Fur Color"]== "Gray"])
nblack = len(dataf[dataf["Primary Fur Color"]== "Black"])
ncinnamon = len(dataf[dataf["Primary Fur Color"]== "Cinnamon"])


final_table = {
    "Color" : ["gray", "Black", "Cinnamon"],
    "Count" : [ngray, nblack, ncinnamon],
}
dataf = pd.DataFrame(data=final_table)

dataf.to_csv("Final_count.csv")
