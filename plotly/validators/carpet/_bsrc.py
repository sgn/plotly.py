import _plotly_utils.basevalidators


class BsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(self, plotly_name='bsrc', parent_name='carpet', **kwargs):
        super(BsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
