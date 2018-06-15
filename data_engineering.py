import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
from sqlalchemy import func, desc
from matplotlib.ticker import NullFormatter
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import seaborn as sns
from flask import Flask, jsonify
import datetime as dt

engine = create_engine("sqlite:///belly_button_biodiversity.sqlite", echo=False)

Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

Otu = Base.classes.otu
Samples = Base.classes.samples
Samples_MD = Base.classes.samples_metadata

session = Session(engine)

def get_sample_names():
    samples_query = session.query(Samples)
    samples_df = pd.read_sql(samples_query.statement, samples_query.session.bind)
    return list(samples_df.columns[1:])

def otu_descriptions():
    otu_query = session.query(Otu)
    otu_df = pd.read_sql(otu_query.statement, otu_query.session.bind)
    return list(otu_df['lowest_taxonomic_unit_found'].values)

