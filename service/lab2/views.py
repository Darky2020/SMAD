from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request, APIRouter
from . import functions
from .data import data

router = APIRouter(prefix="")

templates = Jinja2Templates(directory="templates")

@router.get("/lab2", response_class=HTMLResponse)
async def read_item(request: Request, k: int = 2):

    data_table = "<table><tbody>"

    for i in range(3):
        data_table += "<tr>"

        for y in range(int(len(data)/3)):
            data_table += f"<td>{data[i*int(len(data)/3) + y]}</td>"

        data_table += "</tr>"

    data_table += "</tbody></table>"

    interval_data = "<table><tbody>"

    interval_data += f"<tr><td>Інтервали</td>"
    for interval in functions.interval_stat_series():
        interval_data += f"<td>{interval['range_str']}</td>"
    interval_data += "</tr>"

    interval_data += f"<tr><td>z<sub>i</sub></td>"
    for interval in functions.interval_stat_series():
        interval_data += f"<td>{str(round(interval['avg'], 5))}</td>"
    interval_data += "</tr>"

    interval_data += f"<tr><td>m<sub>i</sub></td>"
    for interval in functions.interval_stat_series():
        interval_data += f"<td>{str(interval['count'])}</td>"
    interval_data += "</tr>"

    interval_data += "</tbody></table>"

    return templates.TemplateResponse(
        "lab2.html",
        {
            "request":       request,
            "data":          data_table,
            "interval_data": interval_data,
            "count":         len(data),
            "average":       round(functions.average(), 6),
            "mode":          str(functions.mode()),
            "exact_mode":    str(functions.exact_mode()),
            "median":        round(functions.median(), 6),
            "exact_median":  round(functions.exact_median(), 6),
            "range":         round(functions.distribution_range(), 6),
            "dispersion":    round(functions.dispersion(), 6),
            "avg_quad_deviation": round(functions.square_deviation(), 6),
            "adj_dispersion":  round(functions.adjusted_dispersion(), 6),
            "adj_aqd":         round(functions.adjusted_square_deviation(), 6),
            "variation":       round(functions.variation(), 6),
            "starting_moment": round(functions.starting_moment(k), 6),
            "central_moment":  round(functions.central_moment(k), 6),
            "k": k,
            "skewness": round(functions.skewness(), 6),
            "kurtosis": round(functions.kurtosis(), 6)
        }
    )
