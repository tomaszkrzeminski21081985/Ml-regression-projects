import pandas as pd

class Statistics:

    def show_Statistics(self,df_Dataset):
        # print(df_Dataset.shape)
        # print("\n")
        # print(df_Dataset.info())
        # print("\n")
        # categorical = [var for var in df_Dataset.columns if df_Dataset[var].dtype=='O']

        # print('There are {} categorical variables\n'.format(len(categorical)))

        # print('The categorical variables are :', categorical)
        
        
        # print(df_Dataset[categorical].head())
        
        # for var in categorical:
        #  print(f"Categorical with missing values: {var} - {df_Dataset[var].isnull().sum()}")
           
        # # check for cardinality in categorical variables

        # for var in categorical:
            
        #     print(var, ' contains ', len(df_Dataset[var].unique()), ' labels')
        # print(df_Dataset.head())
        # print("\n")
        # print(df_Dataset.columns)
        # print("\n") 
        # print(df_Dataset.dtypes)
        # print(df_Dataset.shape)
       
    #    numerical = [var for var in df_Dataset.columns if df_Dataset[var].dtype!='O']

    #    print('There are {} numerical variables\n'.format(len(numerical)))

    #    print('The numerical variables are :', numerical)
       
    #    print(df_Dataset[numerical].head(10).to_string(index=False))
       
    #    print('Missing values in numerical types: ', df_Dataset[numerical].isnull().sum())
       
        print(df_Dataset.columns.isnull())
        
        
        columns=df_Dataset.columns
        
        for col in columns:
            print(col, ' contains ', df_Dataset.loc[ : ,col].isnull().sum(), ' missing values')