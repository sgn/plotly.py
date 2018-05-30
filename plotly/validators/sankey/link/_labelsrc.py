import _plotly_utils.basevalidators


class LabelsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='labelsrc', parent_name='sankey.link', **kwargs
    ):
        super(LabelsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
