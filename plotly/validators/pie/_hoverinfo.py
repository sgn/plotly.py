import _plotly_utils.basevalidators


class HoverinfoValidator(_plotly_utils.basevalidators.FlaglistValidator):

    def __init__(self, plotly_name='hoverinfo', parent_name='pie', **kwargs):
        super(HoverinfoValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=True,
            edit_type='none',
            extras=['all', 'none', 'skip'],
            flags=['label', 'text', 'value', 'percent', 'name'],
            role='info',
            **kwargs
        )
