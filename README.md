# Fraudulent Transaction Detection System
The Fraudulent Transaction Detection System is designed to detect fraudulent transactions in online financial systems. This system provides a user-friendly interface for analyzing user transaction data, calculating statistics, and detecting potentially fraudulent activities.

<img width="869" alt="Screenshot 2023-08-13 at 9 25 07 PM" src="https://github.com/Baci-Ak/Fraudulent-Transaction-Detection-System/assets/134199508/008f0524-b372-4287-be63-5d17bc6b5053">



## 📖 Case Study
Considering the enormous challenges posed by online transactions, you have been hired as a data scientist by a bank that issues credit cards. One of your job roles is to develop a system that uses purchasing transaction data of the bank customers to detect fraudulent behaviours very quickly, possibly in real- time in such a way that appropriate mechanisms for protecting the bank’s clients can be activated.
For this purpose, you are provided with datasets consisting of fraudulent and non-fraudulent purchasing transactions. Specifically, you should design and implement the system by analysing the problem of fraud detection systems, designing, and implementing a solution based on the concepts and principles python objects.

## 📦 Datasets
In the folder (transactions) of this repository, there are three datasets, namely: the transaction.txt, fraud- description.txt, and description.txt.
 The first dataset (description.txt) contains the description of genuine transactions. The second dataset (fraud-description.txt) contains the description of fraudulent transactions. The last dataset (transaction.txt) contains the actual transactions (10,000). The transaction dataset contains the description of the transactions, the amount of the transactions and the locations of the transactions. The locations are not real location to avoid tracing any transaction to anyone. The locations are just Euclidean coordinates in x, and y points. The following are the attributes of the transaction dataset:
1. The user id
2. The transaction id
3. The description of the transaction
4. The amount of the transaction
5. The x coordinate of each transaction
6. The y coordinate of each transaction
7. A Boolean label that represents whether the transaction is fraudulent or not.

<img width="325" alt="Screenshot 2023-08-13 at 8 42 05 PM" src="https://github.com/Baci-Ak/Fraudulent-Transaction-Detection-System/assets/134199508/fc246b9f-82f2-4efa-add4-4c92f311a9be">


## 💻Features
Load and organize transaction data from a file.
Calculate maximum and minimum transaction amounts for a user.
Compute the location centroid based on transaction coordinates.
Calculate the distance of a transaction from the user's centroid.
Determine standard deviation and variance of user transactions.
Detect fraudulent transactions and provide transaction details.


## 🚠Usage
* Upon running the program, a menu of options will be displayed.
* Choose an operation by entering the corresponding number.
* Input the required user and transaction IDs as prompted.
* View the results and details of each operation.


## 📙Modules and Functions
**`Load_Dataset_Module.py`:** Loads and organizes transaction data from a file.
   * transactions(): Reads transaction data and organizes it into a nested dictionary.

 **`fraud_detectionSystem_module.py`:** Provides functions for analyzing user transaction data and detect fradulent transaction.
 * get_max_min_transaction_amounts_for_user(trans_data, user): Calculates max and min transaction amounts.
 
 * calculate_location_centroid(trans_data, user): Computes user's transaction location centroid.
 
 * calculate_distance_from_centroid(trans_data, user, transaction_id): Calculates distance from centroid.
 
 * calculate_standard_deviation(trans_data, user): Computes standard deviation of transactions.
 
 * calculate_variance(trans_data, user): Calculates variance of transactions.
 
 * fraudulent_transaction(trans_data, user, transaction_id): Detects fraud and provides details.

**`Test_Module (Use_Interface)`:** Allows users to interact with the system.

**`Using_the_fraud_detection_system.ipynb` :** shows how to use the system


## 👩🏻‍💻Conclusion
The Fraudulent Transaction Detection System provides a powerful tool for detecting fraudulent transactions in online financial systems. Its modular design, user-friendly interface, and advanced functionalities make it an essential tool for maintaining the security of online transactions.

