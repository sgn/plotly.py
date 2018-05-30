import _plotly_utils.basevalidators


class OrientationValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='orientation', parent_name='layout.legend', **kwargs
    ):
        super(OrientationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='legend',
            role='info',
            values=['v', 'h'],
            **kwargs
        )
