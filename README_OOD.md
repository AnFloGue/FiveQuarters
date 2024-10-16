# Project Overview: Five Quarters

**Five Quarters** is a supplier back-end shop that manages the production of products for various front-end franchises. The system is designed to streamline the ordering and manufacturing process, ensuring that franchises can quickly and efficiently obtain the products they need.

## Key Features

### Home Page
- Displays "Products of the Week" which are pre-made and can be ordered immediately without any waiting time.

### Products Page  
- Franchise owners can order made-to-order products from this page. Each product is sorted into categories that align with existing ones and includes a detailed recipe showing the required ingredients and potential allergens.
  <br><br>
  - **Order Fulfillment Notification**: The system checks the stock and notifies the franchise owner about the availability of the order. If the stock is insufficient, it provides an estimated waiting time.
    <br><br>
  - **Inventory Management**: Upon order placement, the system alerts the inventory administrator to restock items if they are below the designated minimum level.
    <br><br>
  - **Product Information**: Access detailed recipes for each product, including all ingredients and potential allergens.
    <br><br>
  - **Reviews and Popularity Index**: Franchise owners can view all reviews and check the popularity index based on previous orders.

### Internal Inventory System
- Monitors overall stock levels and notifies the administration if there are insufficient ingredients to fulfill an order, ensuring the inventory is always up-to-date.

### User Feedback
- Franchises can rate products and leave comments to help improve product quality.

### User Management
- Provides web pages for user registration, login, and account management for different members who have access to the system. There are two tiers of user roles:
  <br><br>
  - **Inventory Management**: Users in this tier have the possibility of having up to all administrative permissions. They can manage inventory, reorder supplies, and perform other backend administrative actions.
  - **Franchise Owner**: Users in this tier can only place orders, cancel orders, and view pages. They do not have access to change inventory or reorder supplies, or perform any typical actions that only the inventory management backend users would do.

## API-First Approach

### Centralized Logic
- Ensures consistency in data access and modification.

### Security
- Uniform application of authentication and authorization.

### Scalability
- Easier to scale and maintain.

### Separation of Concerns
- Front-end and back-end can evolve independently.

### Easier Testing and Monitoring
- Simplifies testing, monitoring, and debugging.

### Consistency
- Ensures uniform data manipulation rules and validations.

## How It Works

### Ordering Process
- Franchise owners browse the Products Page to find and order products.
- Orders can be placed for both pre-made and made-to-order products.

### Order Fulfillment
- The system checks stock levels and notifies the franchise owner about order availability.
- If stock is insufficient, an estimated waiting time is provided.

### Inventory Management
- Upon order placement, the system alerts the inventory administrator to restock items if they are below the minimum level.
- The Internal Inventory System continuously monitors stock levels and ensures the inventory is up-to-date.

### Product Information and Feedback
- Detailed recipes and ingredient information are available for each product.
- Franchise owners can view reviews and popularity indices to make informed decisions.
- User feedback is collected to improve product quality.

### User Management
- The system provides functionalities for user registration, login, and account management.

## Project Structure

fivequarters/
├── accounts/
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── ...
├── api/
│   ├── init.py
│   ├── urls.py
│   ├── views.py
│   └── ...
├── frontshop/
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── ...
├── inventory/
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── ...
├── fivequarters/  # Assuming this is a subfolder
│   ├── init.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── manage.py
├── .env
├── requirements.txt
└── README.md
└── runtime.txt
└── .gitignore
└── Procfile