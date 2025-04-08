import pandas as pd
from sklearn.preprocessing import OneHotEncoder, RobustScaler
import numpy as np
from sklearn.preprocessing import StandardScaler

class Weather:
    
                    
   def get_data(self):
        data = 'weatherAUS.csv'
        self.df_Dataset = pd.read_csv(data)
        
        
        self.df_Dataset=self.df_Dataset.dropna(subset=['RainTomorrow'])
        
        self.df_Dataset['Date'] = pd.to_datetime(self.df_Dataset['Date'])
        
        self.df_Dataset['Year'] =  self.df_Dataset['Date'].dt.year
        self.df_Dataset['Month'] = self.df_Dataset['Date'].dt.month
        self.df_Dataset['Day'] = self.df_Dataset['Date'].dt.day
        self.df_Dataset.drop('Date', axis=1, inplace = True)       
                       
        self.change_to_hotEncoding()      
        self.change_numerical()  
        
     #    self.df_Dataset.drop(['RISK_MM'])
        return self.df_Dataset
   
   
   def get_data2(self):
      
      data = 'weatherAUS.csv'
      self.df_Dataset = pd.read_csv(data)
      self.df_Dataset = self.df_Dataset.loc[self.df_Dataset['RainTomorrow'].notna()]
      
      self.df_Dataset['Date'] = pd.to_datetime(self.df_Dataset['Date'])
        
      self.df_Dataset['Year'] =  self.df_Dataset['Date'].dt.year
      self.df_Dataset['Month'] = self.df_Dataset['Date'].dt.month
      self.df_Dataset['Day'] = self.df_Dataset['Date'].dt.day
      self.df_Dataset.drop('Date', axis=1, inplace = True)      
            
      return self.df_Dataset
   
   def change_to_hotEncoding(self):
    encoder = OneHotEncoder()
    categorical = [var for var in self.df_Dataset.columns if self.df_Dataset[var].dtype=='O' and var != 'RainTomorrow']
    encoded_data = encoder.fit_transform(self.df_Dataset[categorical])
    encoded_df = pd.DataFrame(encoded_data.toarray())
    encoded_df.columns = encoder.get_feature_names_out()
    self.df_Dataset = pd.concat([self.df_Dataset.drop(categorical, axis=1), encoded_df], axis=1)
    
    
   def change_numerical(self):
    numerical = [var for var in self.df_Dataset.columns if self.df_Dataset[var].dtype!='O']
    
    null_cols = [col for col in numerical if self.df_Dataset[col].isnull().any()]
    for col in null_cols:
     self.df_Dataset[col] = self.df_Dataset[col].fillna(self.df_Dataset[col].mean())
    
    
    
    self.df_Dataset[numerical] = self.df_Dataset[numerical].replace([np.inf, -np.inf], np.nan)
    self.df_Dataset[numerical] = self.df_Dataset[numerical].fillna(self.df_Dataset[numerical].mean())
    for var in numerical:
        self.df_Dataset[var] = np.log(self.df_Dataset[var]+ 1)
        self.df_Dataset[var] = self.df_Dataset[var].replace([np.inf, -np.inf], np.nan)  # Add this line
        self.df_Dataset[var] = self.df_Dataset[var].fillna(self.df_Dataset[var].mean())  # Add this line
        
    targetScaller=RobustScaler()        
        
    self.df_Dataset[numerical] = targetScaller.fit_transform(self.df_Dataset[numerical])