import _plotly_utils.basevalidators


class LocationssrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='locationssrc', parent_name='scattergeo', **kwargs
    ):
        super(LocationssrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
