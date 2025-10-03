<h1>#steps to run the file:</h1>

git commands:

git clone "https://github.com/anirudhkowluri/fake-news-detector.git"

cd "change the path to the destination file"

ls

git status

commands activate the virtual enivornment in terminal and load the streamlit website:
python -m venv .venv

# activate venv (PowerShell(Terminal))
.\.venv\Scripts\Activate.ps1

# (optional) if activation is blocked by execution policy, run:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass


# install from requirements.txt
python -m pip install -r .\requirements.txt

# verify installed packages (brief)
python -m pip list

# save installed versions
python -m pip freeze > installed-versions.txt

# run the website
streamlit run app.py
