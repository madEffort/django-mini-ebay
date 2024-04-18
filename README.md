<h1 align="center">
  <br>
  <a href="https://github.com/madEffort/django-mini-ebay.git">
    <img src="https://github.com/madEffort/django-mini-ebay/assets/158125247/41edec39-5850-43c0-be73-d3095a400893" alt="MiniEbay" width="400">
  </a>
  <br>
</h1>

<h4 align="center">
</h4>

<p align="center">
<a href="https://github.com/madEffort/django-mini-ebay/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-blue"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-v3.10.5-yellow"></a>
<a href="https://github.com/madEffort/django-mini-ebay.git"><img src="https://img.shields.io/badge/PRs-welcome-green"></a>
<a href="https://www.paypal.me/madEffort"><img src="https://img.shields.io/badge/$-donate-ff69b4"></a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> • <a href="#how-to-use">How To Use</a> • <a href="#download">Download</a> • <a href="#credits">Credits</a> • <a href="#related">Related</a> • <a href="#support">Support</a> • <a href="#license">License</a>
</p>


## Key Features

**1. Product Registration and Management**
- **Registration:** Sellers can register new products using a form that captures product details.
- **Edit:** Sellers can edit existing product details through a form prefilled with existing data.
- **Deletion:** Products can be deleted directly if the seller chooses, with confirmation of deletion.

**2. Product Listings and Filtering**
- **Filter by Category:** Products can be sorted into their respective categories for easy browsing.
- **Pagination:** Manage the display of products effectively using pagination.
- **Seller-based Filtering:** Products associated with sellers allow filtering based on the seller's inventory.

**3. Shopping Cart and Checkout Process**
- **Add to Cart:** Users can place items in the shopping cart with specified quantities.
- **Update Cart:** Users can dynamically update the cart items, including increasing or decreasing the quantity or removing items.
- **Checkout:** The checkout process includes reviewing the cart, adjusting quantities, and confirming purchase details, leading to order creation.

**4. User Authentication and Management**
- **Signup and Login:** Includes user registration with login functionality post-signup automatically.
- **Account Deletion:** Users can delete their account if they choose to, with a confirmation process.
- **Profile Management:** Users can edit their profiles and change passwords using dedicated forms.

**5. Order Management**
- **View Orders:** Users can view a detailed list of their past orders.
- **Order Details:** Users can access detailed logs of individual orders, including product snapshots at the time of order.
- **Place Orders:** Users can finalize their purchases by transferring items from the cart to order, adjusting product stocks accordingly.

**6. Category-based Product Browsing**
- **Dynamic Selection:** Users can select categories from a dropdown to filter products displayed according to the chosen category.

**7. Sales Tracking**
- **Sales List:** Sellers can track sales of their listed products, viewing details of the orders that included their products.
- **Detailed View (Commented Out):** Ability to view detailed sales information based on individual product orders, though this feature is currently disabled in the code.


## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/madEffort/django-mini-ebay.git

# Go into the repository
$ cd django-mini-ebay

# Install dependencies
$ poetry install
```

After setting up the database and templates, please use the `makemigrations`, `migrate` and `collectstatic` commands.

```bash
# Run the app
$ python manage.py runserver
```

## Download



## Credits

This software uses the following open source packages:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)

## Related

- [Bootstrap](https://getbootstrap.com/)

## Support

<a href="https://www.paypal.com/paypalme/madEffort">
<img src="https://raw.githubusercontent.com/stefan-niedermann/paypal-donate-button/master/paypal-donate-button.png" alt="Donate with PayPal" width="200">
</a>


## License

This project adheres to the Apache-2.0 license, and you can find more detailed information in the [LICENSE](https://github.com/madEffort/django-mini-ebay/blob/main/LICENSE)

---

> GitHub [@madEffort](https://github.com/madEffort) &nbsp;&middot;&nbsp;
> Naver [@madEffort](https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjky&x_csa=%7B%22fromUi%22%3A%22kb%22%7D&pkid=1&os=32229226&qvt=0&query=%EA%B9%80%ED%98%84%EC%9A%B0)
