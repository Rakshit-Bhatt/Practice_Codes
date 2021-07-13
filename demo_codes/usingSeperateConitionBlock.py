#using smarter way to organiseour long list of conditions in a seperate block
#to use functionaly of 'AND', use all()
#to use functionaly of 'OR', use any()

for i in df.index:
    conditions=[
            df.loc[i, 'Duration']>60,
            df.loc[i, 'Date']==np.NAN,
            df.loc[i, 'Pulse']==np.NAN,
            df.loc[i, 'Maxpulse']==np.NaN,
            df.loc[i, 'Calories']==np.NaN
            ]
    if any(conditions):
        df.drop(i)