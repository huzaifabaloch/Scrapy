SCRAPY
======
Scrapy is a free and open-source web-crawling framework written in Python.
Originally designed for web scraping, it can also be used to extract data using APIs 
or as a general-purpose web crawler

HANDS ON SCRAPY PACKAGE
========================

1. creating virutal enviroment  (COMMAND PROMPT)
	* -> pip install pipenv (to install virtual environment if not installed on computer.)
	* go into any folder where you want to build an virtual enviroment.
	* then write -> virtualenv .
	* then activate it -> .\Scripts\activate
	* virtual enviroment is successfully activated.
	
	* Virtual Environment:
		it isolates your project from your operating system.
		means if you install scrapy or other package into that
		folder, it wont be installed and affect other files and 
		folder and operating system.

2. installing scrapy
	* if you write -> pip freeze
	* it will show you all the packages installed in that folder.
	* in that virtual env activated folfer
	* write -> pip install scrapy
	* it will install the scrapy and other scrapy related packages
	  in that folder.


3. start scrapy project
	* write -> scrapy startproject projectname
	* your first scrapy project will be created.
	* it will contain others files that are made automatically
	* by scrapy for your ease.

4. scrapy built-in files.
	* settings.py
		* all the settings related to scraping on internet.

	* items.py 
		* every data you select on a website such as name,
		author, tags, these are all fields and scrapy 
		wants us to add them in items file.

	* pipelines.py
		* when we want to store our data on a harddrive 
		maybe in csv, json, excel or Sqllite, databases
		then this file is responsible.

	* middlewares.py
		* for proxy related stuff, if a server dont allow
		scraping data. we use proxy there to bypass it.
		we send requests and can also handle the response back
		from server.

5. Selectors
	* Selectors are some if condition that go to a website, apply some conditions
	and extract data from it.
	TWO SELECTORS
	* CSS
	* XPATH	
	==========
	# EXAMPLES
	==========
	response.css('title::text').extract()
	response.css('span.text::text').extract()
	response.xpath('//title/text()').extract()
	response.xpath('//span[@class="text"]/text()').extract()
