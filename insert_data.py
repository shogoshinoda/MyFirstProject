import os
import pandas as pd
import glob
from my_first_project.settings import BASE_DIR
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_first_project.settings")
from django import setup
setup()

from questions.models import Lectures, Questions


# レクチャーを追加
# id = 1
# files = [
#     '01_Low.csv', '02_Manage.csv', '03_Inter_Manage.csv', '04_Economy.csv',
#     '05_Industry_Economy.csv', '06_Inter_English.csv', '07_Human.csv',
#     '08_City_Info.csv', '09_Math.csv', '10_Info_Engineering.csv',
#     '11_Electri_Electro.csv', '12_Material.csv', '13_App_Chemistry.csv',
#     '14_Mecha_Engineering.csv', '15_Traffic_Mecha.csv', '16_Mechatronics.csv',
#     '17_Social_Infra.csv', '18_19_Env_Creation.csv', '18_19_Env_Creation.csv',
#     '20_Architecture.csv', '21_Biological_Resources.csv', '22_App_Organisms.csv',
#     '23_Bio_Env.csv', '24_Pharmacy.csv'
# ]
# for file in files:
#     lectures = pd.read_csv(f'{ BASE_DIR }/static/assets/csv/{ file }').values.tolist()
#     for lecture in lectures:
#         lect = Lectures(
#             lecture = lecture[2],
#             lecture_number = lecture[1],
#             lecture_teacher = lecture[3],
#             subject_id = id
#         )
#         lect.save()
#     id += 1

# 問題を追加
lecture_name = '都市計画'
files = glob.glob(f'static/assets/good_questions/建築学科/{ lecture_name }/*')
lecture_ids = [10356, 10344]
for lecture_id in lecture_ids:
    for file in files:
        file = file.replace(f'static/assets/good_questions/建築学科/{ lecture_name }/','')
        question = Questions(
            question = file,
            lecture_id = lecture_id
        )
        question.save()


'''
環境計画　10302
環境物理　10340
建築設備概論　10464, 10462
建築構造計画 10341, 10300
構造力学3 10356, 10344
都市計画 10463, 10461
'''