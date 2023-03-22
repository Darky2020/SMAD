from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request, APIRouter
from . import functions
from .data import data

router = APIRouter(prefix="")

templates = Jinja2Templates(directory="templates")

@router.get("/lab1", response_class=HTMLResponse)
async def read_item(request: Request, k: int = 2):

    return templates.TemplateResponse(
        "lab1.html",
        {
            "request": request,
            "data": str(data),
            "count": len(data),
            "average": functions.average(),
            "mode": str(functions.mode()),
            "median": str(functions.median()),
            "range": str(functions.range()),
            "dispersion": functions.dispersion(),
            "avg_quad_deviation": functions.avg_quad_deviation(),
            "adj_dispersion": functions.adj_dispersion(),
            "adj_aqd": functions.adj_aqd(),
            "variation": functions.variation(),
            "starting_moment": functions.starting_moment(k),
            "central_moment": functions.central_moment(k),
            "k": k,
            "skewness": functions.skewness(),
            "kurtosis": functions.kurtosis()
        }
    )
