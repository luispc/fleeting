# -*- coding: utf-8 -*-
"""
PLOT FLEETING FREQUENCIES
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statannotations.Annotator import Annotator

# --- LOAD DATA  
PND=6
df_dur = pd.read_csv(r"lfc_usv_data_pnd"+str(PND)+r"_pub.csv")

print(f"Male: {df_dur[df_dur['sex']=='M']['sex'].count()}")
print(f"Fema: {df_dur[df_dur['sex']=='F']['sex'].count()}")

# --- CHECK AND REMOVE OUTLIERS FOR GIVEN COLUMN
# p_05 = df['f2max'].quantile(0.05) # 5th quantile
# p_95 = df['f2max'].quantile(0.95) # 95th quantile
# df['f2max'].clip(p_05, p_95, inplace=True)


#%% --- PLOT 
fig = plt.figure(figsize=(7, 4),dpi=300)
sns.set(font_scale=1.1)
sns.set_style("whitegrid", {"grid.color": "0.6", 
                            "grid.linestyle": ":",
                            "xtick.major.size": 10,
                            "xtick.minor.size": 5                            
                            })


plotting_param = {
    'x'   : 'seg',
    'y'   : 'freq',
    'hue' : 'sex',
    'data': df_dur,
    'orient':'v'
    }
ax = sns.boxplot(**plotting_param,
                 hue_order=['M','F']
                 )
ax.set_ylim(50,115)
ax.set_xticklabels(['$F1_{ini}$', '$F1_{max}$', '$F1_{end}$', '$F2_{ini}$', '$F2_{max}$','$F2_{end}$'])
plt.xlabel('Time instant')
plt.ylabel('Acoustic frequency (kHz)')

#%%#### PLOT STAT ANNOTATIONS ON CHART
pairs = [ [('f1ini','M'), ('f1ini','F')],
          [('f1max','M'), ('f1max','F')],
          [('f1end','M'), ('f1end','F')],
          [('f2ini','M'), ('f2ini','F')],
          [('f2max','M'), ('f2max','F')],
          [('f2end','M'), ('f2end','F')]
    ]
annotator = Annotator(ax, pairs, **plotting_param)
annotator.configure(
    test='Mann-Whitney', 
    text_format='star', 
    loc='outside'
    )
annotator.apply_and_annotate()

plt.savefig("./fig/freqs"+str(PND)+".svg",format='svg')






