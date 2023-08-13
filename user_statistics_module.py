#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # importing the load_dataset_module module

# In[1]:


import load_dataset_module as m
s = m.transactions()
s


# In[ ]:





# In[2]:


s.keys()


# In[ ]:





# In[ ]:





# In[38]:


def get_max_min_transaction_amounts_for_user(trans_data, user):
    try:
        max_amount = float('-inf')  # Initialize max_amount to negative infinity
        min_amount = float('inf')   # Initialize min_amount to positive infinity
    
        for transaction_id in trans_data[user]:
            amount = trans_data[user][transaction_id]['Amount']
            max_amount = max(max_amount, amount)
            min_amount = min(min_amount, amount)
    
        return max_amount, min_amount
    
    except Exception as e:
        print(f"Error in get_max_min_transaction_amounts_for_user function: {e}")
    except:
        print("Some other exception happened.")


        
    


# In[4]:


def calculate_location_centroid(trans_data, user):
    try:
        total_x = 0
        total_y = 0
        total_transactions = 0

        for transaction_id in trans_data[user]:
            x_coord = trans_data[user][transaction_id]['x_coord']
            y_coord = trans_data[user][transaction_id]['y_coord']
            total_x += x_coord
            total_y += y_coord
            total_transactions += 1

        if total_transactions == 0:
            return None  # No transactions for the user
        
        centroid_x = round(total_x / total_transactions, 2)
        centroid_y = round(total_y / total_transactions, 2)
        
        return centroid_x, centroid_y
    
    except Exception as e:
        print(f"Error in calculate_location_centroid function: {e}")
    except:
        print("Some other exception happened.")


# In[ ]:





# In[39]:


import math

def calculate_distance_from_centroid(trans_data, user, transaction_id):
    try:
        total_x = 0
        total_y = 0
        total_transactions = 0

        for trans_id, trans_details in trans_data[user].items():
            x_coord = trans_details['x_coord']
            y_coord = trans_details['y_coord']
            total_x += x_coord
            total_y += y_coord
            total_transactions += 1

        if total_transactions == 0:
            return None  # No transactions for the user
        
        centroid_x = total_x / total_transactions
        centroid_y = total_y / total_transactions
        
        transaction_x = trans_data[user][transaction_id]['x_coord']
        transaction_y = trans_data[user][transaction_id]['y_coord']
        
        distance = math.sqrt((centroid_x - transaction_x)**2 + (centroid_y - transaction_y)**2)
        return distance
    
    except Exception as e:
        print(f"Error in calculate_distance_from_centroid function: {e}")
    except:
        print("Some other exception happened.")



# In[37]:


import math

def calculate_standard_deviation(trans_data, user):
    try:
        transaction_amounts = []
        
        for transaction_id in trans_data[user]:
            amount = trans_data[user][transaction_id]['Amount']
            transaction_amounts.append(amount)
        
        if not transaction_amounts:
            return None  # No transactions for the user
        
        mean = sum(transaction_amounts) / len(transaction_amounts)
        squared_diffs = [(amount - mean)**2 for amount in transaction_amounts]
        variance = sum(squared_diffs) / len(transaction_amounts)
        std_deviation = math.sqrt(variance)
        
        return std_deviation
    
    except Exception as e:
        print(f"Error calculate_standard_deviation function: {e}")
    except:
        print("Some other exception happened.")



# In[ ]:





# In[7]:


def calculate_variance(trans_data, user):
    try:
        transaction_amounts = []
        
        for transaction_id in trans_data[user]:
            amount = trans_data[user][transaction_id]['Amount']
            transaction_amounts.append(amount)
        
        if not transaction_amounts:
            return None  # No transactions for the user
        
        mean = sum(transaction_amounts) / len(transaction_amounts)
        squared_diffs = [(amount - mean)**2 for amount in transaction_amounts]
        variance = sum(squared_diffs) / len(transaction_amounts)
        
        return variance
    
    except Exception as e:
        print(f"Error in calculate_variance function: {e}")
    except:
        print("Some other exception happened.")




# In[ ]:





# In[ ]:





# In[41]:


def fraudulent_transaction(trans_data, user, transaction_id):
    try:
        if user in trans_data and transaction_id in trans_data[user]:
            transaction = trans_data[user][transaction_id]
            description = transaction['description']
            amount = float(transaction['Amount'])
            x_coord = float(transaction['x_coord'])
            y_coord = float(transaction['y_coord'])
            is_fraudulent = transaction['is_fraudulent']
            
            return {
                'transaction_id': transaction_id,
                'description': description,
                'amount': amount,
                'x_coord': x_coord,
                'y_coord': y_coord,
                'is_fraudulent': is_fraudulent
            }
        else:
            return None  # Transaction not found
        
    except KeyError:
        return None
    except ValueError:
        return None
    except Exception as e:
        print(f"Error in calculate_variance function: {e}")
    except:
        return None




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




