# daZ
Simple data analysis tool with some visualization option using streamlit


### Step 1 

Go to your project directory 
write  


    pipreqs  ./  

in command line which generates requrement.txt file 



### Step 2:

create a text file named 'setup.txt' file 
copy and paste the folwing code

    mkdir -p ~/.streamlit/
    
    echo "\
    [general]\n\
    email = \"your-email@domain.com\"\n\
    " > ~/.streamlit/credentials.toml
    
    echo "\
    [server]\n\
    headless = true\n\
    enableCORS=false\n\
    port = $PORT\n\
    " > ~/.streamlit/config.toml


then change the extention of the file from .txt to .sh to make it bash file. 


### Step 3 

Create a file ' Procfile.txt'
copy paste the folwing code

    web: sh setup.sh && streamlit run  filename.py


make sure in the end filename should be your script name.
 

### Step 4 initiating git repo



     git init



### step 5

Login to Heroku


    heroku login


### step 6

Create your desier host name by typing heroku create ''hostname'' 


    heroku create domainname



### step 7

Then type the following command 
Push the code to that instance using the following commands


    git add .
    git commit -m "some message"
    git push heroku master


For further information you can watch following [video](https://www.youtube.com/watch?v=nJHrSvYxzjE&list=PLuM-0SV1yHyoo9AKJI5a6JyGgu5V6ZXjj&index=8) . 
