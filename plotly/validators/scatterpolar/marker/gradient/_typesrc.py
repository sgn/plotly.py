import _plotly_utils.basevalidators


class TypesrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self,
        plotly_name='typesrc',
        parent_name='scatterpolar.marker.gradient',
        **kwargs
    ):
        super(TypesrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
