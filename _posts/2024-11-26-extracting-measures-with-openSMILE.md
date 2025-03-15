---
layout: post
title: Extracting measures with openSMILE ✲ﾟ｡.(✿╹◡╹)ﾉ☆.｡₀:*ﾟ✲*:₀｡
---
While I didn't get the opportunity to pursue my endeavors in speech processing just yet, I still gathered a bunch of resources over the course of my degree, which I thought I'd share, as speech processing tools can be a little niche. In this tutorial, we'll see how to use the [openSMILE](https://github.com/audeering/opensmile) toolkit for feature extraction, and later plot formants. 

<!-- more -->

**openSMILE** is an *extensive*, *open-source*, toolkit for audio analysis, processing and classification, which is aimed for speech and music applications. Specifically, it allows researchers to easily run feature extraction, either via CLI or its Python wrapper, `opensmile-python`. openSMILE is maintained by **audEERING**, a german company working on audio technology and the use of AI for various tasks (speech synthesis/text-to-speech...).

In this tutorial, we will see how to work with openSMILE's Python wrapper to easily extract features from a short audio segment. 

```python
import opensmile
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
```

### extracting audio features ( ・\_・)ノ
GeMAPSv01b

```python
file = "path/to/audio/file" # wav
smile = opensmile.Smile(
		feature_set=opensmile.FeatureSet.GeMAPSv01b,
		feature_level=opensmile.FeatureLevel.LowLevelDescriptors
)
results = smile.process_file(file) # resulting DataFrame
results.head()
```

As you can see here, we're working with 3 indexes: `file`, `start`, and `end`, the last two being time dimensions. If those look weird, it's because of the data type: time here is expressed as a "duration" (the corresponding `pandas` datatype is `timedelta`). We'll convert those later to make things easier.

### plotting formants (｡･o･｡)ﾉ
```python
# extract center formant frequencies
df = pd.read_csv('extracted_features_pandas.csv')
centerformantfreqs = ['start','F1frequency_sma3nz',
                      'F2frequency_sma3nz', 'F3frequency_sma3nz']
formants = df[centerformantfreqs] # new dataframe with the columns we are interested in only
# resulting dataframe
formants.head()
```

```python
sns.lineplot(data=formants, x='start', y='F1frequency_sma3nz')
sns.lineplot(data=formants, x='start', y='F2frequency_sma3nz')
sns.lineplot(data=formants, x='start', y='F3frequency_sma3nz')
plt.xlabel('time (ms)')
plt.title('extracted formants')
plt.show()
```

### additional resources
- [speech surfer](), a great blog about speech processing technologies. They have quite a few tutorials for openSMILE! It is through one of their tutorials that I learnt how to use it. 
