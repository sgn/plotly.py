import _plotly_utils.basevalidators


class TextsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='textsrc', parent_name='scattermapbox', **kwargs
    ):
        super(TextsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
