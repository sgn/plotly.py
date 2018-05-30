import _plotly_utils.basevalidators


class SubunitwidthValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='subunitwidth', parent_name='layout.geo', **kwargs
    ):
        super(SubunitwidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            min=0,
            role='style',
            **kwargs
        )
