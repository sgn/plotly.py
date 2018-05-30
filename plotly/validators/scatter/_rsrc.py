import _plotly_utils.basevalidators


class RsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(self, plotly_name='rsrc', parent_name='scatter', **kwargs):
        super(RsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
