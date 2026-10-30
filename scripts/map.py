"""Generate an approximate Australia operations map from Natural Earth geometry."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
ROOT=Path(__file__).resolve().parents[1]
world=json.loads((ROOT/'site/assets/world.geojson').read_text())
fig, ax=plt.subplots(figsize=(10,6.4)); fig.patch.set_facecolor('#edf2ed'); ax.set_facecolor('#edf2ed')
for f in world['features']:
    if f['properties'].get('name') not in ('Australia','Papua New Guinea','Indonesia','East Timor'): continue
    g=f['geometry']; polygons=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
    for poly in polygons:
        ax.add_patch(Polygon(poly[0],closed=True,facecolor='#d8e1d5',edgecolor='#a6b9ac',linewidth=.65))
points=[('Narngulu / Eneabba / Cataby',115.2,-29.8,-28,27),('Jacinth-Ambrosia',132.34,-30.45,-32,24),('Balranald',143.35,-34.6,-48,25),('Wimmera',142.2,-36.4,-18,-35)]
for name,x,y,dx,dy in points:
    ax.plot(x,y,'o',markersize=8,color='#d47b45',markeredgecolor='white',markeredgewidth=1.5,zorder=3)
    ax.annotate(name,(x,y),xytext=(dx,dy),textcoords='offset points',fontsize=8.4,color='#003e46',fontweight='bold',arrowprops={'arrowstyle':'-','color':'#77968b','lw':.8})
ax.set(xlim=(110,155),ylim=(-44.5,-10),aspect='equal'); ax.axis('off')
fig.text(.11,.06,'Approximate locations • See operation cards for status and source',fontsize=8,color='#45635d')
fig.tight_layout(pad=2); fig.savefig(ROOT/'site/assets/operations-map.svg',facecolor=fig.get_facecolor(),bbox_inches='tight');
