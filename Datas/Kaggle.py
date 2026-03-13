import pandas as pd


test_df = pd.read_csv('test.csv');
train_df = pd.read_csv('train.csv');

train_df['y'] = train_df['y'].map({'yes': 1, 'no': 0})

submission = pd.DataFrame({
    'id': test_df['id'],
    'y': [0] * len(test_df)
})

submission.to_csv('submission.csv', index=False)
print("Submission file created")
input("Ketik 1")