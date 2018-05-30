import _plotly_utils.basevalidators


class YboundssrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='yboundssrc', parent_name='pointcloud', **kwargs
    ):
        super(YboundssrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
