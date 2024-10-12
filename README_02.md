## Architecture of the Five Quarters Project

The Five Quarters project is a supplier back-end system that manages the production and ordering of products for various front-end franchises. It's designed to make the entire process from ordering to manufacturing seamless for the franchises. The system is built on a multi-tiered architecture with separate areas for backend management and franchise owners. * **Versioning**, **authentication**, **authorization** are implemented.
<br><br>
### Application Structure

**The Five Quarters system comprises four main applications:**

*   **API app (api):
    *   This is the heart of the system, managing all data and business logic using a RESTful API approach, ensuring consistency and centralized logic.
    *   The API app employs function-based views, providing flexibility and customisation in handling requests.
    *   Security is ensured through token-based authentication (JWT), with appropriate authorization checks in place to safeguard sensitive data.
    *   Versioning is implemented using URLs (e.g. /api/v1/products) for backward compatibility.
    *   Documentation is done through Swagger to help developers understand the API's functionality.
    *   Caching is utilised to improve performance by storing frequently accessed data in memory.
    *   The API is designed to be scalable.
    *   Standard HTTP status codes are used for error handling, along with meaningful error messages.
    *   The API interacts with the frontshop and backshop apps to provide data and functionality.      <br>
       <br>
*   **Frontshop app (frontshop):
    *   This app acts as the user interface for franchise owners, enabling them to browse and order products. It interacts with the API app to retrieve and display data.
    *   It notifies Backshop when an order is placed, providing details of the order and any ingredients that need restocking.
    *   The `requests` library is used to make API calls.
    *   It includes separate modules for data creation, reading, updating and deletion through the API (`create_services.py`, `read_services.py`, `update_services.py` and `delete_services.py`).
    *   The `operations.py` module is responsible for any necessary calculations.     <br>
     <br>
*   **Backshop app (backshop):
    *   Responsible for inventory management through the API. It monitors stock levels and alerts administrators when ingredients are running low.
    *   It interacts with the API to retrieve and update inventory data.
    *   it is used to manage the overall stock levels and notify the inventory administrator when items need restocking.     <br>
        <br>
* **Account app (account):
    *   Handles user authentication, registration and profile management.
    *   Extends the default Django User model with additional details like user roles, phone numbers and addresses.
    *   Utilizes Django's built-in authentication system and authorization checks for security.
    *   Defines different user roles, such as 'inventory_manager' and 'franchise_owner', to control permissions and limiting  access to certain areas.
    *   Uses the Django admin interface for documentation. <br><br>
    
### **Data Flow**

The API app is the central hub for all data interactions. The frontshop, backshop and account apps communicate with the API to perform their respective functions. The `requests.get` method is used to retrieve data from API endpoints, ensuring decoupling between front-end and back-end, and enabling integration with external services. Caching is implemented to boost performance.
<br><br>
### **Key Features and Functionality**

**The system offers the following key features:**

*   **Two-tiered Access:**
    *   Backend Management: Full access to information, including stock levels, customer order details, ability to reorder supplies, and other administrative functions.
    *   Franchise Owners: Can view their account, browse available products, see order details and place new orders.        <br><br>
        
*   **Ordering Process:**
    *   Franchise owners can browse products and place orders for both pre-made and made-to-order items.
    *   The system checks stock and notifies the franchise owner about order availability, providing estimated waiting times if stock is insufficient.
    *   Upon order placement, the inventory administrator is alerted to restock any items below the minimum level.        <br><br>
        
*   **Inventory Management:**
    *   The backshop app, in conjunction with the API, monitors overall stock levels, notifies about insufficient ingredients to fulfil orders and keeps the inventory updated.         <br><br>
        
*   **Product Information and Feedback:**
    *   Detailed recipes and ingredient information are available for each product, including allergen information.
    *   Franchise owners can view reviews and popularity scores for each product.
    *   Franchise owners can provide feedback on products through ratings and comments.        <br><br>
        
*   **User Management:**
    *   The account app manages user registration, login and account management functionalities.
    *   Different user roles define permissions for different members accessing the system: Inventory Management users have administrative permissions, while Franchise Owners can only view information, place and cancel orders.

### **Suggested Improvements** <br><br>

*   Consolidate API Views: Enhance code organization and clarity by combining relevant functions from `api/v1/views.py` and `frontshop/services/read_services.py` into dedicated modules like `product_views.py`, `category_views.py` and `order_views.py`.        <br><br>
*   Enhance Authentication: to define permissions and poles Improve security by implementing token-based authentication using Django REST Framework's TokenAuthentication or JWTAuthentication.        <br><br>
    
* Explore Django's built-in permission system for managing user roles and permissions within the `account` app.     <br><br>
* Consider adding email verification for new accounts to ensure data integrity.

## Project Structure Analysis

**1. API-First Approach:**
* The project utilises an API-first approach where the API app drives all other apps, such as `frontshop`, `inventory`, and `account`. This promotes **scalability and separation of concerns**, allowing front-end and back-end components to evolve independently.  <br><br>
* The API app uses **function-based views**, offering flexibility and customisation in request handling.     <br><br>
* It adheres to **REST principles**, using standard HTTP methods and URLs for CRUD operations.        <br><br>
* The API is documented with Swagger, facilitating developer understanding.                  <br><br>
* **Versioning**, **authentication**, **authorization**, **rate limiting**, and **error handling**, are implemented.            <br><br>

**2. App Separation:**
* With this separation is aimed to enhances **code organisation, maintainability, and reusability**.  <br><br>
* The project is divided into distinct apps, each handling specific functionalities:     <br><br>
    * **`api`:** Manages the API logic and data serialization.
    * **`frontshop`:**  Handles user interaction with the website, including product browsing, ordering, reviews, and account management. 
    * **`backshop`:**  Manages inventory, stock and product details.
    * **`account`:**  Handles user authentication, registration, and profile management. <br><br>


**3. Model Design:**
* The models are based on the **business logic and their interactions of departemets** . <br><br>

* Each app has models representing the data structures:
    * **`backshop/models.py`:** Contains models for `Category`, `Product`, `Allergen`, `Ingredient`, and `Recipe`.
    * **`frontshop/models.py`:** Includes models for `DeliveryCompany`, `Order`, and `OrderItem`.
    * **`account/models.py`:** Defines the `UserProfile` model that extends the default Django `User` model.

**4. View Logic and Services:**

* The `frontshop` app utilises separate modules (`create_services.py`, `read_services.py`, `update_services.py`, `delete_services.py`) to interact with the API. This further promotes **modularity and code separation**.          <br><br>
* The `views.py` file in the `frontshop` app utilises these services to fetch data from the API and render templates.

**5. Caching:**

* Both the API and `frontshop` app use caching to improve performance by storing frequently accessed data in memory. This reduces the load on the database and speeds up data retrieval.

**6. Security Considerations:**

* The API implements token-based authentication (JWT) and authorization checks. However, the `frontshop` views do not explicitly handle user authentication. Implementing token-based authentication in the `frontshop` views as well would further enhance security and align it with the API's security measures.
  <br><br>
* from django.contrib.auth.decorators import login_required
* from .decorators import franchise_owner_required

* @login_required
* def home(request):
*    ... (View logic accessible to all logged-in users) ...


<br><br><br><br><br><br><br><br>

