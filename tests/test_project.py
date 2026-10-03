from pathlib import Path
import py_compile
def test_required_project_files_exist():
required_files = ["server.py", "client.py", "requirements.txt", "README.md"]
for file_name in required_files:
assert Path(file_name).is_file()
def test_server_has_valid_python_syntax():
py_compile.compile("server.py", doraise=True)
def test_client_has_valid_python_syntax():
py_compile.compile("client.py", doraise=True)
