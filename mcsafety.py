import json
import urllib2
import pygal
#from kitchen.text.converters import to_bytes

#from pygal.style import NeonStyle

#data = json.load(urllib2.urlopen('http://mcsafetyfeed.org/api/counts.php?type=incidentstoday'))
data = json.load(urllib2.urlopen('http://mcsafetyfeed.org/api/counts.php?type=incidentstoday&date=2013-02-08'))

counts = []
labels = []


chart = pygal.Bar()
for d in data:
    chart.add(d['event'], [{'value': int(d["count"]), 'label': d['event']}])
    labels.append(d["letter"])


chart.x_labels = labels
chart.add('Counts', counts)
chart.render_in_browser()
