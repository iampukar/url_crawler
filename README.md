# Overview
-----------------------------------------------------------------------------

url_crawler is a Python library to crawl the details of a URL. 

## Usage

    from url_crawler import url_crawler
    '''
      url -> string URL to crawl for information.
    '''
    package_details = url_crawler(url)
    
    print(package_details.url)
    print(package_details.domain)
    print(package_details.check_https)
    print(package_details.dot_count)
    print(package_details.digit_count)
    print(package_details.url_length)
    
**Utilities**

| Name           | Output | Description  |
| ------------- | -----| -----|
| url | str | Returns the string url. |
| domain | str | Returns the domain of the url. |
| registrar | str | Returns the registrar for the given URL. |
| registered_country | str | Returns the registered domain country of the given URL. |
| whois | dict | Returns the whois information of the given URL. |
| registration_date | int | Returns the number of days since registration of the given URL. |
| expiry_date | int | Returns the number of days to expiration of the given URL. |
| intended_lifespan | int | Returns the number of days of intended lifespan of the given URL. |
| dot_count | int | Returns the dot(.) count in the given URL. |
| digit_count | int | Returns the digit count in the given URL. |
| url_length | int | Returns the length of the given URL. |
| fragments_count | int | Returns the fragment counts in the given URL. |
| entropy | int | Returns the entropy of the given URL. |
| check_http | bool | Checks for http headers in the given URL. |
| check_http | bool | Checks for https headers in the given URL. |
| url_response | bool | Checks for the URL response. |
| check_encoding | bool | Checks for encoding in in the given URL. |
| check_client | bool | Checks for client keyword in the given URL. |
| check_admin | bool | Checks for admin keyword in the given URL. |
| check_server | bool | Checks for server keyword in the given URL. |
| check_login | bool | Checks for login keyword in the given URL. |
| check_ports | bool | Checks for any ports in the given URL. |

## Requirements

The `requirements.txt` file has details of all Python libraries for this package, and can be installed using 
```
pip install -r requirements.txt
```

## Organization

    ├── src
    │   ├── url_crawler
              ├── init             <- init
              ├── url_crawler      <- package source code for URL crawler
    ├── setup.py             <- setup file 
    ├── LICENSE              <- LICENSE
    ├── README.md            <- README
    ├── CONTRIBUTING.md      <- contribution
    ├── test.py              <- test cases for unit testing
    ├── requirements.txt     <- requirements file for reproducing the code package

## License

MIT

## Contributions

For steps on code contribution, please see [CONTRIBUTING](./CONTRIBUTING.md).
