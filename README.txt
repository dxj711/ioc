
1. Installation
    (i) Install the required libraries using the requirements.txt file:
        pip install -r requirements.txt

2. Running the Application
    (i) Run the main.py file by typing the following command in the terminal:
        streamlit run main.py
    (ii) The Streamlit application will open in your default web browser.

3. Using the Application
    (i) File Upload
        Add your input file from the local files section in the app.
    (ii) Generate Plots
        Navigate to the Generate Plots section.
        Select the desired plot type from the dropdown menu.
        Choose the columns to be used for the plot from the dropdown menu.
    (iii) Generate Predictions
        Navigate to the Generate Predictions section.
        Select the regression model from the dropdown menu.
        Choose the feature and target columns from the dropdown menus:
            You can select multiple feature columns.
            For the target column, ensure it is binary (contains exactly two unique values).

4. Future Code Updates
    (i) Adding New Plotting Methods
        Create a new file in the modules folder for the new plotting method.
        Import the file as a library in main.py under the #Visualizations section:
        from modules.file_name import returnFunction
    (ii) Adding New Prediction Methods
        Create a new file in the Regression folder for the new prediction method.
        Import the file as a library in main.py under #Regression section:
        from Regression.file_name import returnFunction

5. Accessing the Project Online
    You can access the project online at the following link: https://christioc.streamlit.app/