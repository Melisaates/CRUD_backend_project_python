from leanapi.path import controller
from leanapi.server import router
from sqlraw.sqlraw import SqlRaw
from starlette import status
from starlette.responses import JSONResponse
from api.config import Config


@controller("app", router)
class Brand:
    @router.get('/brand/{brand_id}', status_code=status.HTTP_200_OK, tags=["brand"])
    def get_brand(self, brand_id: int):
        sqlraw = SqlRaw.paths(["api/routes/brand/model"])
        sqlraw.load("brand.sql").connect(Config.conn)
        list = sqlraw.fetchone({"brand_id": brand_id})
        if list:
            return "list"
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content={"message": "brand id not found"})

