# import pandas as pd
# import sqlite3

# df = pd.read_excel("/Users/hp/Desktop/migr.xlsx")
# print(df)
# connection = sqlite3.connect("/Users/hp/Desktop/people.db")
# df.to_sql(
#     name="people",
#     con=connection,
#     if_exists="replace",
#     index=False,
#     dtype={
#         'person_id':'real',
#         'fish':'real',
#         'birthday':'real',
#         'date_registr':'real'
#     }
# )

import sqlite3
import pandas as pd

con=sqlite3.connect('database.db')
wb=pd.ExcelFile('/Users/hp/Desktop/migr.xlsx')
for sheet in wb.sheet_names:
    df=pd.read_excel('/Users/hp/Desktop/migr.xlsx',sheet_name=sheet)
    df.to_sql(sheet,con, index=False,if_exists="replace")
con.commit()
con.close()