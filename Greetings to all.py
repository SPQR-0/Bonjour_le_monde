# Install pycountry (if not already installed)
# pip install pycountry

from pycountry import countries

for country in countries:
  print(f"Hello {country.name}")
