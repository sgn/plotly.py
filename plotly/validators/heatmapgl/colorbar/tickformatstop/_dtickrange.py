import _plotly_utils.basevalidators


class DtickrangeValidator(_plotly_utils.basevalidators.InfoArrayValidator):

    def __init__(
        self,
        plotly_name='dtickrange',
        parent_name='heatmapgl.colorbar.tickformatstop',
        **kwargs
    ):
        super(DtickrangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            items=[
                {
                    'editType': 'calc',
                    'valType': 'any'
                }, {
                    'editType': 'calc',
                    'valType': 'any'
                }
            ],
            role='info',
            **kwargs
        )
