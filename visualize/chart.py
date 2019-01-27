stacked_area_template = {
    "data": {
        "x": "x",
        "columns": [],
        "types": {
            "profits": 'area-spline',
            "invested": 'area-spline',
        },
        "groups": [['profits', 'invested']]
    },
    "axis": {
        "x": {
            "type": 'timeseries',
            "tick": {
                "format": '%Y-%m-%d'
            }
        }
    }
}
html = """
<style>
iframe {border:0;}
</style>
"""


class Chart(object):

    html = html

    def stacked_area(self, x, profits, invested):
        x.insert(0, 'x')
        profits.insert(0, 'profits')
        invested.insert(0, 'invested')
        stacked_area_template['data']['columns'] = [x, profits, invested]
        return stacked_area_template
