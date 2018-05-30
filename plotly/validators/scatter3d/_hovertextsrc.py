import _plotly_utils.basevalidators


class HovertextsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='hovertextsrc', parent_name='scatter3d', **kwargs
    ):
        super(HovertextsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
