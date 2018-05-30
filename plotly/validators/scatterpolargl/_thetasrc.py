import _plotly_utils.basevalidators


class ThetasrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='thetasrc', parent_name='scatterpolargl', **kwargs
    ):
        super(ThetasrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
