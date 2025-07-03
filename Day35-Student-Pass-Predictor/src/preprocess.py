import pandas
import pandas as pd



def preprocess_input(student_dict, transformer):
    """
       Accepts a single student input as a dictionary, converts to DataFrame,
       and applies the transformer.

       Args:
           student_dict (dict): Output of Student.to_dict()
           transformer (ColumnTransformer): Pre-fitted transformer

       Returns:
           transformed_input (np.array): Preprocessed feature array
    """
    df = pd.DataFrame([student_dict])
    return transformer.transform(df)










