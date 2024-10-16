# Five Quarters Project Documentation

## Home

Welcome to the Five Quarters Project documentation. This supplier back-end system manages the production and ordering of products for various front-end franchises. It's designed to make the entire process from ordering to manufacturing seamless for the franchises.

### Key Features:
- Two-tiered access system
- Comprehensive ordering process
- Efficient inventory management
- Detailed product information and feedback system
- User management with role-based permissions

## Architecture

The Five Quarters project is built on a multi-tiered architecture with separate areas for backend management and franchise owners. The system comprises four main applications:

1. **API app (api)**
2. **Frontshop app (frontshop)**
3. **Backshop app (backshop)**
4. **Account app (account)**

### API App (api)

The heart of the system, managing all data and business logic using a RESTful API approach.

- Employs function-based views
- Implements token-based authentication (JWT)
- Versioning through URLs (e.g., /api/v1/products)
- Documented using Swagger
- Utilizes caching for improved performance
- Designed for scalability
- Uses standard HTTP status codes for error handling

### Frontshop App (frontshop)

Acts as the user interface for franchise owners.

- Enables browsing and ordering of products
- Interacts with the API app for data retrieval and display
- Notifies Backshop when an order is placed
- Uses the `requests` library for API calls
- Includes separate modules for CRUD operations

### Backshop App (backshop)

Responsible for inventory management through the API.

- Monitors stock levels
- Alerts administrators when ingredients are running low
- Interacts with the API to retrieve and update inventory data

### Account App (account)

Handles user authentication, registration, and profile management.

- Extends the default Django User model
- Utilizes Django's built-in authentication system
- Defines different user roles (e.g., 'inventory_manager', 'franchise_owner')
- Uses Django admin interface for documentation

## Data Flow

The API app serves as the central hub for all data interactions. The frontshop, backshop, and account apps communicate with the API to perform their respective functions. 

- `requests.get` method is used to retrieve data from API endpoints
- Caching is implemented to boost performance

## Key Features and Functionality

### Two-tiered Access

1. **Backend Management**
   - Full access to information
   - Ability to reorder supplies
   - Administrative functions

2. **Franchise Owners**
   - View account details
   - Browse available products
   - See order details
   - Place new orders

### Ordering Process

- Browse products and place orders
- System checks stock and notifies about availability
- Provides estimated waiting times if stock is insufficient
- Alerts inventory administrator for restocking

### Inventory Management

- Monitors overall stock levels
- Notifies about insufficient ingredients
- Keeps inventory updated

### Product Information and Feedback

- Detailed recipes and ingredient information available
- Allergen information provided
- Franchise owners can view reviews and popularity scores
- Feedback system through ratings and comments

### User Management

- User registration, login, and account management
- Role-based permissions (Inventory Management users vs. Franchise Owners)

## Project Structure Analysis

### API-First Approach

- Promotes scalability and separation of concerns
- Uses function-based views for flexibility
- Adheres to REST principles
- Documented with Swagger
- Implements versioning, authentication, authorization, rate limiting, and error handling

### App Separation

Enhances code organization, maintainability, and reusability:

- **api**: Manages API logic and data serialization
- **frontshop**: Handles user interaction with the website
- **backshop**: Manages inventory, stock, and product details
- **account**: Handles user authentication, registration, and profile management

## Model Design

Models are based on business logic and department interactions:

### Backshop Models
- Category
- Product
- Allergen
- Ingredient
- Recipe

### Frontshop Models
- DeliveryCompany
- Basket
- BasketItem
- Order
- OrderItem

### Account Models
- UserProfile (extends Django User model)

## Security Considerations

- Token-based authentication (JWT)
- Authorization checks
- `@login_required` decorator used in sensitive views
- Role-based access restrictions
- CSRF Protection in forms
