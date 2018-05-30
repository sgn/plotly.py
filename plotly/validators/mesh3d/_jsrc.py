import _plotly_utils.basevalidators


class JsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(self, plotly_name='jsrc', parent_name='mesh3d', **kwargs):
        super(JsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
