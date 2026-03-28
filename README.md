# Inventory System

A simple inventory management system built with Python.
It uses a menu, a while loop, a list of dictionaries, conditionals, and basic statistics.

---

## How to run

```
python inventory.py
```

---

## Menu options

| Option | Description |
|--------|-------------|
| 1 | Add a new product |
| 2 | Show all products |
| 3 | Calculate statistics |
| 4 | Exit |

---

## How the inventory works

Each product is stored as a dictionary inside a list:

```python
product = {"name": "Pencil", "price": 500, "quantity": 3}
inventory.append(product)
```

---

## Validations

- Price cannot be zero or negative
- Quantity cannot be zero or negative
- Invalid menu options show an error and go back to the menu

---

## Statistics

- **Total products registered** — sum of all quantities
- **Total inventory value** — sum of price x quantity for each product

---

## Requirements

- Python
- No external libraries needed 

## Flow chart

<img width="3008" height="4728" alt="image" src="https://github.com/user-attachments/assets/b72dc4f4-a2fe-499e-a881-af3d22264446" />
