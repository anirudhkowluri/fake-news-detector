<h1>live web demo deployed streamlit app link - https://anirudhkowluri-fake-news-detector-app-nbshmv.streamlit.app/</h1>

<h1>#steps to run the file:</h1>

<p><u>git commands:</u></p>

git clone "https://github.com/anirudhkowluri/fake-news-detector.git"

cd "change the path to the destination file"

ls

git status

<h1>#commands activate the virtual enivornment in terminal and load the streamlit website:</h1>

<h2>#Create the virtual enivironment</h2>
python -m venv .venv

<h2>#Activate the virtual enivironment(venv) in PowerShell(Terminal)</h2>
.\.venv\Scripts\Activate.ps1

<h2>#(optional) if activation is blocked by execution policy, run:</h2>
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass


<h2>#Install  libraries from requirements.txt</h2>
python -m pip install -r .\requirements.txt

<h2>#Verify installed packages (brief)</h2>
python -m pip list

<h2>#Save installed versions</h2>
python -m pip freeze > installed-versions.txt

<h2>#Execute the code files</h2>
Execute the app.ipynb file first
Then execute the app.py file

<h2>#Command to run the website</h2>
streamlit run app.py

<h2>#app.ipynb jupiter notebook code summary</h2>

1. Importing Libraries

The notebook begins by importing all necessary libraries for:

Data manipulation: pandas, numpy

Text processing: re, nltk, string, PorterStemmer, stopwords

Feature extraction: TfidfVectorizer

Modeling & evaluation: train_test_split, LogisticRegression, accuracy_score, confusion_matrix, classification_report

Model saving: joblib

2. Loading the Datasets

Loads two CSV files:

Fake.csv — contains fake news articles

True.csv — contains real news articles

Both are read using pd.read_csv().

3. Data Preparation

Adds a new column class:

0 → Fake news

1 → Real news

Combines both datasets using pd.concat() to form a single dataset named data.

Removes unnecessary columns: title, subject, and date.

Resets and cleans up the DataFrame index.

4. Text Cleaning

Defines a function clean_text(text) that:

Converts text to lowercase

Removes:

Text in brackets ([...])

URLs

HTML tags

Punctuation

Newline characters

Words containing digits
Applies this function to the text column of the dataset.

5. Splitting the Data

Separates features (X = data['text']) and labels (y = data['class']).

Splits the dataset into training and testing sets using train_test_split() with 25% test data and a random seed of 42.

6. Text Vectorization

Initializes a TF-IDF Vectorizer to convert text into numerical form.

Fits and transforms the training data (xv_train).

Transforms the test data (xv_test).

7. Model Training

Initialize and train a Logistic Regression classifier 

8. Model Evaluation

Predicts the test data using the trained model.

Evaluates performance using:

Accuracy score

Classification report

Confusion matrix

These metrics provide insights into how well the model differentiates between fake and real news.

9. Saving the Model

Saves the trained TF-IDF vectorizer and model to disk using:

joblib.dump(vectorizer, 'vectorizer.jb')
joblib.dump(model, 'model.jb')


These saved files are later used in a Streamlit app for real-time predictions.

<h2>#app.py file code summary</h2>
<h3>Creating a  Streamlit app interface:</h3>

Import the necessary libraries

Loads a pre-trained text vectorizer and classification model(vectorizer.jb,model.jb files) created in app.ipynb jupiter notebook.

Lets users input a news article.

When the “Check News” button is clicked:

It vectorizes the text,

Predicts using the model,

Displays whether the news is Real or Fake.
