import numpy as np
import pandas as pd

class NJCleaner():
    def __init__(self, csv_path:str)-> None:
        self.data =  pd.read_csv(csv_path)

    def order_by_scheduled_time(self):
        sorteddata = self.data.sort_values(by=['scheduled_time'])
        return sorteddata
        
    
    def drop_columns_and_nan(self):
        self.data.drop(columns=['from', 'to'])
        self.data.dropna()

    def convert_date_to_day(self):
        date = self.data['date'].to_list()
        date = pd.Timestamp(self.data['date']).day_name()
        self.data['day'] = date
        self.data.drop(columns=['date'])

    #def convert_scheduled_time_to_part_of_the_day(self):
        #for row in self.data.rows:
            #if self.data['scheduled_time']