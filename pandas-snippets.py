"""
This is just to demonstrate some techniques; this file isn't designed to be imported as a module or run as script!
With that said, let's import pandas and begin...
"""
import pandas as pd


# HDFStore
store = pd.HDFStore('data_name.h5')
group_map = dict(
    A = dict(
        fields = ['field_example_one', 'etc']
    )
)

# Clean 'dirty' strings into floats
pd.to_numeric(df, errors='coerce')

# Clean strings to ints
df.ID = pd.to_numeric(df.ID, errors='coerce').fillna(0).astype(np.int64)
# make a 'year' column with ints
df['year'] = pd.to_numeric(df.name.str[:4], errors='coerce').fillna(0).astype(np.int64)
# Force to int, works if strings are 'clean' numbers
df.name.astype(int)

# pandas and csv shenanigans
try:
    # load csv into a pandas DataFrame (header=None is optional)
    df = pd.read_csv(backend_csv_file, header=None)
    with open(backend_csv_file, 'w+') as clear_the_csv:
        # make sure no GIL on file
        clear_the_csv.close()
    # iterate through the DataFrame using indices to locate test reqeust strings
    for index, row in df.iterrows():
        # make a url
        test_in = domain_public + str(row[2])
        print(test_in)
except IOError as e:
    with open(failed_csv, 'a') as note_failures:
        note_failures.close()

# List unique values in a DataFrame column
pd.unique(df.column_name.ravel())

# Convert Series datatype to numeric, getting rid of any non-numeric values
df['col'] = df['col'].astype(str).convert_objects(convert_numeric=True)

# Grab DataFrame rows where column has certain values
valuelist = ['value1', 'value2', 'value3']
df = df[df.column.isin(valuelist)]

# Grab DataFrame rows where column doesn't have certain values
valuelist = ['value1', 'value2', 'value3']
df = df[~df.column.isin(value_list)]

# Delete column from DataFrame
del df['column']

# Select from DataFrame using criteria from multiple columns
# (use `|` instead of `&` to do an OR)
newdf = df[(df['column_one']>2004) & (df['column_two']==9)]

# Rename several DataFrame columns
df = df.rename(columns = {
    'col1 old name':'col1 new name',
    'col2 old name':'col2 new name',
    'col3 old name':'col3 new name',
})

# Lower-case all DataFrame column names
df.columns = map(str.lower, df.columns)

# Even more fancy DataFrame column re-naming
# lower-case all DataFrame column names (for example)
df.rename(columns=lambda x: x.split('.')[-1], inplace=True)

# Loop through rows in a DataFrame
# (if you must)
for index, row in df.iterrows():
    print index, row['some column']

# Next few examples show how to work with text data in Pandas.
# Full list of .str functions: http://pandas.pydata.org/pandas-docs/stable/text.html

# Slice values in a DataFrame column (aka Series)
df.column.str[0:2]

# Lower-case everything in a DataFrame column
df.column_name = df.column_name.str.lower()

# Get length of data in a DataFrame column
df.column_name.str.len()

# load csv into a pandas DataFrame (header=None is optional)
df = pd.read_csv('path/example.csv', header=None)
# same but specify columns
df = pd.read_csv('path/example.csv', names=['one' ,'two' ,'4th'])
# same but skip top 3 rows
df = pd.read_csv('path/example.csv', na_values=sentinels, skiprows=3)

# Sort dataframe by multiple columns
df = df.sort(['col1','col2','col3'],ascending=[1,1,0])

# Get top n for each group of columns in a sorted dataframe
# (make sure dataframe is sorted first)
top5 = df.groupby(['groupingcol1', 'groupingcol2']).head(5)

# Grab DataFrame rows where specific column is null/notnull
newdf = df[df['column'].isnull()]

# Select from DataFrame using multiple keys of a hierarchical index
df.xs(('index level 1 value','index level 2 value'), level=('level 1','level 2'))

# Change all NaNs to None (useful before
# loading to a db)
df = df.where((pd.notnull(df)), None)

# More pre-db insert cleanup...make a pass through the dataframe, stripping whitespace
# from strings and changing any empty values to None
# (not especially recommended but including here b/c I had to do this in real life one time)
df = df.applymap(lambda x: str(x).strip() if len(str(x).strip()) else None)

# Get quick count of rows in a DataFrame
len(df.index)

# Pivot data (with flexibility about what what
# becomes a column and what stays a row).
# Syntax works on Pandas >= .14
pd.pivot_table(
  df,values='cell_value',
  index=['col1', 'col2', 'col3'], #these stay as columns; will fail silently if any of these cols have null values
  columns=['col4']) #data values in this column become their own column

# Change data type of DataFrame column
df.column_name = df.column_name.astype(np.int64)

# Get rid of non-numeric values throughout a DataFrame:
for col in refunds.columns.values:
  refunds[col] = refunds[col].replace('[^0-9]+.-', '', regex=True)

# Set DataFrame column values based on other column values (h/t: @mlevkov)
df.loc[(df['column1'] == some_value) & (df['column2'] == some_other_value), ['column_to_change']] = new_value

# Clean up missing values in multiple DataFrame columns
df = df.fillna({
    'col1': 'missing',
    'col2': '99.999',
    'col3': '999',
    'col4': 'missing',
    'col5': 'missing',
    'col6': '99'
})

# Concatenate two DataFrame columns into a new, single column
# (useful when dealing with composite keys, for example)
df['newcol'] = df['col1'].map(str) + df['col2'].map(str)

# Doing calculations with DataFrame columns that have missing values
# In example below, swap in 0 for df['col1'] cells that contain null
df['new_col'] = np.where(pd.isnull(df['col1']),0,df['col1']) + df['col2']

# Split delimited values in a DataFrame column into two new columns
df['new_col1'], df['new_col2'] = zip(*df['original_col'].apply(lambda x: x.split(': ', 1)))

# Collapse hierarchical column indexes
df.columns = df.columns.get_level_values(0)

# Convert Django queryset to DataFrame
qs = DjangoModelName.objects.all()
q = qs.values()
df = pd.DataFrame.from_records(q)

# Create a DataFrame from a Python dictionary
df = pd.DataFrame(list(a_dictionary.items()), columns = ['column1', 'column2'])

# Get a report of all duplicate records in a dataframe, based on specific columns
dupes = df[df.duplicated(['col1', 'col2', 'col3'], keep=False)]

# Set up formatting so larger numbers aren't displayed in scientific notation (h/t @thecapacity)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
