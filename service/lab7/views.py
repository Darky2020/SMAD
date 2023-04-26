from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request, APIRouter
from .functions import *
from .data import sample

router = APIRouter(prefix="")

templates = Jinja2Templates(directory="templates")

@router.get("/lab7", response_class=HTMLResponse)
async def read_item(request: Request):

    sample_x_table = "<table><tbody>"
    for i in range(2):
        sample_x_table += "<tr>"
        n = int(len(sample["x"])/2)
        for y in range(n):
            sample_x_table += f"<td>{sample['x'][i*n + y]}</td>"
        sample_x_table += "</tr>"
    sample_x_table += "</tbody></table>"

    sample_y_table = "<table><tbody>"
    for i in range(2):
        sample_y_table += "<tr>"
        n = int(len(sample["y"])/2)
        for y in range(n):
            sample_y_table += f"<td>{sample['y'][i*n + y]}</td>"
        sample_y_table += "</tr>"
    sample_y_table += "</tbody></table>"

    function_1 = f"y* = {round(LeastSquaresMethod.alpha_x(), 3)} + {round(LeastSquaresMethod.beta_x(), 3)}x*"
    function_2 = f"x* = {round(LeastSquaresMethod.alpha_y(), 3)} + {round(LeastSquaresMethod.beta_y(), 3)}y*"
    function_3 = f"x* - {round(StaticCorrelationCoefficientMethod.avg_x(), 3)} = {round(StaticCorrelationCoefficientMethod.r_x_to_y(), 3)}(y*-{round(StaticCorrelationCoefficientMethod.avg_y(), 3)})"
    function_4 = f"y* - {round(StaticCorrelationCoefficientMethod.avg_y(), 3)} = {round(StaticCorrelationCoefficientMethod.r_y_to_x(), 3)}(x*-{round(StaticCorrelationCoefficientMethod.avg_x(), 3)})"

    return templates.TemplateResponse(
        "lab7.html",
        {
            "request": request,
            "sample_x_table": sample_x_table,
            "sample_y_table": sample_y_table,
            "det_x": round(LeastSquaresMethod.determinant_x(), 4),
            "det_y": round(LeastSquaresMethod.determinant_y(), 4),
            "d_alpha_x": round(LeastSquaresMethod.d_alpha_x(), 4),
            "d_alpha_y": round(LeastSquaresMethod.d_alpha_y(), 4),
            "d_beta_x": round(LeastSquaresMethod.d_beta_x(), 4),
            "d_beta_y": round(LeastSquaresMethod.d_beta_y(), 4),
            "alpha_x": round(LeastSquaresMethod.alpha_x(), 4),
            "alpha_y": round(LeastSquaresMethod.alpha_y(), 4),
            "beta_x": round(LeastSquaresMethod.beta_x(), 4),
            "beta_y": round(LeastSquaresMethod.beta_y(), 4),
            "function_1": function_1,
            "function_2": function_2,
            "function_3": function_3,
            "function_4": function_4,

            "r_xy": round(StaticCorrelationCoefficientMethod.r_xy(), 4),
            "avg_x": round(StaticCorrelationCoefficientMethod.avg_x(), 4),
            "avg_y": round(StaticCorrelationCoefficientMethod.avg_y(), 4),
            "s_0x": round(StaticCorrelationCoefficientMethod.S_0x(), 4),
            "s_0y": round(StaticCorrelationCoefficientMethod.S_0y(), 4),
            "r_x_to_y": round(StaticCorrelationCoefficientMethod.r_x_to_y(), 4),
            "r_y_to_x": round(StaticCorrelationCoefficientMethod.r_y_to_x(), 4),
        }
    )
