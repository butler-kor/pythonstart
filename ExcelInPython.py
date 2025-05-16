# 엑셀 불러오기
import pandas as pd
data = pd.read_excel('F:\exel97.xlsx')
print(data)
data['오늘'] = data['오늘']+10
new_eacel_file = 'F:\exel98.xlsx'
data.to_excel(new_eacel_file,index = False)
print(new_eacel_file)