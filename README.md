#README FIRST
##Car Parts Catalog

###Requirements
This catalog was developed and tested in Python 2.7. It **will not work** in Python 3.

###Instructions
In order to use/execute the catalog you must first create and populate it's database.  
1. Run file `database_setup.py`  to create database structure  
```$ python database_setup.py```  
2. Run file `initialize___db.py` to insert some initial values in database  
`$ python initialize_db.py`  
3. After DB creation you may run file `project.py`  
`$ python project.py`
4. Open your browser and access [http://localhost:8000/] (http://localhost:8000/) to view the catalog.
###JSON Links  
The RESTful Web Services implemented are listed below.  
List all:  

* Categories:   
http://localhost:8000/categories/JSON  
* Products:   
http://localhost:8000/products/JSON   
* One category  
http://localhost:8000/category/X/JSON
* One Product in specific category 
http://localhost:8000/products/X/X/JSON

**Note:** "X" must be replaced with id from category and/or product.   
 
###Basic navigation
On the left of screen, all categories are listed by default. Click in one category to list all products inside.  
Click "Categories" to list categories and, if you are logged in, to add a new category.

On top right of catalog you have:  
**Home** - Return to main page.  
**About** - Catalog/Store information.  
**Login** - Use Google or Facebook to login and add/edit information.

**Note:** You may only edit/delete products you have created.

###References
* [Bootstrap Theme](https://startbootstrap.com/template-overviews/shop-homepage)
* [Image 1](http://www.speedautocars.com/how-to-choose-the-right-auto-parts-supplier-online/)
* [Image 2](http://www.eastendtransmissionsny.com/transmission-repair-and-rebuilding)
* [Image 3](http://www.speedautocars.com/electronic-injection-inside-the-engine-temperature-sensor/)
* [Banner Image](http://hondamotors.sr/en/parts/damage-report/)