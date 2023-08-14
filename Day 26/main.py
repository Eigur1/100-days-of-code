import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dic = {nato_df.iloc[index]["letter"]:nato_df.iloc[index]["code"] for (index, row) in nato_df.iterrows()}

word = input("What do you wanna natoinize?")
output = [nato_dic[n.upper()] for n in list(word) if n != " "]
print(output)
#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

