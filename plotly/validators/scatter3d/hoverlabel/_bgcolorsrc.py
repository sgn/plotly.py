import _plotly_utils.basevalidators


class BgcolorsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self,
        plotly_name='bgcolorsrc',
        parent_name='scatter3d.hoverlabel',
        **kwargs
    ):
        super(BgcolorsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
