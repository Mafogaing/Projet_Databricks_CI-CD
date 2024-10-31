from notebooks.train_model import main
import os
import sys
from os.path import abspath, dirname

sys.path.insert(0, abspath(dirname(dirname(__file__))))


def test_model_training():
    # Run the main function
    main()
    # Check if MLflow run exists
    assert os.path.exists("mlruns"), "MLflow run not found"

    # Additional tests can be added here

#$env:PYTHONPATH = "E:\Projet_Databricks_CI-CD"; pytest tests/  (commande d'exécution)
