import os
from pathlib import Path
package_name="DiamondPricePrediction"

list_of_file=[
    "github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/components/data_transformation.py",
    f"src/{package_name}/components/model_trainer.py",
    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/trainer_pipeline.py",
    f"src/{package_name}/pipelines/prediction_pipeline.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/utils/__init__.py",
    "notebooks/research.ipynb",
    "notebooks/data/.gitkeep",
    "requirements.txt",
    "setup.py",
    "init_setup.sh"
    ]

# Here I am creating a Directory
for filepath in list_of_file:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    print(filedir,filename)
    """
    I will use here exist_ok for already existing directory and os.makedirs() will
    not raise any error .
    """
    #print(filedir," ===",filename)
    if filedir != "":
        print(filedir)
        os.makedirs(filedir,exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
    else:
        print("File already exists")