import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine


def enlarge(n):
    '''
    Param n is a number.
    Function will enlarge the number
    '''
    return n * 100


def train_validation_test_split(df, features, target,
                                train_size=0.7, val_size=0.1,
                                test_size=0.2, random_state=None,
                                shuffle=True):
    '''
    This function is a utility wrapper around the Scikit-Learn train_test_split arrays or
    matrices into train, validation and test subsets.

    Args:
        X (Numpy array or DataFrame): This is a dataframe with features.
        y (Numpy array or DataFrame): This is a pandas Series with target.
        train_xize (float or int): Proportion of the dataset to include in the train fplit (0-1).
        val_size (float or int): Proportion of the dataset to include in the validation split (0-1).
        test_size (float or int): Proportion of the dataset to include in the test split (0-1).
        random_state (int): Controls the suffling applied to the data before applying the split for reproducibility.
        shuffle (bool): Whether or not to shuffle the data before splitting.
    
    Returns:
        Train, test, and validation dataframes for features (X) and target(y).
    '''

    X = df[features]
    y = df[target]


    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, shuffle=shuffle)
    
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=val_size / (train_size + val_size),
        random_state=random_state, shuffle=shuffle)
    
    return X_train, X_val, X_test, y_train, y_val, y_test


if __name__ == '__main__':
    # print(enlarge(5))

    raw_data = load_wine()
    df = pd.DataFrame(data=raw_data['data'], columns=raw_data['feature_names'])
    df['target'] = raw_data['target']

    X_train, X_val, X_test, y_train, y_val, y_test = train_validation_test_split(
        df, ['ash','hue'], target='target')
    
    breakpoint()
