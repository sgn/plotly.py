import _plotly_utils.basevalidators


class CsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='csrc', parent_name='scatterternary', **kwargs
    ):
        super(CsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
