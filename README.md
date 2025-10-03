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

<h2>#Command to run the website</h2>
streamlit run app.py
