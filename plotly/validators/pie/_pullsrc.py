import _plotly_utils.basevalidators


class PullsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(self, plotly_name='pullsrc', parent_name='pie', **kwargs):
        super(PullsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
