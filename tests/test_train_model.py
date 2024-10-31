from notebooks.train_model import main
import os

def test_model_training():
    # Run the main function
    main()
    # Check if MLflow run exists
    assert os.path.exists("mlruns"), "MLflow run not found"

    # Additional tests can be added here