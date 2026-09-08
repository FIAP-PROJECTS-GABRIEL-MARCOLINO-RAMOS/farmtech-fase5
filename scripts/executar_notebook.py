"""Executa o relatório em kernel novo e salva as saídas no próprio notebook."""
from pathlib import Path
import sys
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager

ROOT = Path(__file__).resolve().parents[1]
path = next((ROOT / "notebooks").glob("*_pbl_fase4.ipynb"))
notebook = nbformat.read(path, as_version=4)
# Usa o mesmo Python do script, inclusive dentro de um ambiente virtual.
manager = KernelManager(kernel_name="python3")
manager.kernel_spec.argv = [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"]
client = NotebookClient(notebook, km=manager, timeout=600,
                        resources={"metadata": {"path": str(ROOT)}})
client.execute()
nbformat.validate(notebook)
nbformat.write(notebook, path)
print(f"Notebook executado sem erros: {path.name}")
