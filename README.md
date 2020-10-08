# LifeLadderPacking
In the LifeLadderPacking app you can create LADDERS by telling amount, length and number of light units.  

When you have a list of ladders you can create a SHIPMENT which is a collection of packed pallets.   

The shipment packs the ladders on HALF PALLETS. These half pallets are then paired to WHOLE PALLETS. If it is an odd number of half pallets, of cource there will be a single half pallet besides all the whole pallets.  

In the result you can read the layout of the shipment, like where all the ladders go and data about each pallet like weight and height. 

# Run guide Windows 

NB. '>' indicates that we work in the terminal. You shall not write it your self. 

A – Install Python using the Microsoft Store:
(source: https://docs.microsoft.com/en-us/windows/python/beginners)

Go to your Start menu (lower left Windows icon), type "Microsoft Store", select the link to open the store.

Once the store is open, select Search from the upper-right menu and enter "Python". Open "Python 3.8" from the results under Apps. Select Get.

Once Python has completed the downloading and installation process, open Windows PowerShell using the Start menu (lower left Windows icon). Once PowerShell is open, enter Python --version to confirm that Python3 has installed on your machine.

The Microsoft Store installation of Python includes pip, the standard package manager. Pip allows you to install and manage additional packages that are not part of the Python standard library. To confirm that you also have pip available to install and manage packages, enter pip --version.

B - Open your terminal and go to folder 'LifeLadderPacking-UAT'

C – Run the below commands in your terminal

This installs an important package for LifeLadderPacking
>pip install binpacking

D - Run application

>py lifeladderApp.py 

if this does not work. Try opening Powershell in the same folder and run: 
>python lifeladderApp.py 