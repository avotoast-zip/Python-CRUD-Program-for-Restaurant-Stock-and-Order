# Python CRUD Application for Restaurant Stock and Order System

A comprehensive Python application for managing a simple restaurant stock and order data with Create, Read, Update, and Delete (CRUD) operations. The hypothetical restaurant is called "Uncle Tjong's Chinese Restaurant" and has an initial list of users, stock items, and menu. The predefined user roles have unique built-in abilities to modify this initial data.

## Business Understanding

This project caters to the food and beverage industry, specifically addressing the need to manage stock and kitchen data efficiently. This data plays a crucial role in keeping track of kitchen inventory and daily orders.

**Benefits:**

* Improved data accuracy and consistency
* Streamlined data management processes
* Enhanced decision-making through readily available data
* Improve coordination between different kitchen and inventory roles in a simple restaurant environment.

**Target Users:**

This application caters to three main user types:

**Master Admin:** Master Admin has an exclusive privilege to access and manage the app users.
**Stock Manager:** Stock Manager has an exclusive privilege to access and manage stock/inventory data.
**Kitchen Staff:** Kitchen Staff has an exclusive privilage to access menu and order data.

## Features

* **Create:**
    * Master Admin can create new users and define their user ID, role, name, and initial password, with user ID as the unique identifier.
    * Stock Manager can create new stock items and define their initial quantity, with item name as the unique identifier.
    * Kitchen Staff can create new orders and define their quantity, with an automated system checking on stock availability for the ingredients of each order item.
* **Read:**
    * Master Admin can retrieve all or any user data, but unable to access their password through this feature for privacy reasons.
    * Stock Manager can retrieve all stock data and see when each item was last updated.
    * Kitchen Staff can access the restaurant's menu and view order history.
* **Update:**
    * Master Admin can update user data (except for their ID and password), but they cannot change their own role.
    * Stock Manager can update stock data by adding or subtracting from the number of stock quantity. This includes checking on the stock availability for such actions to be performed.
    * Kitchen Staff has an indirect ability to update stock quantity data by placing orders. This action, upon checking for stock availability, will automatically reduce stock based on the order quantity and ingredient list.
    * All users can update their own password by first verifying their old one for authentication purposes.
* **Delete:**
    * Master Admin can delete any or all user data except for their own.
* **Security:**
    * The security features of this app includes user authentication, password privacy protection, and data validation.

## Installation

1. **Prerequisites:**
    * This app was built on Python version 3.9.11
    * There are no additional dependencies.

## Data Model
This project utilizes a Dictionary data structure, with a minor use of List for order history data.

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to cindyhtantowibowo@gmail.com or submit an issue if you encounter any problems or have suggestions for improvements.

