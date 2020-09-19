#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[10]:


df = pd.read_csv("Training.csv")


# In[11]:


df.head()


# In[12]:


df.describe()


# In[6]:


X, y = df[['receiving_blood_transfusion', 'red_sore_around_nose',
       'abnormal_menstruation', 'continuous_sneezing', 'breathlessness',
       'blackheads', 'shivering', 'dizziness', 'back_pain', 'unsteadiness',
       'yellow_crust_ooze', 'muscle_weakness', 'loss_of_balance', 'chills',
       'ulcers_on_tongue', 'stomach_bleeding', 'lack_of_concentration', 'coma',
       'neck_pain', 'weakness_of_one_body_side', 'diarrhoea',
       'receiving_unsterile_injections', 'headache', 'family_history',
       'fast_heart_rate', 'pain_behind_the_eyes', 'sweating', 'mucoid_sputum',
       'spotting_ urination', 'sunken_eyes', 'dischromic _patches', 'nausea',
       'dehydration', 'loss_of_appetite', 'abdominal_pain', 'stomach_pain',
       'yellowish_skin', 'altered_sensorium', 'chest_pain', 'muscle_wasting',
       'vomiting', 'mild_fever', 'high_fever', 'red_spots_over_body',
       'dark_urine', 'itching', 'yellowing_of_eyes', 'fatigue', 'joint_pain',
       'muscle_pain']], df.iloc[:,-1]
X.head()


# In[13]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# In[14]:


from sklearn.svm import SVC
from sklearn import metrics
clf2=SVC(kernel="rbf")
clf2.fit(X_train,y_train)
y_pred=clf2.predict(X_test)


# In[15]:


from sklearn import metrics
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


# In[16]:


from sklearn.metrics import f1_score
f1_score(y_test, y_pred, average='weighted')


# In[17]:


from sklearn.metrics import jaccard_similarity_score
jaccard_similarity_score(y_test, y_pred)


# In[18]:


from sklearn.metrics import classification_report
classification_report(y_test, y_pred)


# In[19]:


#Create a Gaussian Classifier
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# In[20]:


from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
clf2=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf2.fit(X_train,y_train)

y_pred=clf2.predict(X_test)
y_pred


# In[21]:


feature_imp2 = pd.Series(clf2.feature_importances_,index=list(X.columns)).sort_values(ascending=False)
feature_imp2[::-1]


# In[22]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


fig = plt.gcf()
fig.set_size_inches(16, 12)

# Creating a bar plot
sns.set_style("whitegrid")
sns.barplot(x=feature_imp2, y=feature_imp2.index, palette='Blues_d',color='white')

# Add labels to your graph
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features")
plt.legend()
plt.show()


# In[ ]:





# In[23]:


X=X.to_numpy()
y=y.to_numpy()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# In[26]:


from sklearn.svm import SVC
from sklearn import metrics
clf3=SVC(kernel="rbf")

#Train the model using the training sets y_pred=clf.predict(X_test)
clf3.fit(X_train,y_train)
a=X[850].reshape(1,-1)
y_pred=clf3.predict(a)
print(y_pred)
print(y[850])


# In[ ]:




