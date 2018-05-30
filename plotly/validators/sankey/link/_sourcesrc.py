import _plotly_utils.basevalidators


class SourcesrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='sourcesrc', parent_name='sankey.link', **kwargs
    ):
        super(SourcesrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
