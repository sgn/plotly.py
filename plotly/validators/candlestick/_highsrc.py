import _plotly_utils.basevalidators


class HighsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='highsrc', parent_name='candlestick', **kwargs
    ):
        super(HighsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
