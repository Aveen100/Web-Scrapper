const axios = require('axios');
const cheerio = require('cheerio');
const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());

app.get('/api/products/:query', (req, res) => {
  const query = req.params.query;
  const url = `http://www.amazon.com/s?k=${query}`;

  axios
    .get(url)
    .then(response => {
      const $ = cheerio.load(response.data);
      const products = [];

      $('div[data-asin]').each((i, el) => {
        const product = {};
        product.id = $(el).attr('data-asin');
        product.title = $(el).find('span.a-text-normal').text();
        product.price = $(el).find('span.a-offscreen').text();
        products.push(product);
      });

      res.json(products);
    })
    .catch(error => {
      console.log("error");
      console.log(error);
      res.status(500).send('Error retrieving Amazon products.');
    });
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}.`);
});
