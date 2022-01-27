import os
import pandas as pd
from my_first_project.settings import BASE_DIR
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_first_project.settings")
from django import setup
setup()

from questions.models import Lectures



id = 1
files = [
    '01_Low.csv', '02_Manage.csv', '03_Inter_Manage.csv', '04_Economy.csv',
    '05_Industry_Economy.csv', '06_Inter_English.csv', '07_Human.csv',
    '08_City_Info.csv', '09_Math.csv', '10_Info_Engineering.csv',
    '11_Electri_Electro.csv', '12_Material.csv', '13_App_Chemistry.csv',
    '14_Mecha_Engineering.csv', '15_Traffic_Mecha.csv', '16_Mechatronics.csv',
    '17_Social_Infra.csv', '18_19_Env_Creation.csv', '18_19_Env_Creation.csv',
    '20_Architecture.csv', '21_Biological_Resources.csv', '22_App_Organisms.csv',
    '23_Bio_Env.csv', '24_Pharmacy.csv'
]
for file in files:
    lectures = pd.read_csv(f'{ BASE_DIR }/static/assets/csv/{ file }').values.tolist()
    for lecture in lectures:
        lect = Lectures(
            lecture = lecture[2],
            lecture_number = lecture[1],
            lecture_teacher = lecture[3],
            subject_id = id
        )
        lect.save()
    id += 1





