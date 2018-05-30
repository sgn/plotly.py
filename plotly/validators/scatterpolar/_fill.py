import _plotly_utils.basevalidators


class FillValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='fill', parent_name='scatterpolar', **kwargs
    ):
        super(FillValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='style',
            values=['none', 'toself', 'tonext'],
            **kwargs
        )
