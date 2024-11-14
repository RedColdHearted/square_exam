# Quick start

### On windows
```bash
git clone https://github.com/RedColdHearted/square_exam.git
cd square_exam
.venv/Scripts/Activate.ps1
pip install -r requirements.txt
```

### On linux
```bash
git clone https://github.com/RedColdHearted/square_exam.git
cd square_exam
source .venv/bin/activate
pip install -r requirements.txt
```

### With poetry 
```bash
pyenv install 3.12
pyenv shell $(pyenv latest 3.12)
poetry env use $(which python) && poetry install && source .venv/bin/activate
```

### Run server
```bash
uvicorn main:app --reload
```