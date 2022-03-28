#!/usr/bin/env python3.10.3
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from explainerdashboard import RegressionExplainer, ExplainerDashboard


# In[6]:


data_set = pd.read_excel("Data.xlsx")


# In[8]:


data_set = data_set.replace("M", "Male")
data_set = data_set.replace("M ", "Male")
data_set = data_set.replace("F", "Female")
data_set = data_set.replace("F ", "Female")


# In[9]:


data_set['SEX '].replace({'Female':1, 'Male':2}, inplace=True)


# In[10]:


data_set.rename(columns = {'AGE ' : 'Age', 'SEX ' : 'Gender', 'HBSAG +VE ' : 'HBsAg', 'HBEAG +VE ' : 'HBeAg',
                           'HBV DNA LOAD ' : 'HBV_DNA_Load'}, inplace = True)


# In[11]:


data_set['HBV_DNA_Load'] = np.log10(data_set['HBV_DNA_Load'])
data_set['HBeAg'] = np.log10(data_set['HBeAg'])
data_set['HBsAg'] = np.log10(data_set['HBsAg'])
data_set['Age'] = np.log10(data_set['Age'])
data_set['Gender'] = np.log10(data_set['Gender'])


# In[12]:


feature_descriptions = {
    
    "Gender": "Gender of passenger (0 = female & 0.3 = male)",
    "Age": "log10 of Age of the patients",
    "HBV_DNA_Load": "Log10 Hepatitis B Virus (HBV) DNA load in HBV infected population",
    "HBeAg": "Log10 Hepatitis B e Antigen (HBeAg) level in the population",
    "HBsAg": "Log10 Hepatitis B surface Antigen (HBsAg) level in the population", 
    
}


# In[13]:


y=pd.DataFrame(data_set,columns=['HBV_DNA_Load'])


# In[14]:


X=pd.DataFrame(data_set[['Age', 'Gender', 'HBsAg', 'HBeAg']])


# In[15]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
print(X_train.shape,y_train.shape,X_test.shape,y_test.shape)


# In[16]:


#Training the model
model = RandomForestRegressor(n_estimators=50, max_depth=5)
model.fit(X_train, y_train.values.ravel())


# In[19]:


explainer = RegressionExplainer(model, X_test, y_test, descriptions=feature_descriptions)
#Start the Dashboard
db = ExplainerDashboard(explainer,title='HBV DNA Load Prediction in hepatitis B infected clinical samples from Bihar, India.', descriptions=feature_descriptions, whatif=False, hide_poweredby=True, shap_interaction=False)

db.to_yaml("dashboard.yaml", explainerfile="explainer.joblib", dump_explainer=True)

db = ExplainerDashboard.from_config("dashboard.yaml")
app = db.flask_server()


# In[ ]:




