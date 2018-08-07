# gumpy
Python Gumtree API.

Currently performs a basic search and parses the response into item names and complete links to said items.

# Example usage

```Python
from gumtree import Search

laptops = Search(query="laptop", location="london")
print(laptops.items[0])
print(laptops.links[0])
```

The output would be something like:

```
Found 34 items.
HP Spectre x360 13-ae055na Convertible Laptop
http://www.gumtree.com/p/laptops/hp-spectre-x360-13-ae055na-convertible-laptop/1309218149
```

Parameters you can specify include:
* Category (category)
* Search Query (query)
* Location (location)
* Minimum price (min_price)
* Maximum price (max_price)
