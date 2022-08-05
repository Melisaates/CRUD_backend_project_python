from leanapi.path import controller
from leanapi.server import router
from sqlraw.sqlraw import SqlRaw
from fastapi import status
from starlette.responses import JSONResponse
from api.config import settings


@controller("app",router)
class District:
    @router.get("/products/",tags=["district"],status_code=status.HTTP_200_OK)
    def get_district(self):
        sql=SqlRaw.paths(["api/routes/district/model"])
        sql.load("district.sql").connect(settings.conn)
        list=sql.fetchall()
        if list:
            return list
        return JSONResponse(status_code = status.HTTP_404_NOT_FOUND,
                            content={"message":"list not found"})