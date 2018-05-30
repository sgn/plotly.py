import _plotly_utils.basevalidators


class NamelengthsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self,
        plotly_name='namelengthsrc',
        parent_name='bar.hoverlabel',
        **kwargs
    ):
        super(NamelengthsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
