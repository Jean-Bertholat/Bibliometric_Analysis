import pybliometrics
import pybliometrics.scopus

pybliometrics.scopus.init(config_dir="pybliometrics.cfg")

query = 'cybersecurity'
s = pybliometrics.scopus.ScopusSearch(query, verbose=True)
print(f"Nombre de résultats trouvés : {s.get_results_size()}")
