import _plotly_utils.basevalidators


class ContourValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='contour', parent_name='', **kwargs):
        super(ContourValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Contour',
            data_docs="""
            autocolorscale
                Determines whether or not the colorscale is
                picked using the sign of the input z values.
            autocontour
                Determines whether or not the contour level
                attributes are picked by an algorithm. If
                *true*, the number of contour levels can be set
                in `ncontours`. If *false*, set the contour
                level attributes in `contours`.
            colorbar
                plotly.graph_objs.contour.ColorBar instance or
                dict with compatible properties
            colorscale
                Sets the colorscale. The colorscale must be an
                array containing arrays mapping a normalized
                value to an rgb, rgba, hex, hsl, hsv, or named
                color string. At minimum, a mapping for the
                lowest (0) and highest (1) values are required.
                For example, `[[0, 'rgb(0,0,255)', [1,
                'rgb(255,0,0)']]`. To control the bounds of the
                colorscale in z space, use zmin and zmax
            connectgaps
                Determines whether or not gaps (i.e. {nan} or
                missing values) in the `z` data are filled in.
            contours
                plotly.graph_objs.contour.Contours instance or
                dict with compatible properties
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, *scatter* traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            dx
                Sets the x coordinate step. See `x0` for more
                info.
            dy
                Sets the y coordinate step. See `y0` for more
                info.
            fillcolor
                Sets the fill color if `contours.type` is
                *constraint*. Defaults to a half-transparent
                variant of the line color, marker color, or
                marker line color, whichever is available.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                plotly.graph_objs.contour.Hoverlabel instance
                or dict with compatible properties
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                plotly.graph_objs.contour.Line instance or dict
                with compatible properties
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            ncontours
                Sets the maximum number of contour levels. The
                actual number of contours will be chosen
                automatically to be less than or equal to the
                value of `ncontours`. Has an effect only if
                `autocontour` is *true* or if `contours.size`
                is missing.
            opacity
                Sets the opacity of the trace.
            reversescale
                Reverses the colorscale.
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace.
            stream
                plotly.graph_objs.contour.Stream instance or
                dict with compatible properties
            text
                Sets the text elements associated with each z
                value.
            textsrc
                Sets the source reference on plot.ly for  text
                .
            transpose
                Transposes the z data.
            uid

            visible
                Determines whether or not this trace is
                visible. If *legendonly*, the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            x
                Sets the x coordinates.
            x0
                Alternate to `x`. Builds a linear space of x
                coordinates. Use with `dx` where `x0` is the
                starting coordinate and `dx` the step.
            xaxis
                Sets a reference between this trace's x
                coordinates and a 2D cartesian x axis. If *x*
                (the default value), the x coordinates refer to
                `layout.xaxis`. If *x2*, the x coordinates
                refer to `layout.xaxis2`, and so on.
            xcalendar
                Sets the calendar system to use with `x` date
                data.
            xsrc
                Sets the source reference on plot.ly for  x .
            xtype
                If *array*, the heatmap's x coordinates are
                given by *x* (the default behavior when `x` is
                provided). If *scaled*, the heatmap's x
                coordinates are given by *x0* and *dx* (the
                default behavior when `x` is not provided).
            y
                Sets the y coordinates.
            y0
                Alternate to `y`. Builds a linear space of y
                coordinates. Use with `dy` where `y0` is the
                starting coordinate and `dy` the step.
            yaxis
                Sets a reference between this trace's y
                coordinates and a 2D cartesian y axis. If *y*
                (the default value), the y coordinates refer to
                `layout.yaxis`. If *y2*, the y coordinates
                refer to `layout.xaxis2`, and so on.
            ycalendar
                Sets the calendar system to use with `y` date
                data.
            ysrc
                Sets the source reference on plot.ly for  y .
            ytype
                If *array*, the heatmap's y coordinates are
                given by *y* (the default behavior when `y` is
                provided) If *scaled*, the heatmap's y
                coordinates are given by *y0* and *dy* (the
                default behavior when `y` is not provided)
            z
                Sets the z data.
            zauto
                Determines the whether or not the color domain
                is computed with respect to the input data.
            zhoverformat
                Sets the hover text formatting rule using d3
                formatting mini-languages which are very
                similar to those in Python. See: https://github
                .com/d3/d3-format/blob/master/README.md#locale_
                format
            zmax
                Sets the upper bound of color domain.
            zmin
                Sets the lower bound of color domain.
            zsrc
                Sets the source reference on plot.ly for  z .""",
            **kwargs
        )
