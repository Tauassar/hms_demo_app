/* eslint-disable no-param-reassign */
const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');

const app = express();

const PRODUCT_DATA_FILE = path.join(__dirname, 'data/server-product-data.json');
const CART_DATA_FILE = path.join(__dirname, 'data/server-cart-data.json');
const USER_DATA_FILE = path.join(__dirname, 'data/server-user-data.json');
const DEPARTMENT_DATA_FILE = path.join(__dirname, 'data/server-department-data.json');
const APPOINTMENT_DATA_FILE = path.join(__dirname, 'data/server-appointment-data.json');
const CARDIO_DEPT_DATA_FILE = path.join(__dirname, 'data/server-cardio-department.json');
const SURGERY_DEPT_DATA_FILE = path.join(__dirname, 'data/server-surgery-department.json');

app.set('port', (process.env.PORT || 3000));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use((req, res, next) => {
  res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate');
  res.setHeader('Pragma', 'no-cache');
  res.setHeader('Expires', '0');
  next();
});

// A fake API token our server validates
const API_TOKEN = 'D6W69PRgCoDKgHZGJmRUNA';

const extractToken = (req) => (
  req.query.token
);

const authenticatedRoute = ((req, res, next) => {
  const token = extractToken(req);

  if (token) {
    if (token === API_TOKEN) {
      return next();
    } else {
      return res.status(403).json({
        success: false,
        error: 'Invalid token provided',
      });
    }
  } else {
    return res.status(403).json({
      success: false,
      error: 'No token provided. Supply token as query param `token`',
    });
  }
});

// Make things more noticeable in the UI by introducing a fake delay
// to logins
const FAKE_DELAY = 500; // ms
app.post('/login', (req, res) => {
  setTimeout(() => {
    fs.readFile(USER_DATA_FILE, (err, raw_data) => {
      let data = JSON.parse(raw_data);
      let user = data.find(data=>data.username==req.body.username)
      if(user && user.password==req.body.password){
        const {password, ...user_data} = user;
        res.json({
          success: true,
          token: API_TOKEN,
          ...user_data
        });
        // res.json(JSON.parse(data));
      }else{
        res.json({
          success: false,
        });
      }
    }
    )
  }, FAKE_DELAY);
});

app.get('/appointments', authenticatedRoute, (req, res) => {
  fs.readFile(APPOINTMENT_DATA_FILE, (err, data) => {
    res.setHeader('Cache-Control', 'no-cache');
    res.json(JSON.parse(data));
  });
});

app.get('/department/cardio', authenticatedRoute, (req, res) => {
  fs.readFile(CARDIO_DEPT_DATA_FILE, (err, data) => {
    res.setHeader('Cache-Control', 'no-cache');
    res.json(JSON.parse(data));
  });
});

app.get('/department/surgery', authenticatedRoute, (req, res) => {
  fs.readFile(SURGERY_DEPT_DATA_FILE, (err, data) => {
    res.setHeader('Cache-Control', 'no-cache');
    res.json(JSON.parse(data));
  });
});

app.get('/departments', authenticatedRoute, (req, res) => {
  setTimeout(() => {
    fs.readFile(DEPARTMENT_DATA_FILE, (err, data) => {
      res.setHeader('Cache-Control', 'no-cache');
      res.json(JSON.parse(data));
    });
  }, FAKE_DELAY);
});

app.get('/cart', authenticatedRoute, (req, res) => {
  fs.readFile(CART_DATA_FILE, (err, data) => {
    res.setHeader('Cache-Control', 'no-cache');
    res.json(JSON.parse(data));
  });
});

app.post('/cart', (req, res) => {
  fs.readFile(CART_DATA_FILE, (err, data) => {
    const cartProducts = JSON.parse(data);
    const newCartProduct = { 
      id: req.body.id, 
      title: req.body.title, 
      description: req.body.description, 
      price: req.body.price, 
      image_tag: req.body.image_tag, 
      quantity: 1 
    };
    let cartProductExists = false;
    cartProducts.map((cartProduct) => {
      if (cartProduct.id === newCartProduct.id) {
        cartProduct.quantity++;
        cartProductExists = true;
      }
    });
    if (!cartProductExists) cartProducts.push(newCartProduct);
    fs.writeFile(CART_DATA_FILE, JSON.stringify(cartProducts, null, 4), () => {
      res.setHeader('Cache-Control', 'no-cache');
      res.json(cartProducts);
    });
  });
});

app.post('/cart/delete', (req, res) => {
  fs.readFile(CART_DATA_FILE, (err, data) => {
    let cartProducts = JSON.parse(data);
    cartProducts.map((cartProduct) => {
      if (cartProduct.id === req.body.id && cartProduct.quantity > 1) {
        cartProduct.quantity--;
      } else if (cartProduct.id === req.body.id && cartProduct.quantity === 1) {
        const cartIndexToRemove = cartProducts.findIndex(cartProduct => cartProduct.id === req.body.id);
        cartProducts.splice(cartIndexToRemove, 1);
      }
    });
    fs.writeFile(CART_DATA_FILE, JSON.stringify(cartProducts, null, 4), () => {
      res.setHeader('Cache-Control', 'no-cache');
      res.json(cartProducts);
    });
  });
});

app.post('/cart/delete/all', (req, res) => {
  fs.readFile(CART_DATA_FILE, () => {
    let emptyCart = [];
    fs.writeFile(CART_DATA_FILE, JSON.stringify(emptyCart, null, 4), () => {
      res.json(emptyCart);
    });
  });
});

app.listen(app.get('port'), () => {
  console.log(`Find the server at: http://localhost:${app.get('port')}/`); // eslint-disable-line no-console
});
