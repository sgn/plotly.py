import _plotly_utils.basevalidators


class SizesrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self,
        plotly_name='sizesrc',
        parent_name='sankey.hoverlabel.font',
        **kwargs
    ):
        super(SizesrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
