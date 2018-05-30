import _plotly_utils.basevalidators


class ZsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='zsrc', parent_name='histogram2dcontour', **kwargs
    ):
        super(ZsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
