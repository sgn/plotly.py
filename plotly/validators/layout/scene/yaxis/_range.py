import _plotly_utils.basevalidators


class RangeValidator(_plotly_utils.basevalidators.InfoArrayValidator):

    def __init__(
        self, plotly_name='range', parent_name='layout.scene.yaxis', **kwargs
    ):
        super(RangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            implied_edits={'autorange': False},
            items=[
                {
                    'editType': 'plot',
                    'impliedEdits': {
                        '^autorange': False
                    },
                    'valType': 'any'
                }, {
                    'editType': 'plot',
                    'impliedEdits': {
                        '^autorange': False
                    },
                    'valType': 'any'
                }
            ],
            role='info',
            **kwargs
        )
