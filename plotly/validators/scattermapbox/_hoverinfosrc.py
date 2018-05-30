import _plotly_utils.basevalidators


class HoverinfosrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self,
        plotly_name='hoverinfosrc',
        parent_name='scattermapbox',
        **kwargs
    ):
        super(HoverinfosrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
