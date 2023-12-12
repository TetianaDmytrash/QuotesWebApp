# Flask Quotes App
 A simple web application for viewing and saving quotes.

# Installation
 1. Clone the repository: git clone https://github.com/TetianaDmytrash/QuotesWebApp/tree/develop
 2. Install dependencies: pip install -r requirements.txt
 3. in file app/database/fillDatabase.py you need to configure your absolute path to the file app/database/quoteFile.txt (I know that it would be more correct to use a relative path, but I have not yet found how to implement it correctly)
 4. when you first launch the application, you should change the setting in the file app/database/isCreated.py to "False" so that the database is created (after launch, if you do not want to refill the database, the flag must be set to "True")
 5. Run the application: python run.py

# Key Features
 * Browse quotes by topic.
 * User registration.
 * Save your favorite quotes.
