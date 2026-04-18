import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file = pd.read_excel('C:/Data_/excel/data_jobs_salary_all.xlsx',sheet_name='maaz_1')
file['job_posted_month']=pd.to_datetime(file['job_posted_date']).dt.strftime('%b')


print(file.info())
                   
