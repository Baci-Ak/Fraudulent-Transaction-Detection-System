#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[7]:


import load_dataset_module as m
import user_statistics_module as s


# In[8]:


data = m.transactions()
data


# In[2]:


import user_statistics_module as s


# In[ ]:





# In[5]:


def Users_interface(transaction_data):
    
    while True:
        print("Welcome to the Fraud Detection System")
        print("1. Get maximum and minimum transaction amounts for a user")
        print("2. Calculate location centroid for a user")
        print("3. Calculate distance from centroid for a transaction")
        print("4. Calculate standard deviation of transactions for a user")
        print("5. Calculate variance of transactions for a user")
        print("6. Get transaction details")
        print("7. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            user = input("Enter user ID (available User IDs: {}): ".format(", ".join(transaction_data.keys())))
            try:
                max_amount, min_amount = s.get_max_min_transaction_amounts_for_user(transaction_data, user)
                print(f"\nThe Maximum transaction amount for user {user}  : {max_amount:.2f}")
                print(f"The Minimum transaction amount for user {user}  : {min_amount:.2f}")
            except TypeError:
                print(f"\nUser {user} not found.")
        
        elif choice == '2':
            user = input("\nEnter user ID (available User IDs: {}): ".format(", ".join(transaction_data.keys())))
            try:
                centroid = s.calculate_location_centroid(transaction_data, user)
                if centroid is not None:
                    print(f"\nLocation centroid for user {user}  : ")
                    print(f"{centroid}")
                else:
                    print(f"\nNo transactions for user {user} or wrong user ID.")
            except KeyError:
                print(f"\nUser {user} not found.")
        
        elif choice == '3':
            user = input("\nEnter user ID (available user IDs are : {}): ".format(", ".join(transaction_data.keys())))
            try:
                print("\nAvailable transaction IDs for user {} are :".format(user))
                print()
                print(", ".join(transaction_data[user].keys()))
                print()
                transaction_id = input("Enter transaction ID: ")
                #transaction_id = input("\nEnter transaction ID (available transaction IDs for user {} are : {}): ".format(user, ", ".join(transaction_data[user].keys())))
                try:
                    distance = s.calculate_distance_from_centroid(transaction_data, user, transaction_id)
                    if distance is not None:
                        print(f"\nThe Distance from centroid for transaction ID {transaction_id}: {distance:.2f}")
                    else:
                        print(f"Transaction ID {transaction_id} for user {user} not found.")
                except KeyError:
                    print(f"\nTransaction {transaction_id} for user {user} not found.")
            
            except KeyError:
                print(f"\nUser {user} not found.")
        
        
        elif choice == '4':
            user = input("Enter user ID (available user IDs: {}): ".format(", ".join(transaction_data.keys())))
            try:
                
                std_deviation = s.calculate_standard_deviation(transaction_data, user)
                if std_deviation is not None:
                    print(f"Standard deviation of transactions for user {user}: {std_deviation:.2f}")
                else:
                    print(f"No transactions for user {user}.")
                    
            except KeyError:
                print(f"User {user_id} not found.")
        
        elif choice == '5':
            user = input("Enter user ID (available user IDs: {}): ".format(", ".join(transaction_data.keys())))
            try:
                
                variance = s.calculate_variance(transaction_data, user)
                if variance is not None:
                    print(f"Variance of transactions for user {user}: {variance:.2f}")
                else:
                    print(f"No transactions for user {user}.")
                    
            except KeyError:
                print(f"User {user_id} not found.")
        
        elif choice == '6':
            user = input("\nEnter user ID (available user IDs: {}): ".format(", ".join(transaction_data.keys())))
            try:
                transaction_id = input("\nEnter transaction ID (available transaction IDs: {}): ".format(", ".join(transaction_data[user].keys())))
                try:
                    transaction_details = s.fraudulent_transaction(transaction_data, user, transaction_id)
                    if transaction_details is not None:
                        print(f"\nTransaction Details:")
                        print(f"Transaction ID: {transaction_details['transaction_id']}")
                        print(f"Description: {transaction_details['description']}")
                        print(f"Amount: {transaction_details['amount']:.2f}")
                        print(f"X Coordinate: {transaction_details['x_coord']:.2f}")
                        print(f"Y Coordinate: {transaction_details['y_coord']:.2f}")
                        print(f"Is Fraudulent: {transaction_details['is_fraudulent']}")
                    else:
                        print(f"Transaction ID {transaction_id} for user {user} not found.")
                        
                except KeyError:
                    print(f"Transaction {transaction_id} for user {user} not found.")
                    
            except KeyError:
                print(f"User {user} not found.")
        
        
        
        elif choice == '7':
            print("Exiting the Fraud Detection System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose again.")
            
        continue_choice = input("\nDo you want to perform another operation? (yes/no): ")
        if continue_choice.lower() != 'yes':
            print("\nExiting the Fraud Detection System. Goodbye!")
            break




# In[ ]:





# In[9]:


#Users_interface(data)


# In[ ]:





# In[ ]:




