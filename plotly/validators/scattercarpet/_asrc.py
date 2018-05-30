import _plotly_utils.basevalidators


class AsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='asrc', parent_name='scattercarpet', **kwargs
    ):
        super(AsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
