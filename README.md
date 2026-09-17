# AI-Assisted Box Selection System

## 1. Project Overview

The AI-Assisted Box Selection System is a Django-based web application that recommends a suitable shipping box for a product.

The system considers:

- Product dimensions
- Product weight
- Box dimensions
- Maximum box weight
- Box cost

The system checks the available boxes and recommends the lowest-cost box that can safely contain the selected product.

---

## 2. Objective

The main objective of this project is to help warehouse teams select a suitable shipping box for customer orders.

Instead of manually checking different box sizes, the system automatically checks the product requirements against the available boxes.

---

## 3. Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Django Admin

---

## 4. Project Features

- Add and manage products
- Add and manage shipping boxes
- Store product dimensions and weight
- Store box dimensions, maximum weight and cost
- Select a product from the web interface
- Automatically check suitable boxes
- Recommend the lowest-cost suitable box
- Show a message when no suitable box is available
- Django Admin interface for managing data

---

## 5. Box Selection Logic

The system follows these steps:

1. The user selects a product.
2. The system gets the product dimensions and weight.
3. Each available box is checked.
4. Product weight is compared with the box maximum weight.
5. Product and box dimensions are sorted to allow flexible orientation.
6. Each product dimension is compared with the corresponding box dimension.
7. Boxes that satisfy both weight and dimension requirements are considered suitable.
8. Suitable boxes are sorted according to cost.
9. The lowest-cost suitable box is recommended.
10. If no box satisfies the requirements, the system displays "No Suitable Box Available."

### Dimension Check

The dimensions are sorted before comparison. This allows the product to be considered in different orientations inside the box.

For example:

Product:

```text
35 × 25 × 5
```

Box:

```text
40 × 30 × 20
```

After sorting:

```text
Product: 5 × 25 × 35
Box:     20 × 30 × 40
```

Each product dimension is less than or equal to the corresponding box dimension, so the product fits.

---

## 6. Example Box Data

### Medium Box

```text
Length: 40 cm
Width: 30 cm
Height: 20 cm
Maximum Weight: 10 kg
Cost: ₹40
```

### Large Box

```text
Length: 60 cm
Width: 40 cm
Height: 40 cm
Maximum Weight: 20 kg
Cost: ₹70
```

---

## 7. Example Products

The project contains products such as:

- Book
- Laptop
- Shoes
- Keyboard
- Monitor
- Printer
- Small Speaker
- Large Item
- Heavy Item
- Small Box Item

---

## 8. Project Structure

```text
Box_Selection/
│
├── box_selection/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── boxes/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── product.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
├── AI_USAGE.md
└── TEST_OUTPUT.md
```

---

## 9. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-link>
```

### Step 2: Open the Project

```bash
cd Box_Selection
```

### Step 3: Create Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate Virtual Environment

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run Migrations

```bash
python manage.py migrate
```

### Step 7: Run the Server

```bash
python manage.py runserver
```

Open the application in a browser:

```text
http://127.0.0.1:8000/
```

---

## 10. Admin Panel

The Django Admin panel is used to manage products and boxes.

Admin URL:

```text
http://127.0.0.1:8000/admin/
```

Products and boxes can be added or updated from the admin panel.

---

## 11. Testing

The project uses Django's built-in testing framework.

Test command:

```bash
python manage.py test
```

Current automated test result:

```text
Found 3 test(s).
Ran 3 tests in 0.003s

OK
```

Detailed test cases and the actual test-run output are available in:

```text
TEST_OUTPUT.md
```

---

## 12. Limitations

- The current system works with individual products.
- It does not currently calculate combined dimensions and weight for multiple products in one order.
- Shipping or handling costs are not included.
- The current recommendation is based on available box dimensions, weight capacity and cost.

---

## 13. Future Improvements

Possible future improvements include:

- Support for multiple products in one order
- Better packing optimization
- More box sizes
- Product and box search
- Order management
- REST API integration
- Authentication and user roles
- Deployment to a cloud platform
- More automated test cases

---

## 14. Conclusion

The project demonstrates how Django can be used to build a simple box-selection system for warehouse operations.

It provides a web interface for selecting products and automatically recommends a suitable shipping box based on product dimensions, weight and box cost.
