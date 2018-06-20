#README FIRST
##Car Parts Catalog

###Requirements
This catalog was developed and tested in Python 2.7. It **will not work** in Python 3.  
This README assumes you have somw knowledge in Python.  

####Ingredients:

* Python
* HTML
* CSS
* OAuth
* Flask Framework
* VirtualBox
* Vagrant
* Udacity Vagrant configuration


###Instructions
In order to use/execute the catalog you must first create and populate it's database.  
1. Run file `database_setup.py`  to create database structure  
```$ python database_setup.py```  
2. Run file `initialize___db.py` to insert some initial values in database  
`$ python initialize_db.py`  
3. After DB creation you may run file `project.py`  
`$ python project.py`
4. Open your browser and access [http://localhost:8000/] (http://localhost:8000/) to view the catalog.

####Google Login

In order to use the Google login you must take these steps:

Have a google login. If you do not have, [sign up](https://accounts.google.com/) for one or use Facebook login instead.  
1. Open [Google Developers Console](https://console.developers.google.com)  
2. Login to your google account.
3. Go to Credentials-> Create Crendentials > OAuth Client ID  
4. Select Web application and insert name 'Catalog-1'.  
4.1 Fill in:
"Authorized JavaScript origins" with http://localhost:8000
"Authorized redirect URIs" with http://localhost:8000/login',  'http://localhost:8000/gconnect' and 'http://localhost:8000/oauth2callback'
5. Click on Save/Create.   
6. Select "Download JSON".  
7. After you have downloaded, rename to "client_secrets.json" and put in the catalogP2 root directory.  
8. Open file "templates/login.html".  
9. Copy the Client ID and paste it into the field **data-clientid**
    
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