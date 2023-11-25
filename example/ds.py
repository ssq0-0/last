import pandas
import pandas as pd

from AI import AI_model

df = pd.read_csv("/Users/ssq/Downloads/test_dataset_Тестовый датасет (1)/test.csv", sep = ';', encoding = 'utf-8')

print(df)


out = pd.DataFrame(columns=['id', 'Группа тем', 'Тема'])
for idx, row in df.iterrows():
    cat, theme = AI_model.exec(row['Текст инцидента'])
    out.loc[len(out)] = [row['id'], cat, theme]
# print(out)


out.to_csv('out.csv', sep = ';', index = False, encoding = 'utf-8')
