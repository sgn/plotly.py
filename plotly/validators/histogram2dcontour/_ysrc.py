import _plotly_utils.basevalidators


class YsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='ysrc', parent_name='histogram2dcontour', **kwargs
    ):
        super(YsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
