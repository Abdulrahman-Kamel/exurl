# exurl package - The split urls to many urls approval on patameters!

With exurl, you can split one url or multiple urls to many approval on patameters count , change parameter value in url to you want but change one by one and return all in list.

# Overview
The exurl python package was written with fast use in mind. It provides the following key features at present <br>
  - take url and change parameters value to you want, one by one <br>
  - take urls list and change parameters value to you want, again one by one <br>
  - all results will returned in list <br>


## why exurl !
when you programming web testing tools should interested GET requests and this requests contains on [parameters] and you want to testing this parameters one by one in the right way
example..
now you programming xss testing tool , will send payload in all parameters and then make match on this payload in response body was it filtered or not ?
in normal will send :- 
https://www.example.com/search.php?q=<payload>&countPage=<payload>&art=<payload>
but this is very bad , you should send as follows..
https://www.example.com/search.php?q=<payload>&countPage=7&art=1
https://www.example.com/search.php?q=someSearch&countPage=<payload>&art=1
https://www.example.com/search.php?q=someSearch&countPage=7&art=<payload>
and then make match on every request
exurl will take url or urls list and will split all parameters inside url alike above example

## Usage

In the following paragraphs, I am going to describe how you can get and use exurl for your own projects.

###  Getting it

To download exurl, either fork this github repo or simply use Pypi via pip.
```sh
$ pip3 install exurl
```

## Using it

### Example on one url
### NOTIC: you can use split_url on one url and split_urls on urls list

```python
import exurl
exampleURL = https://www.example.com/search.php?q=someSearch&countPage=7&art=1
fuzz_example = exurl.split_url(exampleURL, 'FUZZ07')
print(fuzz)
```
The output will be..
```python3
https://www.example.com/search.php?q=FUZZ07&countPage=7&art=1
https://www.example.com/search.php?q=someSearch&countPage=FUZZ07&art=1
https://www.example.com/search.php?q=someSearch&countPage=7&art=FUZZ07
```
### Example on one url
```python3
import exurl
with open('urls.txt') as f:
	urls_list = f.read().splitlines()
splitting_urls = exurl.split_urls(urls_list, 'payload')
```
will found all urls splitting in splitting_urls variable






License
----

MIT License

Copyright (c) 2021 abdulrahman kamel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
