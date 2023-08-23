#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[59]:


#Load Dataset Module
import string
def transactions1(data):  
    try:
        transaction_data = {}
        f = open(data, encoding ="ISO-8859-1")
        for line in f:
            #line = line.replace('"', '')
            user_id, transaction_id, description, amount, x_coord, y_coord, is_fraudulent = line.strip().split(':')
            
            if user_id not in transaction_data:
                transaction_data[user_id] = {}
            
            transaction_data[user_id][transaction_id] = {
                    'description': description,
                    'amount': float(amount),
                    'x_coord': float(x_coord),
                    'y_coord': float(y_coord),
                    'is_fraudulent': is_fraudulent}

        return transaction_data
    
    #handling exceptions:
    except FileNotFoundError:
        print('the file you are trying to read is not in this working directory OR cannot be found')
    except OSError as err:
        print("OS error: {0}".format(err))
    except NameError:
        print('there is a name in the class method that is not defined, please check to fix this')
    except:
        print("Some other exception happened.")


# In[ ]:





# In[64]:


#s = transactions1()
#s


# In[65]:


def transactions(data):  
    try:
        transaction_data = {}
        f = open(data, encoding ="ISO-8859-1")
        #next(f)
        for line in f:
            #line = line.replace('"', '')
            userId, transaction_id, description, amount, x_coord, y_coord, is_fraudulent = line.strip().split(':')
            transaction_data.setdefault(userId, {})
            transaction_data[userId][transaction_id] = {'description':description, 
                                                        'Amount': float(amount), 
                                                        'x_coord': float(x_coord), 
                                                        'y_coord': float(y_coord), 
                                                        'is_fraudulent':is_fraudulent}
        return transaction_data
    
           #handling exceptions:
    except FileNotFoundError:
        print('the file you are trying to read is not in this working directory OR cannot be found')
    except OSError as err:
        print("OS error: {0}".format(err))
    except NameError:
        print('there is a name in the class method that is not defined, please check to fix this')
    except:
        print("Some other exception happened.")


# In[66]:


#p = transactions(Transaction.txt)
#p


# In[ ]:




