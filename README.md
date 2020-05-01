# Password Manager
My first Python application.

Simple Python GUI application for Account and Secret management (Secrets unlike Account have only password without username or e-mail, examples are Wi-Fi password, PIN code, etc.).
UI is implemented using Tkiner package (with the help of [PAGE](http://page.sourceforge.net/) GUI generator). Python 3 is required, all other dependencies are listed in the requirements.txt.

Main application features are:

	- Access protection (registration and login, a master password defined during initial use aka registration is used to access the app content aka login)
	- Entry management (an entry can be by type Account, with username and/or e-mail and secret value like password, or Secret with just value/password)
	- Entry search (it allows searching by Type, Category and Name)
	- Category management (an entry must belong to one of defined categories, a category must be created before a desired entry)	
	- Default e-mail (a default e-mail address can be defined and used when creating an Account entry)
	- Change master password (access password can be changed after login)
	- Reset all (clears all data and requires new registration)
	- Encrypted entries saved within a file
