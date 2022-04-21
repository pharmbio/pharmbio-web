+++
title = "Assessing the Calibration in Toxicological in Vitro Models with Conformal Prediction"
date = 2021-04-12T20:49:00+02:00
doi = "10.1186/s13321-021-00511-5"
url_html = ""
journal = "Journal of Cheminformatics"
author = "Morger A, Svensson F, Arvidsson McShane S, Gauraha N, Norinder U, Spjuth O, Volkamer A"
volume = "13"
number = "35"
art_number = ""
pages = ""
year = "2021"
keywords = ""
document_bibtex_type = ""
abstract = "Machine learning methods are widely used in drug discovery and toxicity prediction. While showing overall good performance in cross-validation studies, their predictive power (often) drops in cases where the query samples have drifted from the training data’s descriptor space. Thus, the assumption for applying machine learning algorithms, that training and test data stem from the same distribution, might not always be fulfilled. In this work, conformal prediction is used to assess the calibration of the models. Deviations from the expected error may indicate that training and test data originate from different distributions. Exemplified on the Tox21 datasets, composed of chronologically released Tox21Train, Tox21Test and Tox21Score subsets, we observed that while internally valid models could be trained using cross-validation on Tox21Train, predictions on the external Tox21Score data resulted in higher error rates than expected. To improve the prediction on the external sets, a strategy exchanging the calibration set with more recent data, such as Tox21Test, has successfully been introduced. We conclude that conformal prediction can be used to diagnose data drifts and other issues related to model calibration. The proposed improvement strategy—exchanging the calibration data only—is convenient as it does not require retraining of the underlying model."
# --- Pharmb.io custom fields ---
short_summary = ""
users = ["olas"]
projects = [""]
# --- Tentative URL fields ---
url_repo_data = ""
url_repo_paper = ""
url_repo_code = ""
url_repo_notebook = ""
url_tutorial = ""
+++
