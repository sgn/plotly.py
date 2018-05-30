import _plotly_utils.basevalidators


class ZsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='zsrc', parent_name='contourcarpet', **kwargs
    ):
        super(ZsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
