def get_samples_metadata_columns():
    import pandas as pd
    samples_meta_df = pd.read_csv('Belly_Button_Biodiversity_Metadata.csv')
    return list(samples_meta_df.columns)

def get_samples_metadata_values():
    import pandas as pd
    samples_meta_df = pd.read_csv('Belly_Button_Biodiversity_Metadata.csv')
    return samples_meta_df.values.tolist()

def get_otu_pie_labels():
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
    Otu = Base.classes.otu
    session = Session(engine)
    otu_id_list = session.query(Otu.otu_id).all()
    otu_taxonomic_list = session.query(Otu.lowest_taxonomic_unit_found).all()
    otu_id = pd.DataFrame(otu_id_list)
    otu_taxonomic = pd.DataFrame(otu_taxonomic_list)
    otu_df = otu_id.join(otu_taxonomic)
    new_otu_df = otu_df.groupby('lowest_taxonomic_unit_found').count().sort_values(by=['otu_id'], ascending=False).reset_index()
    final_new_otu_df = new_otu_df.rename(columns={'otu_id' : "count"})
    otu_id_df = otu_df.groupby('lowest_taxonomic_unit_found').max().reset_index()
    final_otu_df = final_new_otu_df.merge(otu_id_df, how='inner', on='lowest_taxonomic_unit_found')
    named_labels = list(final_otu_df[:10]['otu_id'])
    return named_labels
   
def get_otu_pie_values():
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
    Otu = Base.classes.otu
    session = Session(engine)
    otu_id_list = session.query(Otu.otu_id).all()
    otu_taxonomic_list = session.query(Otu.lowest_taxonomic_unit_found).all()
    otu_id = pd.DataFrame(otu_id_list)
    otu_taxonomic = pd.DataFrame(otu_taxonomic_list)
    otu_df = otu_id.join(otu_taxonomic)
    new_otu_df = otu_df.groupby('lowest_taxonomic_unit_found').count().sort_values(by=['otu_id'], ascending=False).reset_index()
    named_otu_pie = list(new_otu_df[:10]['otu_id'].values)
   
    final_named_otu_pie = []
    for i in named_otu_pie:
        final_named_otu_pie.append(int(i))
        
    return final_named_otu_pie
    
    return named_otu_pie

def get_samples():
    import pandas as pd
    samples_df = pd.read_csv('belly_button_biodiversity_samples.csv')
    return list(samples_df.columns[1:])
